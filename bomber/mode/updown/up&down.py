# -*- coding: utf-8 -*-
"""
@author: Sonic

"""
import random
import math
minF = -3
maxF = 20
timeUnit = 0.4
reqAmount = 25
bulletAmount = 1000
def floorRandom(a, b):
    floor = 0
    while(floor == 0):
        floor = random.randint(a, b)
    return floor


def next2Req(tsd):#(time, start, destination)
    ns1 = floorRandom(minF, maxF)      #next start
    nd1 = ns1
    while (nd1 == ns1):
        nd1 = floorRandom(minF, maxF)
    ns2 = ns1
    if (ns2 == maxF or ns2 == minF):
        nd2 = ns2
        while (nd2 == ns2):
            nd2 = floorRandom(minF, maxF)
    else:
        if (nd1 > ns1):
            nd2 = ns2
            while (nd2 == ns2):
                nd2 = floorRandom(minF, ns2)
        else:
            nd2 = ns2
            while (nd2 == ns2):
                nd2 = floorRandom(ns2, maxF)
    mode = random.randint(0, 1)
    if (mode == 0):
        nt = tsd[0]
    else:    
        nt = random.uniform(tsd[0], tsd[0] + timeUnit * abs(tsd[2] - tsd[1]))
        nt = round(nt, 1)
    return [(nt, ns1, nd1), (nt, ns2, nd2)]

def reqList():
    t0 = round(random.uniform(0, 2), 1)
    s0 = floorRandom(-3, 2)
    d0 = s0
    while(d0 == s0):
        d0 = floorRandom(minF, maxF)
    tuplePre = (t0, s0, d0)
    rlist = [tuplePre]
    for i in range(0, reqAmount, 2):
        rlist += next2Req(rlist[i])
        #print(str(rlist))
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
        
    