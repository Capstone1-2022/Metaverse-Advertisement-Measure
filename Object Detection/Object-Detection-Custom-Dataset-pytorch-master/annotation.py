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

val=['frame0004_jpg.rf.dfe84a1fd1d9744109a1b159b66b94b7',
'frame0005_jpg.rf.730719df8ce70273e11d08feb1eeece4',
'frame0019_jpg.rf.788f0e4d396d5104afc0221899397efb',
'frame0046_jpg.rf.8739ee33368dd1eae9b2f7d4ca7e83a8',
'frame0047_jpg.rf.c9caa02af012840633bedfa73292e12f',
'frame0060_jpg.rf.dfae1b843b967bfe2b1f616ba28a2b5f',
'frame0073_jpg.rf.184e994071a6855a6bd4795087502449',
'frame0097_jpg.rf.5d50e9e15b29dec270fd8f9b7f0984d2',
'frame0100_jpg.rf.2ec63422a935304fa6f01417c9cc48aa',
'frame0106_jpg.rf.51d8f6b5b5c900ba2eb2dd3ffd319a99',
'frame0108_jpg.rf.32652c06bca060ba55e794ee7d364da6',
'frame0143_jpg.rf.253fce5af93734b94aaa6e1166dafe72',
'frame0168_jpg.rf.da67c258e174be9f953a401d6f593e9e',
'frame0172_jpg.rf.d04ca701c737a48400674a7f9b1c298d',
'frame0173_jpg.rf.edce58d2f66872f5c6eddbeb9b73ee7a',
'frame0190_jpg.rf.9d968ae571f0930bbf532cbcf2a91394',
'frame0206_jpg.rf.40f82d831f569613152f6c8911e65494',
'frame0214_jpg.rf.a22cf124fd1c52e9b37bcb7d5a88a51a',
'frame0221_jpg.rf.5122ea211f9c39716aa0318148e36b65',
'frame0234_jpg.rf.d4fce647360684a23f305d250903b96f',
'frame0353_jpg.rf.6be08bc19d1df83d1730efd19ccebdc5',
'frame0381_jpg.rf.aa9d875622bc1d404a68f2339b61762e',
'frame0403_jpg.rf.c5adf5db789a591b8367f8bd1c01dc94',
'frame0414_jpg.rf.4a26297374281069ee932212bca298e8',
'frame0445_jpg.rf.2081cb17448478a72976f82eea747a34',
'frame0445_jpg.rf.7bba8d651506f3a178ae4cf41292b8db',
'frame0475_jpg.rf.1af5480daa9cc22216d9ffa17f9c58fa',
'frame0479_jpg.rf.3ed12d639a7c88f0cab6bb1526666233',
'frame0481_jpg.rf.b853383c8808da8adfefb99839889fa7'
]

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
