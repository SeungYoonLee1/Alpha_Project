# Alpha_Project
KOOKMIN UNIV, Alpha Project

## Environment Information 
![Environment](https://user-images.githubusercontent.com/69844293/174957423-b63d7352-98d3-44ca-b8a1-c91a7f92e31f.png)

**Github에서 제공하는 환경설정**

[https://github.com/XuyangBai/TransFusion/blob/master/docs/getting_started.md](https://github.com/XuyangBai/TransFusion/blob/master/docs/getting_started.md)


#### **CUDA 10.1을 사용하는 경우,**
```
git clone [https://github.com/XuyangBai/TransFusion.git](https://github.com/XuyangBai/TransFusion.git) && cd TransFusion && pip install mmcv-full==1.2.4 && pip install mmdet==2.10.0 && pip install -r requirements/build.txt && pip install -v -e .
```

#### **CUDA 11.1을 사용하는 경우,**
아래 코드를 차례로 실행시키면, TransFusion 모델을 Training & Test 하기 위한 모든 환경설정이 완료된다.

```
conda create --name open-mmlab python=3.7 -y
conda activate open-mmlab
conda install pytorch torchivision -c pytorch
```

- CUDA 11.1의 경우 conda install pytorch==1.10.2 cudatoolkit==11.1 torchvision==0.11.3 -c pytorch
- 위 코드 진행시, pytorch와 torchvision을 CUDA 버전에 맞게 다운로드 해준다.

```
pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/cu111/torch1.10.2/index.html
```
```
git clone https://github.com/open-mmlab/mmcv.git
cd mmcv
MMCV_WITH_OPS=1 pip install -e .  # package mmcv-full will be installed after this step
cd ..
```
```
pip install git+https://github.com/open-mmlab/mmdetection.git
```
```
git clone https://github.com/open-mmlab/mmdetection.git
cd mmdetection
pip install -r requirements/build.txt
pip install -v -e .  # or "python setup.py develop"
```
- directory : mmdetection
- mmdetection 폴더에서 아래 코드들을 실행해주어야 한다.

```
git clone https://github.com/XuyangBai/TransFusion.git
cd TransFusion
pip install mmcv-full==1.2.4 && pip install mmdet==2.10.0
pip install -r requirements/build.txt
pip install -v -e .
```

**만약, pip install -v -e .에서 아래와 같은 오류**

**1 error detected in the compilation of ‘mmdet3d/ops/voxel/src/scatter_points_cuda.cu’. 에러가 발생할 경우,** 

**아래 사진과 같은 방법(diff —git)으로 해결한다.**

![solve1 (1)](https://user-images.githubusercontent.com/69844293/174958343-4ebdf71c-cae5-4cfd-a77b-01bedf0cdc84.png)

**그 후, pip install -v -e . 를 다시 실행해주면 정상적으로 설치된다.**

