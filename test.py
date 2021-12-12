# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 15:59:15 2021

@author: Shaunak04, Nikhil
"""
import os
import sys

import tensorflow as tf
from tensorflow.keras import layers
import pandas as pd
import numpy as np
import cv2
import matplotlib.pyplot as plt
import data_func

BATCH_SIZE = 6
HEIGHT = 256
WIDTH = 256

path = "val/indoors"

filelist = []

for root, dirs, files in os.walk(path):
    for file in files:
        filelist.append(os.path.join(root, file))

filelist.sort()
data = {
    "image": [x for x in filelist if x.endswith(".png")],
    "depth": [x for x in filelist if x.endswith("_depth.npy")],
    "mask": [x for x in filelist if x.endswith("_depth_mask.npy")],
}
df = pd.DataFrame(data)


filelist2 = []

test_path = "val/test"

for root, dirs, files in os.walk(test_path):
    for file in files:
        filelist2.append(os.path.join(root, file))

filelist2.sort()
data2 = {
    "image": [x for x in filelist2 if x.endswith(".png")],
    "depth": [x for x in filelist2 if x.endswith("_depth.npy")],
    "mask": [x for x in filelist2 if x.endswith("_depth_mask.npy")],
}

test_df = pd.DataFrame(data2)


new_model = tf.keras.models.load_model('model')
new_model.summary()

better_model = tf.keras.models.load_model('collab_model')
better_model.summary()

def visualize_depth_map(samples, test=False, model=None):
    input, target = samples
    cmap = plt.cm.jet
    cmap.set_bad(color="black")

    if test:
        pred = model.predict(input)
        fig, ax = plt.subplots(2, 3, figsize=(50, 50))
        print("SDKHJAD")
        for i in range(2):
            ax[i, 0].imshow((input[i].squeeze()))
            ax[i, 1].imshow((target[i].squeeze()), cmap=cmap)
            ax[i, 2].imshow((pred[i].squeeze()), cmap=cmap)

    else:
        fig, ax = plt.subplots(6, 2, figsize=(50, 50))
        print("SDKHJAD12313")
        for i in range(6):
            ax[i, 0].imshow((input[i].squeeze()))
            ax[i, 1].imshow((target[i].squeeze()), cmap=cmap)
            
def visualize_single_image(samples, test=False, model=None):
    input, target = samples
    cmap = plt.cm.jet
    cmap.set_bad(color="black")

    pred = model.predict(input)
        #fig, ax = plt.subplots(6, 3, figsize=(50, 50))
        #for i in range(6):
            #ax[i, 0].imshow((input[i].squeeze()))
            #ax[i, 1].imshow((target[i].squeeze()), cmap=cmap)
            #ax[i, 2].imshow((pred[i].squeeze()), cmap=cmap)
        
    for i in range(len(input)):
        plt.imshow(input[i].squeeze(), cmap=cmap)
        plt.show()
        plt.imshow(pred[i].squeeze(), cmap=cmap)
        plt.show()

    # else:
    #     fig, ax = plt.subplots(6, 2, figsize=(50, 50))
    #     for i in range(6):
    #         ax[i, 0].imshow((input[i].squeeze()))
    #         ax[i, 1].imshow((target[i].squeeze()), cmap=cmap)            

#validation_loader = data_func.DataGenerator(
#    data=df[260:].reset_index(drop="true"), batch_size=BATCH_SIZE, dim=(HEIGHT, WIDTH)
#)

visualize_samples = next(
    iter(data_func.DataGenerator(data=test_df, batch_size=6, dim=(HEIGHT, WIDTH)))
)

visualize_single_image(visualize_samples,model=new_model)
visualize_single_image(visualize_samples,model=better_model)

