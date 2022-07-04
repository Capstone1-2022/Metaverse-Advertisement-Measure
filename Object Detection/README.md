## 파일구조
> annotation.py
- dataset 디렉토리에 있는 이미지와 xml 파일을 학습을 위해 분류해 json 파일에 저장함
- 이미지의 확장자를 제외한 이름을 val 리스트에 넣어 validation set으로 사용

> model.py
- 모델의 구조와 loss 함수
- loss 함수는 detection의 정확도 향상을 위해 confidence loss의 negative sample의 loss를 3배로 함

> modified_train.py
- 모델을 학습시킴
- batch_size, epoch, lr 등의 패러미터를 조정할 수 있음 (현재는 로컬 환경의 성능 문제로 batch_size를 4로 줄임)

> detect.py
- 모델을 사용해 object detection을 함
- detection할 이미지를 dataset 디렉토리에 넣고 이미지의 확장자를 제외한 이름을 test 리스트에 넣어서 사용함
- detect 함수에서 cropping과 detect된 object에 대해 사각형을 그리는 작업을 함

모델 출처:https://github.com/ppriyank/Object-Detection-Custom-Dataset-pytorch

<br>

## 로직 실행 방법
> `python3 detect.py` 명령어로 파이썬 스크립트 실행 가능

- 측정 대상 이미지 : `Object Detection/datasets/roblox/roblox data/JPEGImages` 에 있는 이미지들
   - 그 중에서도 detect.py 코드 내부 102 번째 코드라인에서 test 리스트에 선언된 것들만 선택된다.
- 측정 결과(아바타에 box 표시)
   - `Object Detection/Object-Detection-Custom-Dataset-pytorch-master/verify/verified image` 에 저장된다.
- 측정 결과(아바타 이미지 잘라내기)
   - `Object Detection/Object-Detection-Custom-Dataset-pytorch-master/verify/verified image/cropped image` 에 저장된다.