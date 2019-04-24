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
    ns = floorRandom(min(tsd[1], tsd[2]), max(tsd[1], tsd[2]))      #next start
    nd = ns
    while (nd == ns):
        nd = floorRandom(minF, maxF)
    mode = random.randint(0, 1)
    if (mode == 0):
        nt = tsd[0]
    else:    
        nt = tsd[0] + 10
        nt = round(nt, 1)
    return (nt, ns, nd)

def reqList():
    t0 = round(random.uniform(0, 2), 1)
    s0 = floorRandom(-3, 2)
    d0 = s0
    while(d0 == s0):
        d0 = floorRandom(minF, maxF)
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
        
    