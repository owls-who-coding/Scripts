import os
import shutil
import PIL
from PIL import Image
import numpy as np

ROOT_PATH = 'C:/Users/joonh/Desktop/project'

IMG_PATH = 'images'

img_path = f'{ROOT_PATH}/{IMG_PATH}'
img_list = os.listdir(img_path)

if not os.path.exists(f'{ROOT_PATH}/img_aug') :
    os.mkdir(f'{ROOT_PATH}/img_aug')

#print(img_list)
for img_file in img_list :
    print(img_file)
    image = Image.open(f'{img_path}/{img_file}')
    try :
        if image.mode in ("RGBA"):
            iamge = image.convert("RGB")
        img_name = img_file.split('.jpg')[0]
        print(img_name)
        #회전
        resize_image = image.resize((480,480))
        if not os.path.exists(f'{ROOT_PATH}/img_aug/{img_name}_480.jpg') :
                resize_image.save(f'{ROOT_PATH}/img_aug/{img_name}_480.jpg')
        for r in range(0, 360, 90) : 
            if r == 180: 
                continue
            rotated_image = image.rotate(r)
            # rotated_image_array = np.array(rotated_image)
            # rotated_image = Image.fromarray(rotated_image_array)
            if not os.path.exists(f'{ROOT_PATH}/img_aug/{img_name}_{r}.jpg') :
                rotated_image.save(f'{ROOT_PATH}/img_aug/{img_name}_{r}.jpg')
    except:
         print("실패")
         pass
    

        
    #색 바꾸기

    #crop

    #