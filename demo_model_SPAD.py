"""
This code shows the multilayer perceptron model and the implementation of the 
algorithm for "Spatial images from temporal data". 

paper link:  https://www.osapublishing.org/optica/abstract.cfm?uri=optica-7-8-900

Authors: A. Turpin, G. Musarra, Francesco Tonolini, Ashley Lyons, Ilya Starshinov, 
Federica Villa, Francesco Fioranelli, Roderick Murray-Smith, Daniele Faccio. 
Extreme Light Group, University of Glasgow
Date: 2020.09.15
"""
# Load all the required libraries 
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.utils import np_utils
import keras
import time
import scipy.io as sio
import h5py
import skimage
from matplotlib.pyplot import figure
import pylab as pl
from IPython import display
import tensorflow as tf


# Load the data with the histograms that are fed into the model and the ground
# truth 3D images for comparison. 
# Number of histograms - 3D camera pairs: 100 
# SPAD histogram length = 1800
# 3D camera resolution = 64 x 64

#folder = "here_goes_your_working_directory"
folder = "C:/Users/aturpin/Dropbox/Glasgow_2018/Papers/LiDAR/Github/raw_data/uploaded_github/"

mat_contents = sio.loadmat(folder+'histograms_SPAD.mat') 
histograms = mat_contents['people'] # This is just an example, can load other data

mat_contents = sio.loadmat(folder+'ToF_camera_SPAD.mat') 
camera_depth = mat_contents['people'] # This is just an example, can load other data

#%% Now we create the MLP. We trained it with 100 epochs, a batch size of 150 and with shuffling the data.
# Note: Before feeding the ToF camera data into the algorithm for trainig, it is required to reshape it to 100x4096

if 'model' in locals(): del model
keras.backend.clear_session()

with tf.device("/device:GPU:0"): # The model is prepared to work on a GPU for faster training
    model = Sequential()
                input_dim = 1800, 
                kernel_initializer='normal'
                ,activation='tanh'
               ))           
    model.add(Dense((512),activation='tanh'))
    model.add(Dense((256),activation='tanh'))
    model.add(Dense((4096)))
    model.compile(loss='categorical_crossentropy', #'categorical_crossentropy',#
              optimizer='adam', 
              metrics=['accuracy'])
    


model.summary()    
    
#%% After the model is trained, we can directly load the weights and test it

model = load_model('weights_people.h5') # We provide as an example the weights of a model already trained on people

camera_depth_predicted = model.predict(histograms) 
camera_depth_predicted = np.reshape(camera_depth_predicted,(100,64,64)) # This reshape is required to transform the predicted data (1D) into an image (2D)
camera_depth_predicted = camera_depth_predicted/camera_depth_predicted.max()

# Plot the results dynamically 
fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

plt.ion()

fig.show()
fig.canvas.draw()

for i in range(nval):
    ax1.clear()
   
    plt.subplot(121)
    plt.imshow(camera_depth[:,:,i],vmin=0, vmax=1)
    
    ax2.clear()
    plt.subplot(122)
    plt.imshow(camera_depth_predicted[i,:,:],vmin=0, vmax=1)

    
    display.display(pl.gcf())
    display.clear_output(wait=True)
    time.sleep(0.01)







