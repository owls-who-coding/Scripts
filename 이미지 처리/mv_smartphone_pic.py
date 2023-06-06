import os
import time
import json
import shutil

ROOT_PATH = 'D:/새 폴더'
origin_path = './원천'
#sub_path = './Data'
sub_path='./원본데이터'
disease_list = os.listdir(f'{origin_path}/train')

get_tag_list = ["스마트폰", "스마트 폰", "일반카메라", "일반 카메라"]
get_tag_list2 = ["검안경", "검 안경"]

def copy_img(src_url, des_url) :
    #print(src_url, "  ", des_url)
    if os.path.exists(f'{src_url}.png'):
        shutil.copy(f'{src_url}.png', f'{des_url}.png')
    elif os.path.exists(f'{src_url}.jpg'):
        shutil.copy(f'{src_url}.jpg', f'{des_url}.jpg')
    #time.sleep(10)

#trian Data
def train_data() :
    for dis_name in disease_list :
        if not os.path.exists(f'{sub_path}/train/{dis_name}'):
            os.makedirs(f'{sub_path}/train/{dis_name}')
        level_list = os.listdir(f'{origin_path}/train/{dis_name}')
        for level_name in level_list :
            if not os.path.exists(f'{sub_path}/train/{dis_name}/{level_name}'):
                os.makedirs(f'{sub_path}/train/{dis_name}/{level_name}')
            org_path = f'{origin_path}/train/{dis_name}/{level_name}'
            file_ext = '.json'
            file_list = [_ for _ in os.listdir(org_path) if _.endswith(file_ext)]
            save_path = f'{sub_path}/train/{dis_name}/{level_name}'

            for file_name in file_list :
                with open(f'{org_path}/{file_name}', 'r', encoding='UTF-8') as f :
                    #print(file_name,)
                    #print(f)
                    data = json.load(f)
                    fn = file_name.split('.')[0]
                    if data["images"]["meta"]["device"] in get_tag_list :
                        print(data["images"]["meta"]["device"])
                        copy_img(f'{org_path}/{fn}', f'{save_path}/{fn}')



#validation Data
def validation_data():
    for dis_name in disease_list :
        if not os.path.exists(f'{sub_path}/val/{dis_name}'):
            os.makedirs(f'{sub_path}/val/{dis_name}')
        level_list = os.listdir(f'{origin_path}/val/{dis_name}')
        for level_name in level_list :
            if not os.path.exists(f'{sub_path}/val/{dis_name}/{level_name}'):
                os.makedirs(f'{sub_path}/val/{dis_name}/{level_name}')
            org_path = f'{origin_path}/val/{dis_name}/{level_name}'
            file_ext = '.json'
            file_list = [_ for _ in os.listdir(org_path) if _.endswith(file_ext)]
            save_path = f'{sub_path}/val/{dis_name}/{level_name}'

            for file_name in file_list :
                with open(f'{org_path}/{file_name}', 'r', encoding='UTF-8') as f :
                    #print(file_name,)
                    #print(f)
                    data = json.load(f)
                    fn = file_name.split('.')[0]
                    if data["images"]["meta"]["device"] in get_tag_list :
                        print(data["images"]["meta"]["device"])
                        copy_img(f'{org_path}/{fn}', f'{save_path}/{fn}')
    
if __name__ == "__main__" :
    #train_data()
    validation_data()

    