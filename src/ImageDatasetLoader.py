import numpy as np
import cv2
import os


class ImageDatasetLoader:
    def __init__(self, preprocessor=None):
        self.preprocessor = preprocessor

    def load(self, imagePaths):
        data = []

        for (i, imagePath) in imagePaths:
            image = cv2.imread(imagePath)
            if self.preprocessor is not None:
                image = self.preprocessor.preprocess()
            data.append(image)

        return np.array(data)
