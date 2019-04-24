# -*- coding: utf-8 -*-
"""
@author: hyc

"""
import os
import random
import shutil
path = os.getcwd()
i = 0
num = 11
l = []
dirs1 = os.listdir(path + "\\..\\boundary")
while(i<num):
    l.append(path + "\\..\\boundary\\" + dirs1[random.randint(1, 1000)])
    i+=1
dirs2 = os.listdir(path + "\\..\\lift")
i = 0
while(i<num):
    l.append(path + "\\..\\lift\\" + dirs2[random.randint(0, 999)])
    i+=1
dirs3 = os.listdir(path + "\\..\\longInterval")
i = 0
while(i<num):
    l.append(path + "\\..\\longInterval\\" + dirs3[random.randint(0, 999)])
    i+=1
dirs4 = os.listdir(path + "\\..\\pureRandom")
i = 0
while(i<num):
    l.append(path + "\\..\\pureRandom\\" + dirs4[random.randint(0, 999)])
    i+=1
dirs5 = os.listdir(path + "\\..\\updown")
i = 0
while(i<num):
    l.append(path + "\\..\\updown\\" + dirs5[random.randint(0, 999)])
    i+=1
i = 0
while (i < num * 5):
    oldname= l[i]
    newname= path + "\\..\\mix\\" + str(i) + ".txt"
    shutil.copyfile(oldname,newname)
    i+=1
