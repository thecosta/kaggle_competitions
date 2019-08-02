import glob
import numpy as np
from PIL import Image
from keras.preprocessing.image import ImageDataGenerator
from tqdm import tqdm



train_datagen = ImageDataGenerator(rescale=1.0/255)
test_datagen = ImageDataGenerator(rescale=1.0/255)

train_generator = train_datagen.flow_from_directory(
    '/Volumes/Brome/kaggle/data/all-dogs/',
    target_size=(64, 64),
    batch_size=32,
    save_to_dir='/Volumes/Brome/kaggle/data/all-dogs-gen/',
    save_prefix='aug',
    save_format='png',
    class_mode=None)

for i in tqdm(train_generator, total=20579):
    continue
