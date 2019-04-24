# -*- coding: utf-8 -*-
"""
@author: Sonic

"""
import os
import re
path= os.getcwd() + "\\"     
txtpattern = ".+\.txt"
#获取该目录下所有文件，存入列表中
fs=os.listdir(path)
n=0
for f in fs:
    if (re.match(txtpattern,f)):
    #设置旧文件名（就是路径+文件名）
        oldname = path + f  
    #设置新文件名
        newname = path + "LSJ_{}.txt".format(n)
    #用os模块中的rename方法对文件改名
        os.rename(oldname,newname)
        print(oldname,'======>',newname)
        n += 1

fs=os.listdir(path)
n=0
for f in fs:
    if (re.match(txtpattern,f)):
    #设置旧文件名（就是路径+文件名）
        oldname = path + f  
    #设置新文件名
        newname = path + "bullet_{}.txt".format(n)
    #用os模块中的rename方法对文件改名
        os.rename(oldname,newname)
        print(oldname,'======>',newname)
        n += 1
