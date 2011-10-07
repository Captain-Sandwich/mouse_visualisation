#!/usr/bin/python2

from matplotlib.mlab import amap
import matplotlib.pyplot as plt
import numpy as np
import sys

STOP_TRESHOLD = 5 # 0.5 secs stop
DOT_SCALING = 20

try:
    #y,x = np.loadtxt(sys.argv[1],int,unpack=True)
    data = np.loadtxt(sys.argv[1],int,unpack=True).transpose()
except:
    print 'Data file corrupt.'
    sys.exit(1)

def find_stops(x,y):
    n = len(x) #length is the same
    index = 0
    finds = []
    while index < n-2:
        count = 0
        while x[index] == x[index+1] and y[index] == y[index+1] and index < n-2:
            count = count+1
            if index < n-2:
                index = index+1
        if count >= STOP_TRESHOLD:
            finds.append( (x[index],y[index],count*DOT_SCALING) )
        index = index+1

def find_stops(data):
   n = len(data) #length is the same
   index = 0
   finds = []
   while index < n-2:
       count = 0
       while (data[index] == data[index+1]).all():
           count = count+1
           if index < n-2:
               index = index+1
           else:
               break
       if count >= STOP_TRESHOLD:
           finds.append( np.append(data[index],count*DOT_SCALING) )
       index = index+1
   return np.array(finds)


dots = find_stops(data)
    

#H, xedges, yedges = np.histogram2d(x, y, bins=(16, 15))
#H.shape, xedges.shape, yedges.shape
#extent = [yedges[0], yedges[-1], xedges[-1], xedges[0]]
#plt.imshow(H, extent=extent, interpolation='nearest')
#plt.colorbar()
#plt.show()

plt.plot(*data.transpose(),color='k',alpha=0.3)
plt.scatter(*dots.transpose(),color='k',alpha=0.3)
plt.show()
