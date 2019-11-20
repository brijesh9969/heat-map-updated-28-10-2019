import serial
from serial import Serial
import time
import csv
import numpy as np
name1=input("enter a file name :")
name=name1+".csv"
ser=serial.Serial("COM12",115200)
f=open(name,"w")
c=0
while True:       
        read=ser.readline().decode("utf-8").split("\r")
        f.write(str(read[1]))
        f.write(",")
        f.write(str(c))
        f.write("\n")
        c+=1
        print(read)
    
