import os
import shutil

# nuScenes full v1.0 데이터셋을 다운로드받고 하나의 폴더에 데이터들을 합치는 코드 
# 해당 코드를 작성하여 각 데이터(v1 ~ v10)에 있는 데이터를 하나로 모음

dir_name = ['CAM_BACK_RIGHT',
 'CAM_FRONT',
 'RADAR_FRONT',
 'LIDAR_TOP',
 'RADAR_FRONT_LEFT',
 'RADAR_BACK_RIGHT',
 'RADAR_FRONT_RIGHT',
 'CAM_FRONT_LEFT',
 'CAM_BACK',
 'RADAR_BACK_LEFT',
 'CAM_FRONT_RIGHT',
 'CAM_BACK_LEFT']

data_name = ['v2', 'v3',                 # v1은 default로 설정하여 옮길필요 없음
             'v4', 'v5', 'v6',
             'v7', 'v8', 'v9', 'v10']

# # path이 존재하지 않으면, directory 생성
# if not os.path.exists(new_path):
#     os.mkdir(new_path)
    
# move # 내 데이터셋에 맞게 경로 설정
for i in data_name:
    for _ in dir_name:
        path = '/media/kaai/01efd209-945a-466d-a352-d7e1a0eda982/Dataset/NuScenes/train_dataset/' + i + '/sweeps/' + _ + '/' # samples, sweeps
        files = os.listdir(path)
        new_path = '/media/kaai/01efd209-945a-466d-a352-d7e1a0eda982/Dataset/NuScenes/train_dataset/total_train_dataset/sweeps/' + _ + '/' # samples, sweeps
        for file in files:
            shutil.move(path + file, new_path + file)
            print('{} has been moved to new folder!'.format(file))
      
    
    
    
# copy    
# for file in files:
#     if 'pdf' in file:
#         shutil.copy(path + file, new_path + file)
#         print('{} has been copied in new folder!'.format(file))
