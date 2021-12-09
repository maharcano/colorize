# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 23:13:26 2020

@author: pedro.brinca
"""

# Purpose: Colorize batches of tiff pictures  

# Description: This file takes all tiff files in the folder where it is run, 
# converts them to jpeg, uses deepai.org API to colorize the pictures which
# become available at a specified url and downloads them. It does so, picture
# by picture.

# Comments: The API has a guest api-key that is available for a limited number
# of colorizations (the one below). However, you can sign up their mailing list
# and get a fully functional one for free. Just access the same url below:
# https://deepai.org/machine-learning-model/colorizer
# while logged in. There is a max size output image to which all images are
# automatically rescaled to (keeping aspect ratio) if the input exceeds it.


#import cv2             # to convert TIFFS to JPEGS
import requests        # to request the API for the conversion
import urllib.request  # to download the colorized photo
import glob            # to map tiff files in folder into a list of filenames



for file in glob.glob("*.jpg"):
    r = requests.post(
        "https://api.deepai.org/api/colorizer",
        files={
            'image': open(file, 'rb'),
        },
        headers={'api-key': 'ace21ef6-d4f8-4bae-8a45-50743a341dd3'}
    )
    print(file)
    lnk = r.json()
    
    urllib.request.urlretrieve(lnk['output_url'], file)
    

for file in glob.glob("*.jpg"):
    r = requests.post(
        "https://api.deepai.org/api/waifu2x",
        files={
            'image': open(file, 'rb'),
        },
        headers={'api-key': 'ace21ef6-d4f8-4bae-8a45-50743a341dd3'}
    )
    print(file)
    lnk = r.json()
    
    urllib.request.urlretrieve(lnk['output_url'], file)

