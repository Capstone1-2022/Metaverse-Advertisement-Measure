import glob
import os  
import json 
import xml.etree.ElementTree as ET


unique_labels = {'roblox-avatar':1}

path = os.path.abspath("D:/장진우/캡스톤디자인I/광고 측정 모델/datasets/roblox/roblox data/JPEGImages/")
annotation_path = "D:/장진우/캡스톤디자인I/광고 측정 모델/datasets/roblox/roblox data/Annotations/"
dict ={}

for file in glob.glob(annotation_path + "*.xml"): 
  print(file)
  temp = file.split("\\")[-1][:-3]
  if temp == 'classes.':continue
  image_name= temp + "jpg"
  image_path = path + "/" + image_name
  print(image_path)
  tree = ET.parse(file)
  root = tree.getroot()
  boxs =[] 
  labels =[]
  difficulties = []
  for object in root.iter('object'):
    label = object.find('name').text.lower().strip()
    bbox = object.find('bndbox')
    xmin = int(bbox.find('xmin').text) - 1
    ymin = int(bbox.find('ymin').text) - 1
    xmax = int(bbox.find('xmax').text) - 1
    ymax = int(bbox.find('ymax').text) - 1
    boxs.append([xmin, ymin, xmax, ymax])
    labels.append(unique_labels[ label  ])
    difficulties.append(0)
  dict[image_path] = {"boxes": boxs, "labels": labels, "difficulties": difficulties} 

   			


train_images = list()
train_objects = list()
test_images = list()
test_objects = list()

val=['frame0004_jpg.rf.3049b76b9063fa36d462d02527bc4ea3',
'frame0019_jpg.rf.788f0e4d396d5104afc0221899397efb',
'frame0046_jpg.rf.8739ee33368dd1eae9b2f7d4ca7e83a8',
'frame0060_jpg.rf.76f93d270fd83c2c746cca9430c15c82',
'frame0073_jpg.rf.ec358d7c222270647f86260a056ecb60',
'frame0097_jpg.rf.5d50e9e15b29dec270fd8f9b7f0984d2',
'frame0106_jpg.rf.4aecb16db56e391d934ae35bcf29ce2c',
'frame0168_jpg.rf.da67c258e174be9f953a401d6f593e9e',
'frame0172_jpg.rf.d04ca701c737a48400674a7f9b1c298d',
'frame0173_jpg.rf.32fd7703d4c5a7c8fab23aafff16bf45',
'frame0190_jpg.rf.9d968ae571f0930bbf532cbcf2a91394',
'frame0206_jpg.rf.f6cd2694bec0e6ee119b64272e5aef37',
'frame0234_jpg.rf.d4fce647360684a23f305d250903b96f',
'frame0353_jpg.rf.6be08bc19d1df83d1730efd19ccebdc5',
'frame0479_jpg.rf.3ed12d639a7c88f0cab6bb1526666233',
'frame0481_jpg.rf.a8fd2097f83ca8002f0f1e769a883762']

for key in dict:
	name = key.split("/")[-1]
	name=name[0:-4]
	print(name)
	if name not in val:
		train_images.append(key)
		train_objects.append(dict[key])
	else:
		test_images.append(key)
		test_objects.append(dict[key])




output_folder = './'
# Save to file
with open(os.path.join(output_folder, 'TRAIN_images.json'), 'w') as j:
    json.dump(train_images, j)


with open(os.path.join(output_folder, 'TRAIN_objects.json'), 'w') as j:
    json.dump(train_objects, j)


with open(os.path.join(output_folder, 'label_map.json'), 'w') as j:
    json.dump(unique_labels, j)  # save label map too


with open(os.path.join(output_folder, 'TEST_images.json'), 'w') as j:
    json.dump(test_images, j)


with open(os.path.join(output_folder, 'TEST_objects.json'), 'w') as j:
    json.dump(test_objects, j)
