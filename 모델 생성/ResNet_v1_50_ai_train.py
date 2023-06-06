from ResNet_ops_1 import *
import shutil


#train_path = './Data/train/병명별/결막염' #경로 마지막에 반드시 '/'를 기입해야합니다.
model_name = 'resnet_v1_50'

epoch = 300
if __name__ == '__main__':
    disTable= ['유루증']
    save_foler = f'./model_saved/병명별/resnet_v1_50_300'
    for dis in disTable :
        train_path = f'./Data/train/병명별/{dis}'
        val_path = f'./Data/val/병명별/{dis}'
        fine_tunning = Fine_tunning(train_path=train_path,
                                    model_name=model_name,
                                    val_path = val_path, 
                                    epoch=epoch)
        history = fine_tunning.training()
        fine_tunning.save_accuracy(history)

        if not os.path.exists(f'{save_foler}/{dis}'):
            os.makedirs(f'{save_foler}/{dis}')
        fileList = os.listdir(save_foler)
        for file in fileList :
            if os.path.isdir(f'{save_foler}/{file}') : continue
            shutil.move(f'{save_foler}/{file}', f'{save_foler}/{dis}')
        