# Alpha_Project
KOOKMIN UNIV, Alpha Project, 이승윤

Camera와 LiDAR의 센서퓨전 기법을 이용해 3D 공간상에 있는 다중 객체를 Detection & Tracking하는 딥러닝 시스템
nuScenes 데이터셋을 이용하여 Transformer기반의 TransFusion 모델을 학습시켰으며, Multi-Object가 성공적으로 Detection된 모습을 확인할 수 있다. <br>
TransFusion 모델 : Convolutional backbone과 transformer decoder기반의 detection head로 구성

## 3D Multi Object Detection & Tracking Using TransFusion
![t4](https://user-images.githubusercontent.com/69844293/174959258-7c6e7195-baf0-4aec-9470-a392015f623a.png)

## Environment Information 
![Environment](https://user-images.githubusercontent.com/69844293/174957423-b63d7352-98d3-44ca-b8a1-c91a7f92e31f.png)

## Setup Environment
[https://github.com/SeungYoonLee1/Alpha_Project/tree/main](https://github.com/SeungYoonLee1/Alpha_Project/blob/main/setup_environment.md)

## Prepare Data
https://github.com/SeungYoonLee1/Alpha_Project/blob/main/prepare_data.md

## Training
```
# 데이터 준비를 위한 코드 실행
python tools/create_data.py nuscenes --root-path ./data/nuscenes --out-dir ./data/nuscenes --extra-tag nuscenes
```
```
# Single GPU
## Detection
python tools/train.py configs/transfusion/detection/transfusion_nusc_voxel_LC.py
# --work-dir 명령행 옵션 부여 (log와 model의 저장을 위해) -lsy
# 만약 --work-dir이 None(아무것도 부여하지 않음)이면,
# default로 config파일이 있는 directory에 저장되도록 설정되어있다.
```
## Test
```
python tools/test.py ${CONFIG_FILE} ${CKPT_PATH} --eval 'mAP' --eval-options 'show=True' 'out_dir=${SHOW_DIR}'
python tools/test.py work_dirs/transfusion_nusc_voxel_LC/transfusion_nusc_voxel_LC.py work_dirs/transfusion_nusc_voxel_LC/latest.pth --eval 'mAP' --eval-options 'show=True' 'out_dir=result/'
```
## Reference

https://github.com/XuyangBai/TransFusion
```
@article{bai2021pointdsc,
  title={{TransFusion}: {R}obust {L}iDAR-{C}amera {F}usion for {3}D {O}bject {D}etection with {T}ransformers},
  author={Xuyang Bai, Zeyu Hu, Xinge Zhu, Qingqiu Huang, Yilun Chen, Hongbo Fu and Chiew-Lan Tai},
  journal={CVPR},
  year={2022}
}
```
