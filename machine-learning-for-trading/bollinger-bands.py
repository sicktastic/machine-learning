# https://www.youtube.com/watch?v=u34HNFMp8Fw
# by sentdex

import numpy as np
import time

sampleData = open('sampleData.txt', 'r').read()
splitDate = sampleData.split('\n')

date, closep, highp, lowp, openp, volume = np.loadtxt(splitDate, delimiter=',', unpack=True)

def standard_deviation(tf, prices):
    sd = []
    sddate = []
    x = tf
    while x <= len(prices):
        array2consider = prices[x-tf:x]
        standev = array2consider.std()
        sd.append(standev)
        sddate.append(date[x])
        x += 1
    return sddate, sd

def moving_average(value, window):
    weights = np.repeat(1.0, window) / window
    smas = np.convolve(values, weights, 'valid')
    return smas

def bollinger_bands(mult, tff):
    bdate = []
    topBand = []
    botBadn = []
    midBand = []

    x = tff

    while x < len(date)
        curSMA = moving_average(closep[x-tff:x], tff)[-1]

        d, curSD = standard_deviation(tff, closep[0:tff])
        curSD = curSD[-1]

        TB = curSMA + (curSD * mult)
        BB = curSMA - (curSD * mult)
        D = date[x]

        bdate.append(D)
        topBand.append(TB)
        botBand.append(BB)
        midBand.append(curSMA)

        x += 1

    return ddate, topBand, botBand, midBand

d, tb, bb, mb =  bollinger_bands(2, 20)

print d
print tb
print bb
print mb
