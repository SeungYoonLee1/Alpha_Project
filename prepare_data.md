**NuScenes 데이터셋을 이용해 Model을 Training & Test**

Download nuScenes V1.0 full dataset data [HERE](https://www.nuscenes.org/download). Prepare nuscenes data by running

```
python tools/create_data.py nuscenes --root-path ./data/nuscenes --out-dir ./data/nuscenes --extra-tag nuscenes
```

**데이터셋을 다음과 같은 directory 경로로 설정해주어야 한다.**
![1 (1)](https://user-images.githubusercontent.com/69844293/174962462-c0c72df9-8c6e-4256-8ac4-a3138c82b995.png)

**Training 시, 데이터셋에 관한 오류를 방지하기 위해 해당 10개(Train)데이터셋을 하나로 뭉쳐야 한다.** 

**이를 위해, 각각을 압축 해제 & 합체하는 작업 수행** 

**각각의 폴더(v1~v10)에 압축 해제 수행**

![2](https://user-images.githubusercontent.com/69844293/174962583-611a29fc-39c0-4c50-b426-ca2953281b8d.png)

#### 데이터셋을 하나로 뭉치기 위해 폴더 내 파일을 옮기는 파이썬 코드를 작성 
![1 (2)](https://user-images.githubusercontent.com/69844293/174962627-0e004869-05e6-4d85-9cec-29fcd1b8e3fc.png)

```
import os 
# 내 데이터셋에 맞게 경로 설정
path_dir = '/media/kaai/01efd209-945a-466d-a352-d7e1a0eda982/Dataset/NuScenes/train_dataset/v2/samples'

file_list = os.listdir(path_dir)
file_list
```
![2 (1)](https://user-images.githubusercontent.com/69844293/174962836-1bfe874e-da91-4ad1-9a01-7905c339212f.png)

```
import os
import shutil


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
```

**코드를 이용하여 폴더 내 데이터들을 옮긴 모습**

**(위 폴더의 데이터를 아래 폴더로 옮김)**

![1 (3)](https://user-images.githubusercontent.com/69844293/174962954-021e2d92-e9c5-48b9-962b-27d704b003cc.png)

**최종적으로 사진과 같이 directory 설정**

![1 (4)](https://user-images.githubusercontent.com/69844293/174962994-3d063e1f-2d14-4a4f-9b6d-f635c3c0fb93.png)

