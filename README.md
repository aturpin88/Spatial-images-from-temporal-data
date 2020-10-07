# Spatial images from temporal data: code details

Python implementation of the article: Spatial images from temporal data. We present our multiplayer perceptron (MLP) model, we give pre-trained weights (se below for download link), test data, and code to implement the model. 

## Citation 

You can find the whole paper in [Optica](https://www.osapublishing.org/optica/abstract.cfm?uri=optica-7-8-900). 

Alex Turpin, Gabriella Musarra, Valentin Kapitany, Francesco Tonolini, Ashley Lyons, Ilya Starshynov, Federica Villa, Enrico Conca, Francesco Fioranelli, Roderick Murray-Smith, and Daniele Faccio, "Spatial images from temporal data," Optica 7, 900-905 (2020)

## Data and documents descriptions
- [histograms_SPAD.mat](), [histograms_RADAR.mat](), [ToF_camera_SPAD.mat](), and [ToF_camera_RADAR.mat]() are the histograms and 3D images experimentally recorded using the single-photon avalanche diode (SPAD) sensor, the RADAR, and the time-of-flight (ToF) camera. 
This data was not used during the training of the ANN. [ToF_recovered_SPAD.mat]() and [ToF_recovered_RADAR.mat]() are the corresponding 3D images retrieved with our algorithm. 
- [demo_model.py]() shows our ANN model and contains the required instructions to test it on the above-mentioned data. 
- The pre-trained weights for the algorithm being trained with two people and the SPAD sensor can be downloaded from the following link: [weights](https://www.dropbox.com/s/opmd3kxlip7inp3/weights_people.h5?dl=0) 

## How to use the code
The code [demo_model.py]() will assist you to test our recovery algorithm with the pre-trained [weights](https://www.dropbox.com/sh/ll9jr793g5s1ktl/AACLmUSD4r6eYevG7Ej1YRIRa?dl=0) and the provided recorded data.

## Requirements
[python 3.6](https://www.python.org/downloads/release/python-360/) or higher

[keras 2.1.2](http://faroit.com/keras-docs/2.1.2/) or higher

[tensorflow 1.14.0](https://www.tensorflow.org/install) or higher

[numpy](https://numpy.org)

[h5py](https://www.h5py.org/)

[matplotlib](https://matplotlib.org/)

## License
[MIT](https://choosealicense.com/licenses/mit/)
