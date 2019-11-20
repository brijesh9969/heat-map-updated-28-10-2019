import serial
from serial import Serial
import time
import csv
import numpy as np
name1=input("enter a file name :")
name=name1+".csv"
ser=serial.Serial("COM4",115200)#left
ser1=serial.Serial("COM5",115200)#right
f=open(name,"w")
c=0
while True:       
        read=ser.readline().decode("utf-8").split("\r")#left
        read1=ser1.readline().decode("utf-8").split("\r")#right
        f.write(str(read[1]))
        f.write(",")
        f.write(str(read1[1]))
        f.write(",")
        f.write(str(c))
        f.write("\n")
        c+=25
        print(read,"--" ,read1)
    
