#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 09:37:38 2018
Image text recognition using Baidu api
@author: XnCSD
"""

import glob
from os import path
import os
from aip import AipOcr
from PIL import Image


def convertimg(picfile, outdir):
    '''Adjust image size and compress images that are too large
    picfile:    image path
    outdir：    image output path
    '''
    img = Image.open(picfile)
    width, height = img.size
    while (width * height > 4000000):  # The image compressed by this value is about more than 200k
        width = width // 2
        height = height // 2
    new_img = img.resize((width, height), Image.BILINEAR)
    new_img.save(path.join(outdir, os.path.basename(picfile)))


def baiduOCR(picfile, outfile):
    """Use Baidu API to recognize text and save the extracted text
    picfile:    image file name
    outfile:    output file
    """
    filename = path.basename(picfile)

    APP_ID = ''  # The ID just obtained, the same below
    API_KEY = ''
    SECRECT_KEY = ''
    client = AipOcr(APP_ID, API_KEY, SECRECT_KEY)

    i = open(picfile, 'rb')
    img = i.read()
    print("Recognizing pictures:\t" + filename)
    #message = client.basicGeneral(img)  #Universal text recognition, free for 50,000 transactions per day
    # message = client.basicAccurate(img)   #Universal text high-precision recognition, 800 times a day for free
    message = client.general(img)
    print("Recognition success!")
    i.close();
    print(message)
    '''with open(outfile, 'a+') as fo:
        fo.writelines("+" * 60 + '\n')
        fo.writelines("Identify pictures:\t" + filename + "\n" * 2)
        fo.writelines("Text content:\n")
        # output text content
        for text in message.get('words_result'):
            fo.writelines(text.get('words') + '\n')
        fo.writelines('\n' * 2)
    print("Text export successful!")'''
    print()


if __name__ == "__main__":

    outfile = 'export.txt'
    outdir = 'tmp'
    baiduOCR('1.png', outfile)#
