# -*- coding: utf-8 -*-
"""
@author: Sonic

"""
import re
from enum import Enum
import os
import sys
import ctypes


path = os.getcwd()

#print mode available to console
'''
dirs = os.listdir(path + "\\bomber\\mode")
print("\nChoose a bombing mode:\n")
for dir in dirs:
    print(dir + " ", end = "")
print("\n")
'''

#choose a mode
#string_mode = input()
string_mode = sys.argv[1]
output_dir = "output\\"
bullet_dir = "bomber\\mode\\" + string_mode + "\\"


#bullet amount
#print("\nInput the bullet amount:\n")
bullet_amount = int(sys.argv[2])


#result path
result_path = "result\\WA_details.txt"
abstract_path = "result\\abstract.txt"
resulttxt = open(result_path, 'w')
abstracttxt = open(abstract_path, 'w')

#initialize
patternIN = "\[(.+)\]IN-(-?\d+)-(-?\d+)-(.*)"
patternOUT = "\[(.+)\]OUT-(-?\d+)-(-?\d+)-(.*)"
patternOPEN = "\[(.+)\]OPEN-(-?\d+)-(.*)"
patternCLOSE = "\[(.+)\]CLOSE-(-?\d+)-(.*)"
patternARRIVE = "\[(.+)\]ARRIVE-(-?\d+)-(.*)"

patternReq = "\[.+\](-?\d+)-FROM-(-?\d+)-TO-(-?\d+)"

e1 = " Attemps To Break In !\n"
e2 = " Attemps To Break Out !\n"
e3 = "The Door Has Already Closed !\n"
e4 = "Ghost Appear !\n"
e5 = " Never Came IN !\n"
e6 = "The Door Has Already Opened !\n"
e7 = " Still In The Elevator !\n"
e8 = "The Door Isn't Closed In The End!\n"
e9 = "Something Wrong with the request of ID "
e10 = " An Opened Elevator Arrive?\n"
e11 = " Duplicately Arrive At Floor "
e12 = " Jump From {} To {}!\n"
e13 = " Arrive Doesn't Match In!\n"
e14 = " Close Too Fast At Floor " 
e15 = " Arrive Too Fast To {}!\n"
e16 = " Time Recurse!\n"

def readStatus(line):
    matchIN = re.match(patternIN, line)
    matchOUT = re.match(patternOUT, line)
    matchOPEN = re.match(patternOPEN, line)
    matchCLOSE = re.match(patternCLOSE, line)
    matchARRIVE = re.match(patternARRIVE, line)   
    if(re.match(patternIN, line)):
        return ["IN", float(matchIN.group(1)), int(matchIN.group(2)), int(matchIN.group(3)), matchIN.group(4)]
    elif(re.match(patternOUT, line)):
        return ["OUT", float(matchOUT.group(1)), int(matchOUT.group(2)), int(matchOUT.group(3)), matchOUT.group(4)]
    elif(re.match(patternOPEN, line)):
        return ["OPEN", float(matchOPEN.group(1)), int(matchOPEN.group(2)), matchOPEN.group(3)]
    elif(re.match(patternCLOSE, line)):
        return ["CLOSE", float(matchCLOSE.group(1)), int(matchCLOSE.group(2)), matchCLOSE.group(3)]
    elif(re.match(patternARRIVE, line)):
        return ["ARRIVE", float(matchARRIVE.group(1)), int(matchARRIVE.group(2)), matchARRIVE.group(3)]
    else:
        return ["WRONG FORMAT!"]

def readReq(line):
    match = re.match(patternReq, line)
    if(re.match(patternReq, line)):
        return [int(match.group(1)), int(match.group(2)), int(match.group(3))]  #(id, start, destination)
    else:
        return ["WRONG FORMAT!"]

def limitCheck(filepath):
    lineNumber = 0
    status = True
    limitA = [-3,-2,-1,1,15,16,17,18,19,20]
    limitB = [-2,-1,1,2,4,5,6,7,8,9,10,11,12,13,14,15]
    limitC = [1,3,5,7,9,11,13,15]
    reqList = []
    with open(filepathIn) as file:
        lines = file.readlines()
    for line in lines:
        newReq = readReq(line)
        if(newReq[0] == "WRONG FORMAT!" or newReq[0] == "ARRIVE"):
            continue
        lineNumber += 1
        if(newReq[0] == "OPEN" or newReq[0] == "CLOSE"):
            if(newReq[3] == "A" and newReq[2] not in limitA or newReq[3] == "B" and newReq[2] not in limitB or newReq[3] == "C" and newReq[2] not in limitC):
                print(newReq[3] + e17)
                status = False
        elif(newReq[0] == "ARRIVE" and newReq[3] == "A"):
            Alast = newReq[2]
        elif(newReq[0] == "ARRIVE" and newReq[3] == "B"):
            Blast = newReq[2]
        elif(newReq[0] == "ARRIVE" and newReq[3] == "C"):
            Clast = newReq[2]  
    if (Alast not in limitA):
        print("A" + e18)
        status = False
    elif (Blast not in limitB):
        print("B" + e18)
        status = False    
    elif (Clast not in limitC):
        print("C" + e18)
        status = False  
    if(status == True):
        print("    ---Limit Check Pass!---")
        return True
    else:
        print("***WA: Logic Check Failed!***")      
        return False 

