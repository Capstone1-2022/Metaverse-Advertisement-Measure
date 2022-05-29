https://github.com/ultralytics/yolov5

SSD보다 이후에 나온 모델인 YOLOv5를 사용했음

cmd에서

    python train.py --img 640 --batch 4 --epochs 100 --data data.yaml --weights yolov5s.pt --cache

사용하여 train함

학습환경에 따라 batch size나 epoch 변경 가능

학습결과는 yolov5-master/runs/train에 저장됨


학습데이터는 Roboflow에서 만들었음

Roboflow에서 학습데이터 가공 후 다운 받아서 datasets 폴더에 경로에 맞춰 넣으면 학습에 사용가능

.yaml 파일은 yolov5-master/data에 넣어야 함


wandb.ai 사용하여 실시간으로 학습과정 볼 수 있음

--------------------------------------------------------------------------------------------------------------------






https://github.com/ppriyank/Object-Detection-Custom-Dataset-pytorch
Custom Dataset으로 학습 가능한 SSD
detect.py에서 img_path를 detect하고 싶은 이미지의 path로 바꾸고 python detect.py로 실행하면 verify 폴더 안의 verified image 폴더에 테스트 이미지에 레이블이 달린 것이 저장되고 레이블이 달릴 각각의 box를 crop한 것이 cropped image에 
