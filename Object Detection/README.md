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

사용하지 않아도 

