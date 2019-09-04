import os
from tqdm import tqdm
from PIL import Image, ImageDraw


class GenerateMasks():


    def __init__(self, csv_path, images_path, save_path):
        self.csv_path = csv_path
        self.images_path = images_path
        self.save_path = save_path
        
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)
            
        self.__read_csv()
    

    def __read_csv(self):

        
        with open(self.csv_path, 'r') as f:
            for idx, line in enumerate(tqdm(f, total=50273)):
                # skip header
                if not idx:
                    continue

                line = line[:-1]

                # skip non-classID
                if not len(line.split(',')[1]):
                    continue
                
                line = line.split(',')
                image = line[0][:-2]
                class_id = int(line[0][-1])
        
                if class_id == 1:
                    color=(0, 255, 68)
                if class_id == 2:
                    color=(0, 191, 255)
                if class_id == 3:
                    color=(255, 0, 234)
                if class_id == 4:
                    color=(255, 0, 0)

                encoded_pixels = line[1].split(' ')
                
                image_path = os.path.join(self.images_path, image)
                im = Image.open(image_path)
                
                mask = Image.new(size=im.size, mode='RGB')
                draw = ImageDraw.Draw(mask)

                for idx, encoded_pixel in enumerate(encoded_pixels):
                    if idx % 2 == 0:
                        start = int(encoded_pixel)
                        end = int(encoded_pixels[idx+1])-1
                        prev_start = start
                        for i in range(end):
                            end = start + i
                            y_start = start % im.size[1]
                            x_start = start / im.size[1]
                            y_end = end % im.size[1]
                            x_end = end / im.size[1]
                            #print(f'{start}, {end}')
                            #print(f'({x_start}, {y_start})')
                            draw.line([(x_start, y_start), (x_end, y_end)], fill=color)
                            prev_start = end
                
                save_image = os.path.join(self.save_path, image)
                mask.save(save_image)
                
                
                

if __name__ == '__main__':
    csv_path = '/Volumes/Brome/kaggle_data/severstal-steel-detection/train.csv'
    images_path = '/Volumes/Brome/kaggle_data/severstal-steel-detection/train_images'
    save_path = '/Volumes/Brome/kaggle_data/severstal-steel-detection/train_images_masks'
    GenerateMasks(csv_path, images_path, save_path)
        
