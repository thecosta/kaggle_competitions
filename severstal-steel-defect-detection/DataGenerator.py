from keras.preprocessing.image import ImageDataGenerator


class DataGenerator():


    def __init__(self, rotation_range=0.2, width_shift_range=0.05,
                 height_shift_range=0.05, shear_range=0.05, zoom_range=0.05,
                 horizontal_flip=True, fill_mode='nearest'):

        self.rotation_range = rotation_range
        self.width_shift_range = width_shift_range
        self.height_shift_range = height_shift_range
        self.shear_range = shear_range
        self.zoom_range = zoom_range
        self.horizontal_flip = horizontal_flip
        self.fill_mode = fill_mode

        self.data_aug = dict(rotation_range = self.rotation_range,
            width_shift_range = self.width_shift_range,
            height_shift_range = self.height_shift_range,
            shear_range = self.shear_range,
            zoom_range = self.zoom_range,
            horizontal_flip = self.horizontal_flip,
            fill_mode = self.fill_mode)

        
    def train_gen(self):

        image_datagen = ImageDataGenerator(**self.data_aug)
        maks_datagen = ImageDataGenerator(**self.data_aug)
        
    
    
