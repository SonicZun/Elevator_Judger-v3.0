# -*- coding: utf-8 -*-
"""
@author: Sonic

"""
global tstart
global tuples
global punchPattern
global timePrevious
global timePresent
import time
import re
import sys

tstart = time.time()
tuples = []
punchPattern = "\[(.+)\]"

def timePunch():
    return ("[" + str(time.time() - tstart) + "]")

def preprocess():
    with open('bomber\\mode\\{}\\bullet_{}.txt'.format(sys.argv[1], int(sys.argv[2]))) as file:
        lines = file.readlines()
    for line in lines:
        match = re.match(punchPattern, line)
        if(not match):
            continue
        time = float(match.group(1))
        command = line[match.end():].strip()
        tupleElement = (time, command)
        tuples.append(tupleElement)
                
preprocess()
timePrevious = 0
time.sleep(2.6)    
for tupleElement in tuples:
    timePresent = tupleElement[0]
    time.sleep((timePresent - timePrevious))
    timePrevious = timePresent
    #print(timePunch() + str(tupleElement[0]) + " " + tupleElement[1]) # for debug
    print(tupleElement[1])
    sys.stdout.flush()
#time.sleep(0)
#print(timePunch() + chr(3))    #ASCII(3):ETX--END of TXT    #for debug
#print(chr(3))