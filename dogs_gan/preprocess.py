import glob
import numpy as np
from PIL import Image
from keras.preprocessing.image import ImageDataGenerator
from tqdm import tqdm



path_in = '/Users/bruno/Documents/git/burncam/data/images/'
path_out = '/Users/bruno/Documents/git/burncam/data/images_gen/'
train_datagen = ImageDataGenerator(rescale=1.0/255)
test_datagen = ImageDataGenerator(rescale=1.0/255)

train_generator = train_datagen.flow_from_directory(
    path_in,
    target_size=(512, 512),
    batch_size=221,
    save_to_dir=path_out,
    save_prefix='aug',
    save_format='png',
    class_mode=None)

for i in train_generator:
    break
