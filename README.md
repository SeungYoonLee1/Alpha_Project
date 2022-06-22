# Alpha_Project
KOOKMIN UNIV, Alpha Project, 이승윤

Camera와 LiDAR의 센서퓨전 기법을 이용해 3D 공간상에 있는 다중 객체를 Detection & Tracking하는 딥러닝 시스템
nuScenes 데이터셋을 이용하여 Transformer기반의 TransFusion 모델을 학습시켰으며, Multi-Object가 성공적으로 Detection된 모습을 확인할 수 있다. <br>
TransFusion 모델 : Convolutional backbone과 transformer decoder기반의 detection head로 구성

## 3D Multi Object Detection & Tracking Using TransFusion
![t4](https://user-images.githubusercontent.com/69844293/174959258-7c6e7195-baf0-4aec-9470-a392015f623a.png)

## Environment Information 
![Environment](https://user-images.githubusercontent.com/69844293/174957423-b63d7352-98d3-44ca-b8a1-c91a7f92e31f.png)

## 환경설정
[https://github.com/SeungYoonLee1/Alpha_Project/tree/main](https://github.com/SeungYoonLee1/Alpha_Project/blob/main/setup_environment.md)

## 데이터 준비
https://github.com/SeungYoonLee1/Alpha_Project/blob/main/prepare_data.md

## Reference
```
@article{bai2021pointdsc,
  title={{TransFusion}: {R}obust {L}iDAR-{C}amera {F}usion for {3}D {O}bject {D}etection with {T}ransformers},
  author={Xuyang Bai, Zeyu Hu, Xinge Zhu, Qingqiu Huang, Yilun Chen, Hongbo Fu and Chiew-Lan Tai},
  journal={CVPR},
  year={2022}
}
```
