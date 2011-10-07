#!/usr/bin/python2

import numpy as np
from sys import argv
import thread
import time

from Xlib import display

disp = display.Display() #open display
geometry = (disp.screen()._data['width_in_pixels'],
            disp.screen()._data['height_in_pixels'])
 
def mousepos():
    """mousepos() --> (x, y) get the mouse coordinates on the screen (linux, Xlib)."""
    data = display.Display().screen().root.query_pointer()._data
    return (data['root_x'], geometry[1] - data['root_y'])
 

def data_routine(list_ref):
    """periodically calls mousepos and adds the data to a list"""
    while recording:
        list_ref.append(mousepos())
        time.sleep(100)
        print len(list_ref)


#header = ('# Mouse Data\n# '+time.strftime('%d.%m.%y %H:%M:%S'))
filename = 'data'+time.strftime('%d%m%H%M%S')
data = []
#recording = True
#thread.start_new(data_routine,(data,))
#a = raw_input('press ENTER to stop')
#recording = False

while True:
    try:
        data.append(mousepos())
        time.sleep(0.01)
    except KeyboardInterrupt:
        print 'ping'
        break

np.savetxt(filename,np.array(data))

