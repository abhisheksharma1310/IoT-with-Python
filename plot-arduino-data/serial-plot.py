import serial
import matplotlib.pyplot as plt
import numpy as np

plt.ion()
fig = plt.figure()

i = 0
x = list()
y = list()

ser = serial.Serial("COM15", 9600)
ser.close()
ser.open()

while True:
    data = ser.readline()
    print(data.decode())
    x.append(i)
    y.append(data.decode())

    plt.scatter(i, float(data.decode()))
    i += 1
    plt.show()
    plt.pause(0.01)
