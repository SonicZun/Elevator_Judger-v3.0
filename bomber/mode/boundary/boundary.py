# -*- coding: utf-8 -*-
"""
@author: Sonic

"""
import random
import math
minF = -3
maxF = 20
timeUnit = 0.4
reqAmount = 15
bulletAmount = 1000
def floorRandom(a, b):
    floor = 0
    while(floor == 0):
        floor = random.randint(a, b)
    return floor

def nextReq(tsd):#(time, start, destination)
    mode = random.randint(0, 1)
    bdlist = [minF, maxF, -1, 1] 
    sd = random.sample(bdlist, 2)
    mode = random.randint(0, 1)
    ns = sd[0]
    nd = sd[1]
    if (mode == 0):
        nt = tsd[0]
    else:    
        nt = random.uniform(tsd[0], tsd[0] + timeUnit * abs(tsd[2] - tsd[1]))
        nt = round(nt, 1)
    return (nt, ns, nd)

def reqList():
    t0 = round(random.uniform(0, 2), 1)
    mode = random.randint(0, 1)
    if (mode == 0):
        s0 = minF
        d0 = maxF
    else:
        s0 = maxF
        d0 = minF
    tuplePre = (t0, s0, d0)
    rlist = [tuplePre]
    for i in range(0, reqAmount - 1):
        rlist.append(nextReq(rlist[i]))
    return rlist

def makeBullet(num):
    f = open("bullet_{}.txt".format(num), 'w')
    rl = reqList()
    for i in range(0, reqAmount):
        req = rl[i]
        f.write("[{}]{}-FROM-{}-TO-{}\n".format(req[0], i, req[1], req[2]))
    f.close()

for i in range(0, bulletAmount):
    makeBullet(i)
        
    