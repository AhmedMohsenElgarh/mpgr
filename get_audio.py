#! /usr/bin/env python

# Copyright 2019  QCRI (Authors: Ahmed Ali)
# Apache 2.0.

##
# This script shows how to crawl the MGB-3 audio files.
# You may need to run the script few times as sometime youtube blocks crawling
##

import subprocess
import os
import sys

    
if not os.path.exists('wav'): os.mkdir('wav')

f = open("/content/drive/MyDrive/mgb3_asr/mgb3/map","r") 


for line in f:
    audioFile='./wav/'+str(line.split()[0])+'.wav'
    youtubeID=line.split()[1]
    if os.path.exists(audioFile): 
        print ("Exist: ", audioFile)
        continue 
    print ("Processing: ", audioFile, youtubeID)
    subprocess.run(['youtube-dl','-f','[ext=mp4]','--output','tmp.mp4',"--",str(youtubeID)],stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    subprocess.run(['ffmpeg','-i','tmp.mp4','tmp.wav'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    subprocess.run(['/usr/local/lib/python3.7/dist-packages/sox','tmp.wav','-r','16000','-c','1',str(audioFile),'trim','0','720'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if os.path.exists("tmp.mp4"): os.remove("tmp.mp4")
    if os.path.exists("tmp.wav"): os.remove("tmp.wav")


