import os
import sys
import json
import datetime
import numpy as np
import pandas as pd
import statistics
import cv2
import skimage.draw
import tensorflow as tf
import keras
import time
import glob 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import RandomizedSearchCV

import joblib
from .mrcnn.config import Config
from .mrcnn import model as modellib, utils

from .mask_saving import Masked_Image
from .Preprocessing_opt import PreprocessImages 


class Sputum:
    """
    Class Sputum contains all the necessary methods for the Mask RCNN Implementation,
    including the training, inference and prediction. Then the Machine Learning Model 
    for evalutation and a scoring method for the final evaluation.

    Parameters
    ----------
    root_dir : str
        Path to the root directory. In this directory the algorithm will be saving all the important files
        such as coco weight file, then inside the log folder, the trained weight files will be saved after 
        every epoch. It is mandatory to set the root_dir.

    """
    def __init__(self,root_dir=None):
        self.root_dir = root_dir


    def train_mask_rcnn(self,dataset_path,weights,epochs):

        """
        This function trains the mask rcnn model based on the dataset and the weights.

        Parameters
        ----------

        dataset_path : str
            Path to the dataset. Inside this path there should be two folders: train and val.
            Inside this train and val folders the annotation file with respect to it should be 
            saved as "train.json" only in both the folers.
        
        weights : str, options= "coco" or path to the saved weight file
            Path to the weight file. If pretained weight exist give that path else give "coco", which will
            download the coco weight file from the internet and save it inside the root directory."

        epochs : int
            Number of epochs for training.

        Returns
        -------
        
        Weight Files
            Trained weight files will be saved inside the root directory.

        """

        # Root directory of the project
        ROOT_DIR = os.path.abspath(self.root_dir)

        print("Root Directory is: ",ROOT_DIR)

        # Import Mask RCNN

        sys.path.append(ROOT_DIR)  # To find local version of the library
        MODEL_DIR = os.path.join(ROOT_DIR, "logs")

        print("Model Directory is: ",MODEL_DIR)
        # Path to trained weights file
        if weights=='coco':
            COCO_WEIGHTS_PATH = os.path.join(ROOT_DIR, "mask_rcnn_coco.h5")
            # Download COCO trained weights from Releases if needed
            if not os.path.exists(COCO_WEIGHTS_PATH):
                utils.download_trained_weights(COCO_WEIGHTS_PATH)
        else: 
            COCO_WEIGHTS_PATH=weights
            if not os.path.exists(COCO_WEIGHTS_PATH):
                print("Invalid Path to weights file")

        # Directory to save logs and model checkpoints, if not provided

        DEFAULT_LOGS_DIR = os.path.join(ROOT_DIR, "logs")
       
        ############################################################
        #  Configurations
        ############################################################


        class SputumConfig(Config):
            """Configuration for training on the hail, hand  dataset.
            Derives from the base Config class and overrides some values.
            """
            # Give the configuration a recognizable name
            NAME = "Sputum"

            # We use a GPU with 12GB memory, which can fit two images.
            # Adjust down if you use a smaller GPU.
            IMAGES_PER_GPU = 1

            # Number of classes (including background)
            NUM_CLASSES = 1 + 1  # Background + ridge + valley

            # Number of training steps per epoch
            STEPS_PER_EPOCH = 100

            # Skip detections with < 80% confidence
            DETECTION_MIN_CONFIDENCE = 0.9

        config = SputumConfig()

        ############################################################
        #  Dataset
        ############################################################

        class SputumDataset(utils.Dataset):

            def load_sputum(self, dataset_dir, subset):
                """Load a subset of the hail dataset.
                dataset_dir: Root directory of the dataset.
                subset: Subset to load: train or val
                """
                # Add classes. We have only one classes to add.
                self.add_class("Sputum", 1, "sputum")


                # Train or validation dataset?
                assert subset in ["train", "val"]
                dataset_dir = os.path.join(dataset_dir, subset)

                annotations = json.load(open(os.path.join(dataset_dir, "train.json")))
                annotations = list(annotations.values())  # don't need the dict keys

                # The VIA tool saves images in the JSON even if they don't have any
                # annotations. Skip unannotated images.
                annotations = [a for a in annotations if a['regions']]

                # Add images
                for a in annotations:

                    polygons = [r['shape_attributes'] for r in a['regions']]
                    objects = [s['region_attributes'] for s in a['regions']]
                    class_ids = [int(n['Sputum']) for n in objects]

                    
                    image_path = os.path.join(dataset_dir, a['filename'])
                    image = skimage.io.imread(image_path)
                    height, width = image.shape[:2]

                    ###changed###
                    for i,p in enumerate(polygons):
                        all_p_x=np.array(p['all_points_x'])
                        all_p_y=np.array(p['all_points_y'])
                        all_p_x[all_p_x>=width]=width-1
                        all_p_y[all_p_y>=height]=height-1
                        polygons[i]['all_points_x']=list(all_p_x)
                        polygons[i]['all_points_y']=list(all_p_y)

                    self.add_image(
                        "Sputum",
                        image_id=a['filename'],  # use file name as a unique image id
                        path=image_path,
                        width=width, height=height,
                        polygons=polygons,
                        class_ids=class_ids)

            def load_mask(self, image_id):
                """Generate instance masks for an image.
                    Returns:
                        masks: A bool array of shape [height, width, instance count] with
                            one mask per instance.
                        class_ids: a 1D array of class IDs of the instance masks.
                """
                # If not a hail dataset image, delegate to parent class.
                image_info = self.image_info[image_id]
                if image_info["source"] != "Sputum":
                    return super(self.__class__, self).load_mask(image_id)
                class_ids = image_info['class_ids']
                # Convert polygons to a bitmap mask of shape
                # [height, width, instance_count]
                info = self.image_info[image_id]
                mask = np.zeros([info["height"], info["width"], len(info["polygons"])],
                                dtype=np.uint8)
                for i, p in enumerate(info["polygons"]):
                    # Get indexes of pixels inside the polygon and set them to 1
                    rr, cc = skimage.draw.polygon(p['all_points_y'], p['all_points_x'])
                    mask[rr, cc, i] = 1

                # Return mask, and array of class IDs of each instance. Since we have
                print("info['class_ids']=", info['class_ids'])
                class_ids = np.array(class_ids, dtype=np.int32)
                return mask, class_ids#[mask.shape[-1]] #np.ones([mask.shape[-1]], dtype=np.int32)#class_ids.astype(np.int32)            


            def image_reference(self, image_id):
                info = self.image_info[image_id]
                if info["source"] == "Sputum":
                    return info["path"]
                else:
                    super(self.__class__, self).image_reference(image_id)


        # Training dataset.
        dataset_train = SputumDataset()
        dataset_train.load_sputum(dataset_path, "train")
        dataset_train.prepare()

        # Validation dataset
        dataset_val = SputumDataset()
        dataset_val.load_sputum(dataset_path, "val")
        dataset_val.prepare()

        # Create model in training mode
        model = modellib.MaskRCNN(mode="training", config=config,
                                model_dir=MODEL_DIR)

        print("Training network heads")
        model.train(dataset_train, dataset_val,
                    learning_rate=config.LEARNING_RATE,
                    epochs=epochs,
                    layers='heads')

        print("Training is Complete.")
        print("Model Saved at :",MODEL_DIR)


    def crop_maskrcnn(self,model_dir, coco_model_path, image_path, image_name, output_path):
        """This function crops the bounding box image based on the maskrcnn model output. Mask RCNN
        algorithm detects the object of interest in the imagine and the shaded part detected is cropped and 
        saved to the output_path.

        Parameters
        ----------

        model_dir : str
            Path to the model directory.
        model_path : str
            Path to the trained model or coco model.
        image_path : str
            Path to the image for which cropping is to be done.
        image_name : str
            Name of the image.
        output_path : str
            Path to the output directory where the image is to be saved.

        Returns
        -------
        Images
            The Predicted part will be cropped and saved in the output directory.

        """
        
        class SputumConfig(Config):
            """Configuration for training on the hail, hand  dataset.
            Derives from the base Config class and overrides some values.
            """
            # Give the configuration a recognizable name
            NAME = "Sputum"

            # We use a GPU with 12GB memory, which can fit two images.
            # Adjust down if you use a smaller GPU.
            IMAGES_PER_GPU = 1

            # Number of classes (including background)
            NUM_CLASSES = 1 + 1  # Background + ridge + valley

            # Number of training steps per epoch
            STEPS_PER_EPOCH = 100

            # Skip detections with < 80% confidence
            DETECTION_MIN_CONFIDENCE = 0.9

        class InferenceConfig(SputumConfig):
            # Set batch size to 1 since we'll be running inference on
            # one image at a time. Batch size = GPU_COUNT * IMAGES_PER_GPU
            GPU_COUNT = 1
            IMAGES_PER_GPU = 1

        session = tf.Session()
        keras.backend.set_session(session)
        configs = InferenceConfig()
        with modellib.MaskRCNN(mode="inference", model_dir=model_dir, config=configs) as models:
            models.load_weights(coco_model_path, by_name=True)
        print('Sputum weight file loaded')

        preprocess_obj = PreprocessImages()
        preprocess_obj.crop_run(image_path,image_name,output_path,models,session)

    def mask_saving(self,model_dir, coco_model_path, image_path, image_name, output_path):
        """The Mask RCNN model when given a image detects the area of interest. This method
        saves that predictions as a image file which can be used for evaluating how good the 
        model is. The Image is saved in the output_path given.

        Parameters
        ----------
        model_dir : str
            Path to the model directory.
        model_path : str
            Path to the trained model or coco model.
        image_path : str
            Path to the image for which cropping is to be done.
        image_name : str
            Name of the image.
        output_path : str
            Path to the output directory where the image is to be saved.

        Returns
        -------
        Images
            The Predicted part will be saved in the output directory.

        """
        class SputumConfig(Config):
            """Configuration for training on the hail, hand  dataset.
            Derives from the base Config class and overrides some values.
            """
            # Give the configuration a recognizable name
            NAME = "Sputum"

            # We use a GPU with 12GB memory, which can fit two images.
            # Adjust down if you use a smaller GPU.
            IMAGES_PER_GPU = 1

            # Number of classes (including background)
            NUM_CLASSES = 1 + 1  # Background + ridge + valley

            # Number of training steps per epoch
            STEPS_PER_EPOCH = 100

            # Skip detections with < 80% confidence
            DETECTION_MIN_CONFIDENCE = 0.9

        class InferenceConfig(SputumConfig):
            # Set batch size to 1 since we'll be running inference on
            # one image at a time. Batch size = GPU_COUNT * IMAGES_PER_GPU
            GPU_COUNT = 1
            IMAGES_PER_GPU = 1

        session = tf.Session()
        keras.backend.set_session(session)
        configs = InferenceConfig()
        with modellib.MaskRCNN(mode="inference", model_dir=model_dir, config=configs) as models:
            models.load_weights(coco_model_path, by_name=True)
        print('Sputum weight file loaded')

        preprocess_obj = Masked_Image()
        preprocess_obj.sputum_mask_segment(image_path,image_name,output_path,models,session)

    def sputum_ml_feature_extract(self, path_to_csv, crop_dir, feature_folder):
        """Based on the cropped images, this method extracts the features from the images. This 
        feature extraction method is for training the Machine Learning model. There is 24 features
        extracted without including the score.

        Parameters
        ----------
        path_to_csv : str
            Path to csv files containing the labels and other attributes.

        crop_dir : str
            Path to the directory where the cropped images are saved.

        feature_folder : str
            Path to the directory where the features are to be saved.

        Returns
        -------
        Parquet file
            A Parquet file will be saved inside the feature folder containing various features.
            The File format will be having a timestamp.

        """


        df=pd.read_csv(path_to_csv)
        result=[]
        for i in range(len(df)):
            s = df['Score'][i]
            image_name=df['image_name'][i]
            img_path=os.path.join(crop_dir,image_name)
            img=cv2.imread(img_path)
            img_resized=cv2.resize(img,(110,70))
            b,g,r=cv2.split(img_resized)
            b_list = []

            for i in range(len(b)):
                for j in range(len(b[i])):
                    b_list.append(b[i][j])
            g_list = []
            for i in range(len(g)):
                for j in range(len(g[i])):
                    g_list.append(g[i][j])
            r_list = []
            for i in range(len(r)):
                for j in range(len(r[i])):
                    g_list.append(r[i][j])

            b_a = np.array(b_list)
            g_a = np.array(g_list)
            r_a = np.array(r_list)

            if len(b_a)!=0:
                b_mean = cv2.mean(b)
                b_max = np.max(b_a)
                b_median = statistics.median(b_a)
                b_10 = np.percentile(b_a, 10)
                b_25 = np.percentile(b_a, 25)
                b_50 = np.percentile(b_a, 50)
                b_75 = np.percentile(b_a, 75)
                b_100 = np.percentile(b_a, 100)
            else:
                b_mean = [0]
                b_max = 0
                b_median = 0
                b_10 = 0
                b_25 = 0
                b_50 = 0
                b_75 = 0
                b_100 = 0
            if len(g_a)!=0:
                g_mean = cv2.mean(g)
                g_median = statistics.median(g_a)
                g_max = np.max(g_a)
                g_10 = np.percentile(g_a, 10)
                g_25 = np.percentile(g_a, 25)
                g_50 = np.percentile(g_a, 50)
                g_75 = np.percentile(g_a, 75)
                g_100 = np.percentile(g_a, 100)
            else:
                g_mean = [0]
                g_median = 0
                g_max = 0
                g_10 = 0
                g_25 = 0
                g_50 = 0
                g_75 = 0
                g_100 = 0
            if len(r_a)!=0:
                r_mean = cv2.mean(r)
                r_max = np.max(r_a)
                r_median = statistics.median(r_a)
                r_10 = np.percentile(r_a, 10)
                r_25 = np.percentile(r_a, 25)
                r_50 = np.percentile(r_a, 50)
                r_75 = np.percentile(r_a, 75)
                r_100 = np.percentile(r_a, 100)
            else:
                r_mean = [0]
                r_max = 0
                r_median = 0
                r_10 = 0
                r_25 = 0
                r_50 = 0
                r_75 = 0
                r_100 = 0

            result.append({'img':image_name,'B_Mean':b_mean[0],'G_Mean':g_mean[0],'R_Mean':r_mean[0],
                        'B_Max':b_max,'G_Max':g_max,'R_Max':r_max,
                        'B_Median':b_median,'G_Median':g_median,'R_Median':r_median,
                        'B_10':b_10,'B_25':b_25,'B_50':b_50,'B_75':b_75,'B_100':b_100,
                        'G_10': g_10, 'G_25': g_25, 'G_50': g_50, 'G_75': g_75, 'G_100': g_100,
                        'R_10': r_10, 'R_25': r_25, 'R_50': r_50, 'R_75': r_75, 'R_100': r_100,'Score':s})

        pd.DataFrame(result).to_parquet(os.path.join(feature_folder,'sputum_{0}_feature.parquet'.format(time.time())))



    def sputum_ml_train(self,feature_folder,algorithm, model_save_dir):
        """Based on the features extracted the Machine Learning model is trained. The 
        best parameters are selected and the model is saved as a pickle file in
        the model_save_dir.

        Parameters
        ----------
        feature_folder : str
            Path to the directory where the feature files are saved as a parquet file.
        
        algorithm : str,options=['RandomForest','KNN']
            The algorithm to be used for training the model. Currently supports Random Forest and 
            K Nearest Neighbour. The Best Parameters for the algorithms are found using RandomizedSearchCV
            and the model is saved in the model_save_dir, with the time stamp format.

        model_save_dir : str
            Path to the directory where the machine learning model is to be saved.

        Returns
        -------
        Machine Learning Model
            Machine Learning model will be saved inside the model_save_dir with the time stamp format.
            Prints the Accuracy and Confusion Matrix of the model prediction based on 10 percent of test data.
        """
        feature_dir=feature_folder
        file_name=glob.glob(feature_dir+'/*.parquet')
        
        data=pd.DataFrame()
        for file in file_name:
            data1=pd.read_parquet(file)
            data=pd.concat([data,data1])

        X=data.drop(['img','Score'],axis=1)
        X=X/255.0
        y=data['Score']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=143,stratify=y)
        if algorithm=='RandomForest':
            rf = RandomForestClassifier()
            param_grid = {
            'criterion':["gini", "entropy"],
            'max_depth': [7, 10, 13,20,30],
            'max_features': [4, 5, 6,8,10],
            'min_samples_leaf': [3,4,5, 7, 9],
            'min_samples_split': [4, 6, 8,10,12],
            'n_estimators': [100,200,300, 400, 500]}
            clf = RandomizedSearchCV(estimator=rf,
                                    param_distributions=param_grid,
                                    scoring='accuracy',
                                    verbose=1)
            clf.fit(X_train,y_train)
            rf_model=clf.best_estimator_
            y_pred=rf_model.predict(X_test)
            print("Accuracy: ",accuracy_score(y_test,y_pred))
            print("Confusion Matrix:\n",confusion_matrix(y_test,y_pred))
            joblib.dump(clf, os.path.join(model_save_dir,'sputum_rf_model_{}.pkl'.format(time.time())))

        elif algorithm=='KNN':
            knn = KNeighborsClassifier(n_neighbors=8) 
            param_grid = {'weights':['uniform', 'distance'],
                        'algorithm':['auto', 'ball_tree', 'kd_tree', 'brute'],
                        'metric':['euclidean','minkowski','manhattan'],
                        'p':[1,2,3,4],
                        'leaf_size':[1,10,20,30,40,50,60,70,80,90,100]}
            clf = RandomizedSearchCV(estimator=knn,
                                    param_distributions=param_grid,
                                    scoring='accuracy',
                                    verbose=1)
            clf.fit(X_train,y_train)
            knn_model=clf.best_estimator_
            y_pred=knn_model.predict(X_test)
            print("Accuracy: ",accuracy_score(y_test,y_pred))
            print("Confusion Matrix:\n",confusion_matrix(y_test,y_pred))
            joblib.dump(clf, os.path.join(model_save_dir,'sputum_knn_model.pkl'.format(time.time())))

        





