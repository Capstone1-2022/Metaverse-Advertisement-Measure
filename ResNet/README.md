#ResNet50을 이용한 아바타 클러스터링
##ResNet50 학습
ResNet50.ipynb를 수행하면 train폴더 내에 있는 이미지 폴더 각각을 레이블링해 학습을 시작한다.
학습이 완료된 후의 parameter는 resnet50.pt에 저장됨
대표적인 parameter인 lr, epoch는 13번 코드블록과 17번 코드블록에서 변경이 가능함.
"""
lr = 0.0008
epochs = 2500
optimizer = 'Adam'
"""
"""
lr_sche = optim.lr_scheduler.StepLR(config.optimizer, step_size=1000, gamma=0.5)
epochs = 2000
log_interval = 100

ready_to_train.train(epochs, log_interval)
"""
-----------------------------------------------------
##Resnet50 기반 이미지 구분
ResNet50의 구조를 선언한 뒤, resnet50.pt에 저장되어있는 parameter들을 불러온다.
load_resnet.ipynb 수행 시 ./test 폴더 내에 있는 이미지 폴더 각각을 레이블링해 모델의 입력값으로 한다.
-> test data가공 = transforms와 DataLoader를 통해 수행
-> get_representation 함수를 통해 test -> testoutputs, testlabels에 결과값 저장
-> get_lda() 또는 get_tsne()를 통해 3차원 결과값을 2차원으로 축소
-> mscluster()를 통해 축소된 데이터를 mean-shift clustering하고 결과를 출력 (cluster의 수, cluster 결과)