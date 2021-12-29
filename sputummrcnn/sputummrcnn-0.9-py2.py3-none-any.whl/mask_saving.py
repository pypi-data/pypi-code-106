import random
import numpy as np
import os
np.random.seed(1)
random.seed(1)
import skimage.io
import cv2
import colorsys
from PIL import Image, ImageDraw

from .mrcnn import model as modellib, utils

class Masked_Image:
    def color_map(self, N=256, normalized=False):
        def bitget(byteval, idx):
            return ((byteval & (1 << idx)) != 0)

        dtype = 'float32' if normalized else 'uint8'
        cmap = np.zeros((N, 3), dtype=dtype)
        for i in range(N):
            r = g = b = 0
            c = i
            for j in range(8):
                r = r | (bitget(c, 0) << 7 - j)
                g = g | (bitget(c, 1) << 7 - j)
                b = b | (bitget(c, 2) << 7 - j)
                c = c >> 3

            cmap[i] = np.array([r, g, b])

        cmap = cmap / 255 if normalized else cmap
        return cmap

    def random_colors(self, N, bright=True):
        """
        Generate random colors.
        To get visually distinct colors, generate them in HSV space then
        convert to RGB.
        """
        brightness = 1.0 if bright else 0.7
        hsv = [(i / N, 1, brightness) for i in range(N)]
        colors = list(map(lambda c: colorsys.hsv_to_rgb(*c), hsv))
        random.shuffle(colors)
        return colors

    def apply_mask(self, image, mask, color, alpha=0.5):
        """Apply the given mask to the image.
        """
        for c in range(3):
            image[:, :, c] = np.where(mask == 1,
                                      image[:, :, c] * (1 - alpha) + alpha * color[c] * 255, image[:, :, c])
        return image

    def save_image(self, image, image_name, boxes, masks, class_ids, scores, class_names, filter_classs_names=None,
                   scores_thresh=0.1, save_dir=None, mode=0):
        """
            image: image array
            image_name: image name
            boxes: [num_instance, (y1, x1, y2, x2, class_id)] in image coordinates.
            masks: [num_instances, height, width]
            class_ids: [num_instances]
            scores: confidence scores for each box
            class_names: list of class names of the dataset
            filter_classs_names: (optional) list of class names we want to draw
            scores_thresh: (optional) threshold of confidence scores
            save_dir: (optional) the path to store image
            mode: (optional) select the result which you want
                    mode = 0 , save image with bbox,class_name,score and mask;
                    mode = 1 , save image with bbox,class_name and score;
                    mode = 2 , save image with class_name,score and mask;
                    mode = 3 , save mask with black background;
        """
        mode_list = [0, 1, 2, 3]
        assert mode in mode_list, "mode's value should in mode_list %s" % str(mode_list)

        if save_dir is None:
            save_dir = os.path.join(os.getcwd(), "output")
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)

        useful_mask_indices = []

        N = boxes.shape[0]
        if not N:
            print("\n* No instances in image %s to draw * \n" % (image_name))
            return
        else:
            assert boxes.shape[0] == masks.shape[-1] == class_ids.shape[0]

        for i in range(N):
            # filter
            class_id = class_ids[i]
            score = scores[i] if scores is not None else None
            if score is None or score < scores_thresh:
                continue

            label = class_names[class_id]
            if (filter_classs_names is not None) and (label not in filter_classs_names):
                continue

            if not np.any(boxes[i]):
                # Skip this instance. Has no bbox. Likely lost in image cropping.
                continue

            useful_mask_indices.append(i)

        if len(useful_mask_indices) == 0:
            print("\n* No instances in image %s to draw * \n" % (image_name))
            return

        colors = self.random_colors(len(useful_mask_indices))

        if mode != 3:
            masked_image = image.astype(np.uint8).copy()
        else:
            masked_image = np.zeros(image.shape).astype(np.uint8)

        if mode != 1:
            for index, value in enumerate(useful_mask_indices):
                masked_image = self.apply_mask(masked_image, masks[:, :, value], colors[index])

        masked_image = Image.fromarray(masked_image)

        if mode == 3:
            masked_image.save(os.path.join(save_dir, '%s.jpg' % (image_name)))
            return

        draw = ImageDraw.Draw(masked_image)
        colors = np.array(colors).astype(int) * 255

        for index, value in enumerate(useful_mask_indices):
            class_id = class_ids[value]
            score = scores[value]
            label = class_names[class_id]

            y1, x1, y2, x2 = boxes[value]
            if mode != 2:
                color = tuple(colors[index])
                draw.rectangle((x1, y1, x2, y2), outline=color)

            # # Label
            # font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
            # draw.text((x1, y1), "%s %f" % (label, score), (255, 255, 255), font)

        masked_image.save(os.path.join(save_dir,(image_name)))
    
    def sputum_mask_segment(self, image_path,image_name,output_path,models,session):
        image = skimage.io.imread(image_path)
        class_names = ['BG', 'Sputum']
        with session.as_default():
            with session.graph.as_default():
                results = models.detect([image], verbose=1)             
                r = results[0]
                boxes = r['rois']  ## bounding box coordinates
                if len(boxes) != 0:
                    self.save_image(image, image_name=image_name, boxes=r['rois'], masks=r['masks'],
                                class_ids=r['class_ids'], scores=r['scores'], class_names=class_names,
                                save_dir=output_path)
                else:
                    cv2.imwrite(os.path.join(output_path,image_name),image)


