import serial
from serial import Serial
import time
import numpy as np

ser=serial.Serial("COM6",115200)

while True:       
        ser.write(str.encode('0'))
        read=ser.readline().decode("utf-8")
        r=list(read.split(","))
        data=r[4:10]
        #print(data)
        a=[]
        #l3=[]
        for i in data:
                a.append(float(i))
        l3=np.asarray(a)
        print(l3)
        
