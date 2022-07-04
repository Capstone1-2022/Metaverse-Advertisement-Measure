#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Image text recognition using Baidu api

"""

import glob
from os import path
import os
from aip import AipOcr
from PIL import Image
import cv2
import numpy as np
def check(s1,s2):
    num1=len(s1)
    num2=len(s2)
    dp=np.zeros((num1+2,num2+2), dtype=np.int)
    for i in range(0,num1+1):
        dp[i][0]=i
    for i in range(0,num2+1):
        dp[0][i]=i
    for i in range(1,num1+1):
        for j in range(1,num2+1):
            if(s1[i-1]==s2[j-1]):
                dp[i][j]=dp[i-1][j-1]
            else:
                MIN=dp[i][j-1]+1
                MIN=min(MIN,dp[i-1][j]+1)
                MIN=min(MIN,dp[i-1][j-1]+1)
                dp[i][j]=MIN

    return dp[num1][num2]
def convertimg(picfile, outdir):
    '''Adjust image size and compress images that are too large
     picfile: image path
     outdir: image output path
    '''
    img = Image.open(picfile)
    width, height = img.size
    while (width * height > 4000000):  # The image compressed by this value is about more than 200k
        width = width // 2
        height = height // 2
    new_img = img.resize((width, height), Image.BILINEAR)
    new_img.save(path.join(outdir, os.path.basename(picfile)))


def baiduOCR(picfile):
    """Use Baidu API to recognize text and save the extracted text
     picfile: image file name
     outfile: output file
    """
    filename = path.basename(picfile)

    APP_ID = '26145723'  # The ID just obtained, the same below
    API_KEY = 'aGkwAg40AqorWGGP9GUvFsGN'
    SECRECT_KEY = 'SpBxYvzmYvyjWnsTOHbk088t6GioK0CQ'
    client = AipOcr(APP_ID, API_KEY, SECRECT_KEY)

    i = open(picfile, 'rb')
    img = i.read()
    #print("Recognizing pictures：\t" + filename)
    #message = client.basicGeneral(img)  # Universal text recognition, free for 50,000 transactions per day
    # message = client.basicAccurate(img)   # Universal text high-precision recognition, 800 times a day for free
    message = client.general(img)
    #print("Recognition success!")
    i.close();
    #print(message)
    #print()
    return message

print(check('Hahd dba��jdh','Hdhdidbdxjdh'))
print(len('Hahd dba��jdh'))
if __name__ == "__main__":
    m={}
    path1 = "RobloxTextImages"  # folder directory
    files = os.listdir(path1)  # Get the names of all files in a folder
    s = []
    for file in files:  # Traverse folders
        if not os.path.isdir(file):  # Determine whether it is a folder, not a folder to open
            filename=path1 + "/" + file
            message=baiduOCR(path1 + "/" + file)
            img = cv2.imread(path1 + "/" + file)
            num=0
            for k in range(0,len(message['words_result'])):
                cv2.rectangle(img, (message['words_result'][k]['location']['left'], message['words_result'][k]['location']['top']), (message['words_result'][k]['location']['left']+message['words_result'][k]['location']['width'], message['words_result'][k]['location']['top']+message['words_result'][k]['location']['height']), (0, 255, 0), 2)
                cv2.imwrite(file, img)
                word=message['words_result'][0]['words']
                if(word in m):
                    m[word]+=1
                else:
                    flag=False
                    for i in m.items():
                        if(check(word,i[0])<=5 and len(word)>5):
                            flag=True
                            m[i[0]]+=1
                            break
                    if(flag==False):
                        m[word]=1

    f=open("jieguo.txt",'w')
    for i in m.items():
        f.write(i[0]+': '+str(i[1])+'\r')
