This project is an implementation of a deep learning classifier using the Meso4 architecture to
detect fake or real images. The Meso4 model is designed for image classification and is trained
to distinguish between authentic and manipulated images. The project report demonstrates the
use of the Meso4 architecture for image classification, particularly in the context of
distinguishing real images from manipulated (fake) ones. It showcases how to load a pre-trained
model, preprocess images, and make predictions using the trained classifier. This code can be
used as a starting point for image authenticity detection in various applications, such as
deepfake detection or image forensics. This project implements a deep learning classifier,
Meso4, to detect fake or real images. Meso4 is a convolutional neural network (CNN) designed
for binary image classification. The code utilizes Keras and loads a pre-trained Meso4 model
with learned weights. Images are preprocessed using the Keras `ImageDataGenerator` and are
then classified as "real" or "fake." The predicted labels are based on the model's output, where
a threshold determines the classification. This code is useful for image authenticity verification,
making it relevant in applications like deepfake detection, image forensics, and image
tampering analysis. It offers a practical framework for leveraging pre-trained models to assess
image integrity, aiding in the identification of potentially manipulated content.
