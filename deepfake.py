import warnings
warnings.filterwarnings('ignore')
from keras.models import Model as KerasModel
from keras.layers import Input, Dense,Flatten, Conv2D, MaxPooling2D, BatchNormalization, Dropout, Reshape, Concatenate, LeakyReLU
from keras.optimizers import Adam
import os
import urllib.request

IMGWIDTH = 256
class Classifier:
    def __init__(self):
        self.model = 0

    def predict(self, x):
        return self.model.predict(x)

    def fit(self, x, y):
        return self.model.train_on_batch(x, y)

    def get_accuracy(self, x, y):
        return self.model.test_on_batch(x, y)

    def load(self, path):
        self.model.load_weights(path)

class Meso4(Classifier):
    def __init__(self, learning_rate=0.001):
        self.model = self.init_model()
        optimizer = Adam(lr = learning_rate)
        self.model.compile(optimizer = optimizer, loss='mean_squared_error', metrics=['accuracy'])

    def init_model(self):
        x = Input(shape=(IMGWIDTH, IMGWIDTH, 3))

        x1 = Conv2D(8, (3,3), padding='same', activation='relu')(x)
        x1 = BatchNormalization()(x1)
        x1 = MaxPooling2D(pool_size=(2,2), padding='same')(x1)

        x2 = Conv2D(8,(5,5), padding='same', activation='relu')(x1)
        x2 = BatchNormalization()(x2)
        x2 = MaxPooling2D(pool_size=(2,2), padding='same')(x2)

        x3 = Conv2D(16, (5,5), padding='same', activation='relu')(x2)
        x3 = BatchNormalization()(x3)
        x3 = MaxPooling2D(pool_size=(2,2), padding='same')(x3)

        x4 = Conv2D(16,(5,5), padding='same', activation='relu')(x3)
        x4 = BatchNormalization()(x4)
        x4 = MaxPooling2D(pool_size=(4,4), padding='same')(x4)

        y = Flatten()(x4)
        y = Dropout(0.5)(y)
        y = Dense(16)(y)
        y = LeakyReLU(alpha=0.1)(y)
        y = Dropout(0.5)(y)
        y = Dense(1, activation='sigmoid')(y)

        return KerasModel(inputs=x, outputs=y)
      
# Download files using urllib instead of !wget
urls = [
    ("https://github.com/PacktPublishing/Machine-Learning-for-Cybersecurity-Cookbook/raw/master/Chapter04/Deepfake%20Recognition/mesonet_weights/Meso4_DF", "Meso4_DF"),
    ("https://github.com/PacktPublishing/Machine-Learning-for-Cybersecurity-Cookbook/raw/master/Chapter04/Deepfake%20Recognition/mesonet_test_images/df00204.jpg", "df1.jpg"),
    ("https://github.com/PacktPublishing/Machine-Learning-for-Cybersecurity-Cookbook/raw/master/Chapter04/Deepfake%20Recognition/mesonet_test_images/real00240.jpg", "real.jpg")
]

for url, filename in urls:
    print(f"Downloading {filename}...")
    urllib.request.urlretrieve(url, filename)

# Create test_images directory if it doesn't exist
if not os.path.exists("test_images"):
    os.mkdir("test_images")

# Move downloaded images to test_images directory
for filename in ["df1.jpg", "real.jpg"]:
    os.rename(filename, os.path.join("test_images", filename))

from keras.preprocessing.image import ImageDataGenerator
MesoNet_classifier= Meso4()
MesoNet_classifier.load("Meso4_DF")
imagedata_gen = ImageDataGenerator(rescale=1.0/255)
datagen = imagedata_gen.flow_from_directory("./", classes=["test_images"])
num_to_label = {1:"real", 0:"fake"}
X, y = datagen.next()
prob_predictions = MesoNet_classifier.predict(X)
p = [num_to_label[round(x[0])] for x in prob_predictions]
print(p)
file_names = datagen.filenames
file_names
