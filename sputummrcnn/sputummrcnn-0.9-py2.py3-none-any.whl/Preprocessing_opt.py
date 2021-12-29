import os
import cv2 as cv
import threading
import numpy as np
class PreprocessImages():
    def crop_run(self,impath,imname,savedir,model,session):
        # print('impath',impath,imname)
        img = cv.imread(impath)
        img = cv.resize(img,(400,600))
        print(img.shape)
        with session.as_default():
            with session.graph.as_default():
                results = model.detect([img], verbose=0)
                r = results[0]
                if len(r['scores']) !=0:
                    index = np.argmax(r['scores'])
                    box = r['rois'][index]
                    y = box[0]
                    x = box[1]
                    y1 = box[2]
                    x1 = box[3]
                    mask = r['masks'][:, :, index]
                    temp = cv.imread(impath)
                    temp = cv.resize(temp, (400, 600))
                    for j in range(temp.shape[2]):
                        temp[:, :, j] = temp[:, :, j] * mask
                    temp = temp[y:y1, x:x1]
                    save_path = os.path.join(savedir,imname)
                    cv.imwrite(save_path,temp)


        return True