def logicCheck(filepath, elv):
    Status = Enum('Status', ('sCLOSE', 'sOPEN', 'WA'))
    status = Status.sCLOSE
    personInner = []
    with open(filepath) as file:
        lines = file.readlines()
    lineNumber = 0
    for line in lines:
        info = readStatus(line)
        if(info[0] == "WRONG FORMAT!"):
            continue
        if (len(info) == 4 and info[3] != elv):
            continue
        if (len(info) == 5 and info[4] != elv):
            continue
        lineNumber += 1
        if(status == Status.sCLOSE):
            if(info[0] == "IN"):
                print("elevator " + elv + " " + str(lineNumber) + ": " + "ID " + str(info[2]) + e1)
                status = Status.WA
                break
            elif(info[0] == "OUT"):
                print("elevator " + elv + " " + str(lineNumber) + ": " + "ID " + str(info[2]) + e2)
                status = Status.WA
                break
            elif(info[0] == "OPEN"):
                status = Status.sOPEN
            elif(info[0] == "CLOSE"):
                print("elevator " + elv + " " + str(lineNumber) + ": " + e3)
                status = Status.WA
                break
        elif(status == Status.sOPEN):
            if(info[0] == "IN"):
                personInner.append(info[2])
            elif(info[0] == "OUT"):
                if(len(personInner) <= 0):
                    print("elevator " + elv + " " + str(lineNumber) + ": " + e4)
                    status = Status.WA
                    break
                else:
                    if(info[2] not in personInner):
                        print("elevator " + elv + " " + str(lineNumber) + ": " + str(info[2]) + e5)
                        status = Status.WA
                        break
                    else:
                        personInner.remove(info[2])
            elif(info[0] == "OPEN"):
                print("elevator " + elv + " " + str(lineNumber) + ": " + e6)
                status = Status.WA
                break
            elif(info[0] == "CLOSE"):
                status = Status.sCLOSE
            elif(info[0] == "ARRIVE"):
                print("elevator " + elv + " " + str(lineNumber) + ": " + e10)
                status = Status.WA
                break
    if(len(personInner) > 0):
        for person in personInner:
            print("elevator " + elv + " " + "ID " + str(person) + e7)
            status = Status.WA
    elif(status == Status.sOPEN):
        print("elevator " + elv + " " + e8)
        status = Status.WA
    
    if(status == Status.sCLOSE):
        print("elevator " + elv + " " + "    ---Logic Check Pass!---")
        return True
    else:
        print("elevator " + elv + " " + "***WA: Logic Check Failed!***")      
        return False     


def map(n):
    if (n < 0):
        return n + 3
    else:
        return n + 2
def demap(n):
    if (n < 3):
        return n - 3
    else:
        return n - 2

def logicCheck_plus(filepath, elv):
    status = True
    pre_floor = map(1)
    with open(filepath) as file:
        lines = file.readlines()
    lineNumber = 0
    for line in lines:
        info = readStatus(line)
        if (info[0] == "WRONG FORMAT!"):
            continue
        if (len(info) == 4 and info[3] != elv):
            continue
        if (len(info) == 5 and info[4] != elv):
            continue
        lineNumber += 1
        if (info[0] == "ARRIVE"):
            if (map(info[2]) == pre_floor):
                print("elevator " + elv + " " + str(lineNumber) + ": " + e11 + str(info[2]) + "\n")
                status = False
                break
            elif (abs(map(info[2]) - pre_floor) > 1):
                print("elevator " + elv + " " + str(lineNumber) + ": " + e12.format(demap(pre_floor), info[2]))
                status = False
                break
            else:
                pre_floor = map(info[2])
        elif (info[0] == "IN"):
            if (map(info[3]) != pre_floor):
                print("elevator " + elv + " " + str(lineNumber) + ": " + e13)
                status = False
                break
    if(status == True):
        print("elevator " + elv + " " + "    ---Logic Check Plus Pass!---")
        return True
    else:
        print("elevator " + elv + " " + "***WA: Logic Check Plus Failed!***")      
        return False 


