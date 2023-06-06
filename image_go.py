import os
import shutil

ROOT_PATH = "./Data/eyesData"
TRAIN_LABEL_DATA_PATH = "./Data/eyesData/train_labelling"
VAL_LABEL_DATA_PATH = "./Data/eyesData/valid_labelling"
TRAIN = 'train'
VAL = "valid"

def copyImg(path, type) :
    file_list = os.listdir(path)
    label_list = [_ for _ in file_list if _.endswith('.txt')]
    print(label_list)
    
    for label_path in label_list :
        if label_path == 'classes.txt' : 
            shutil.copy(f'{path}/{label_path}',f"{ROOT_PATH}/labels/{type}/{label_path}")
            continue
        
        #라벨 파일 복사
        shutil.copy(f'{path}/{label_path}',f"{ROOT_PATH}/labels/{type}/{label_path}")

        #이미지 파일 복사
        try :
            img_name = label_path.split('.txt')[0] + '.jpg'
            #print(img_name)
            shutil.copy(f'{path}/{img_name}',f"{ROOT_PATH}/images/{type}/{img_name}")
        except :
            img_name = label_path.split('.txt')[0] + '.png'
            #print(img_name)
            shutil.copy(f'{path}/{img_name}',f"{ROOT_PATH}/images/{type}/{img_name}")
        
        


copyImg(TRAIN_LABEL_DATA_PATH, type = TRAIN)
copyImg(VAL_LABEL_DATA_PATH, type = VAL)
