# Deep Fake Detection

This project implements a deep learning classifier using the Meso4 architecture to detect fake (manipulated) or real images.

## Overview

The Meso4 model is a convolutional neural network (CNN) designed for binary image classification, specifically trained to distinguish between authentic and manipulated images. This implementation leverages the Keras framework and a pre-trained model to classify images.

## Features

- Implementation of Meso4 architecture for image classification
- Loading of pre-trained models for immediate use
- Image preprocessing using Keras ImageDataGenerator
- Binary classification of images as "real" or "fake"

## Requirements

To install the necessary dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone the repository
2. Install dependencies
3. Run the script:

```bash
python deepfake.py
```

The script will:
- Download the pre-trained Meso4 model
- Download sample test images (fake and real)
- Process the images and provide predictions

## Applications

This code can be used as a starting point for:
- Deepfake detection
- Image forensics
- Image tampering analysis
- Image authenticity verification

## Model Architecture

The Meso4 architecture consists of:
- Multiple convolutional layers with batch normalization
- MaxPooling layers for feature reduction
- Dropout layers to prevent overfitting
- Dense layers for classification

## License

[Specify license information here]

## Acknowledgements

- Based on MesoNet architecture for deepfake detection
- Test images and pre-trained weights from Machine Learning for Cybersecurity Cookbook