def functionCheck(filepathIn, filepathOut):
    reqList = []
    with open(filepathIn) as file:
        lines = file.readlines()
    for line in lines:
        newReq = readReq(line)
        if(newReq[0] == "WRONG FORMAT!" or newReq[0] == "ARRIVE"):
            continue 
        inList = False
        for req in reqList:
            if(req[0] == newReq[0]):
                inList = True
                req[2] = newReq[2]
        if(not inList):
            reqList.append(newReq)
    reqList.sort(key = lambda req: req[0])
    
    resultList = []
    with open(filepathOut) as file:
        lines = file.readlines()
    for line in lines:
        newResult = readStatus(line)
        if(newResult[0] != "IN" and newResult[0] != "OUT" ):
            continue
        find = False
        if(newResult[0] == "IN"):
            for result in resultList:
                if(result[0] == newResult[2]):
                    find = True
            if(not find):
                resultList.append([newResult[2], newResult[3], 0])
        elif(newResult[0] == "OUT"):
            for result in resultList:
                if(result[0] == newResult[2]):
                    result[2] = newResult[3]
    resultList.sort(key = lambda result: result[0])
    reqList_backup = reqList.copy()
    resultList_backup = resultList.copy()
    #print("reqList: \n" + str(reqList_backup))
    #print("resultList: \n" + str(resultList_backup))
    for i in range(max(len(reqList), len(resultList))):
        if(i >= len(resultList) or i >= len(reqList) or reqList[i] != resultList[i]): 
            if(i >= len(reqList)):
                print("ID " + str(resultList[i][0]) + " Shouldn't Appear!\n")
            else:
                print(e9 + str(reqList[i][0]) + "\n")
            print("***WA: Function Check Failed!***")
            print("[id, start, destination]")
            print("\nreqList: \n" + str(reqList_backup)[1 : len(str(reqList_backup)) - 1])
            print("\nresultList: \n" + str(resultList_backup)[1 : len(str(resultList_backup)) - 1])
            return False
        
        
        
    #print("[id, start, destination]")
    #print("\nreqList: \n" + str(reqList_backup)[1 : len(str(reqList_backup)) - 1])
    #print("\nresultList: \n" + str(resultList_backup)[1 : len(str(resultList_backup)) - 1])
    print("    ---Function Check Pass!---")
    return True

def timeCheck(filepath):
    status = True
    pre_open = 0.0
    pre_time = 0.0
    with open(filepath) as file:
        lines = file.readlines()
    lineNumber = 0
    for line in lines:
        info = readStatus(line)
        if (info[0] == "WRONG FORMAT!"):
            continue
        if (info[1] < pre_time):
            print(str(lineNumber) + ": " + e16)
            status = False
            break
        lineNumber += 1
        if (info[0] == "CLOSE"):
            if (info[1] - pre_open < 0.39):
                print(str(lineNumber) + ": " + e14 + str(info[2]) + "\n")
                status = False
                break 
        elif (info[0] == "OPEN"):
            pre_open = info[1]
        elif (info[0] == "ARRIVE"):
            if (info[1] - pre_time < 0.39):
                print(str(lineNumber) + ": " + e15.format(info[2]))
                status = False
                break 
        pre_time = info[1]
    if(status == True):
        print("    ---Time Check Pass!---")
        return True
    else:
        print("***WA: Time Check Plus Failed!***")      
        return False 


def Check(i):
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("* Bombing Mode: " + string_mode)
    print("\n* Bullet ID: " + str(i))
    print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
    result_logicA = logicCheck(output_dir + "output_{}.txt".format(i), "A")
    print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
    result_logicB = logicCheck(output_dir + "output_{}.txt".format(i), "B")
    print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
    result_logicC = logicCheck(output_dir + "output_{}.txt".format(i), "C")
    print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
    result_logicpA = logicCheck_plus(output_dir + "output_{}.txt".format(i), "A")
    print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
    result_logicpB = logicCheck_plus(output_dir + "output_{}.txt".format(i), "B")
    print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
    result_logicpC = logicCheck_plus(output_dir + "output_{}.txt".format(i), "C")    
    print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
#    result_time = timeCheck(output_dir + "output_{}.txt".format(i))
#    print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
    result_function = functionCheck(bullet_dir + "bullet_{}.txt".format(i), output_dir + "output_{}.txt".format(i))   
    print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
    return result_logicA and result_logicB and result_logicC and result_logicpA and result_logicpB and result_logicpC and result_function 
WA_list = []
for i in range(0, bullet_amount):
    check_result = Check(i)
    if (not check_result):
        WA_list.append(i)
        savedStdout = sys.stdout
        sys.stdout = resulttxt
        Check(i)
        sys.stdout = savedStdout
savedStdout = sys.stdout
sys.stdout = abstracttxt
if(len(WA_list) == 0):
    print("All pass!")
else:
    print("WA: ", end = "")
    for wa in WA_list:
        print(str(wa) + " ", end = "")

resulttxt.close()
abstracttxt.close()