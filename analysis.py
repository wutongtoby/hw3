import matplotlib.pyplot as plt

import numpy as np

import serial

import time


t = np.arange(0,10,0.1) # signal vector
x = np.zeros(100)
y = np.zeros(100)
z = np.zeros(100)
tilt = np.zeros(100)
serdev = '/dev/ttyACM0'
s = serial.Serial(serdev)
s.baudrate = 115200

line=s.readline()
line=s.readline()
line=s.readline()
line=s.readline()
for i in range(0, 99):
    line=s.readline() # Read an echo string from K66F terminated with '\n'
    # print line
    x[i] = float(line.decode('utf-8'))
    line=s.readline()
    y[i] = float(line.decode('utf-8'))
    line=s.readline()
    z[i] = float(line.decode('utf-8'))
    line=s.readline()
    tilt[i] = float(line.decode('utf-8'))

plt.subplot(211)

l1,  = plt.plot(t,x)
l2,  = plt.plot(t,y)
l3,  = plt.plot(t,z)
plt.xlabel('Time')
plt.ylabel('Acc Vector')

plt.legend((l1, l2, l3), ('x', 'y', 'z'))


plt.subplot(212)

plt.stem(t,tilt)
plt.show()
plt.xlabel('Time')
plt.ylabel('Tilt')

s.close()