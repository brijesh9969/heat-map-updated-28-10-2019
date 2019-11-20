from pandas import read_csv
import threading
import time
import os
import numpy as np
def reading():
    f=open("fsr_video_value.csv","w")
    data=read_csv("fsr.csv",usecols = [4,5,6,7,8,9])
    data.to_csv('file1.csv') 
    fsr_value=read_csv("file1.csv")
    fsr=fsr_value.values.tolist()
    print(len(fsr))
    reading=np.array(fsr)
    for i in range(len(reading)-2):
        time.sleep(1.5)
        print(reading[i])
        
    
     
    
    
reading()

#def reading1():
  #  print("threading example")
#t1=threading.Thread(target=reading)
#t2=threading.Thread(target=reading1)
#t1.start()
#t2.start()
#t2.join()
