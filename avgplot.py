from pandas import read_csv
from pandas import DataFrame
from statistics import mean
import pandas as pd
from statistics import mean
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import cm
import math
import re
from fpdf import FPDF
import random
# from scipy import interpolate



data=read_csv("jeffin-6.csv",usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,36]).values.tolist()
data2=read_csv("jeffin-6.csv",usecols=[18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]).values.tolist()
# left
# print(data)
# temp=[]
for i in range(len(data)):
    temp=data[i][18]
    data[i][18]=data[i][0]
    data[i][0]=temp


for i in range(len(data2)):
    temp2=data2[i][18]
    data2[i][18]=data2[i][0]
    data2[i][0]=temp2

def removing(data,p):
    for i in range(p):
        data.pop(0)
    return data


counter=1
try:
    for i in range(len(data)):
        data[i][17]=counter
        if int(data[i][16])==3 and int(data[i+1][16])==0:
            # print(counter)
            counter=counter+1
except:
    print("EXCEPTION out of bound")
print(counter)
# print(data)


counter2=1
try:
    for i in range(len(data)):
        data2[i][17]=counter2
        if int(data2[i][16])==3 and int(data2[i+1][16])==0:
            # print(counter)
            counter2=counter2+1
except:
    print("EXCEPTION out of bound")

print(counter2)




for i in range(1,len(data)):
    data[i][11]=abs(data[i][11]-data[0][11])
for i in range(1,len(data2)):
    data2[i][11]=abs(data2[i][11]-data2[0][11])

p=0
for i in range(len(data)):
    if(data[i][17]==1):
        p=i+1
        # print("a")

left=removing(data,p)





p2=0
for i in range(len(data2)):
    if(data2[i][17]==1):
        p2=i+1
        # print("a")

right=removing(data2,p2)





data=data
name="test"

counter=0
try:
    for i in range(len(data)):
        data[i][17]=counter
        # print(data[i][17])

        if int(data[i][16])==3 and int(data[i+1][16]) ==0:
            counter=counter+1
            print(counter)
except:
    print("Exception occur")
#taking the fifteen and sixteen column
# print(data)

fifteen_col=[]
sixteen_col=[]


time=[]
ex=[]
ey=[]
ez=[]
accx=[]
accy=[]
accz=[]
time_final=[]
ex_final=[]
ey_final=[]
ez_final=[]
accx_final=[]
accy_final=[]
accz_final=[]
j=1

def plottingmap(time_final3,ex_final,ey_final,ez_final,accx_final,accy_final,accz_final,sixty_percent_final,counter,time_percent_total,index):
    print("@@@@@@@@@@@@@@@@@@####################")
    print("EX final")
    # print(ex_final)


    # plt.subplot(311)
    color=iter(cm.rainbow(np.linspace(0,1,10)))
    for i in range(counter-1):
        c=next(color)
        c=next(color)
        plt.ylim(-30, 30)
        print("length of EX")
        print(len(time_final3[i]))
        plt.plot(time_final3[i], ex_final[i],'-',c=c,label="stride"+str(i+1))




        # plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.title('Left FootAll angles are referenced with the ground)')
        plt.ylabel('toe in/out')

    plt.show()

    dataframelist = pd.DataFrame(ex_final)
    print("DFD")
    print(dataframelist)
    dataframelist_mean=dataframelist.mean(axis = 0, skipna = True)
    print(dataframelist_mean)
    plt.plot(time_final3[index], dataframelist_mean,'-',color="black",label="Stride Average")
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    lower_bound=dataframelist.min(axis = 0, skipna = True)
    upper_bound=dataframelist.max(axis = 0, skipna = True)
    plt.fill_between(time_final3[index], lower_bound, upper_bound, facecolor='blue', alpha=0.5,label='1 sigma range')


    plt.show()






sixty_percent=[]

# try:
for i in range(len(data)):
    if data[i][17]==j:
    # if int(data[i][17])>=2:
        if int(data[i][16])==2 and int(data[i+1][16])==3:
            ####finding a value of phase for 60%
            sixty_percent.append(data[i+1][0])
        if(j>=counter):
            break
        elif float(data[i][17])==j and float(data[i+1][17])==j+1:

            time_final.append(time)
            ex_final.append(ex)
            ey_final.append(ey)
            ez_final.append(ez)
            accx_final.append(accx)
            accy_final.append(accy)
            accz_final.append(accz)
            time=[]
            ex=[]
            ey=[]
            ez=[]
            accx=[]
            accy=[]
            accz=[]
            j+=1

        #360 is -1
        time.append(float(data[i][0]))
        # if float(data[i][1])<180:
        #     ex.append(math.radians(float(data[i][1])))
        # else:
        #     ex.append(math.radians(float(data[i][1])-360))
        ex.append(float(data[i][1]))
        ey.append(float(data[i][2]))
        ez.append(float(data[i][3]))
        accx.append(float(data[i][4]))
        accy.append(float(data[i][5]))
        accz.append(float(data[i][6]))

# except:
#     print("Exception2 occur")


print("########")
print("sixty percent")
print(sixty_percent)
print("EX final")
print(ex_final)
##########converting time into percentage
##time final is the list of the list in data

time_final3=[]
print("XXXXXXXXXXXLENGTH OF TIME")
print(len(time_final))
sixty_percent_final=[]
print("XXXXXXXXXXXLENGTH OF TIME")

for i in range(len(time_final)):
    # print(i)
    time_final2=[]
    for j in range(len(time_final[i])):
        time_final2.append((j/len(time_final[i]))*100)
        for k in range(len(sixty_percent)):
            if(time_final[i][j]==sixty_percent[k]):
                # print(sixty_percent[k])
                sixty_percent_final.append((j/len(time_final[i]))*100)
    time_final3.append(time_final2)
print("Sixty percent final")
print(sixty_percent_final)

#converting time into percent
time_percent_total=[]
for i in range(len(time_final3)):
    time_percent_per_cycle=[]
    for j in range(len(time_final3[i])):
        time_percent_per_cycle.append((j*100)/len(time_final3[i]))
    time_percent_total.append(time_percent_per_cycle)

largest=len(time_final3[0])
index=0
index
for i in range(len(time_final3)-1):
    # print(len(time_final3[i]))
    if len(time_final3[i])<len(time_final3[i+1]):
        largest=time_final3[i]
        index=i
print(len(time_final3[index]))

for i  in range(len(time_final3)):
    discard_remainder=len(time_final3[i])-len(time_final3[index])
    # print(discard_remainder)
    if len(time_final3[index])<=len(time_final3[i]):
        discard_remainder=len(time_final3[i])-len(time_final3[index])
        print("discard_remainder")
        print(discard_remainder)
        for j in range(discard_remainder):
            p=random.randint(2, len(time_final3[i])-5)
            time_final3[i].pop(p)
            ex_final[i].pop(p)
            ey_final[i].pop(p)
            ez_final[i].pop(p)



# print(largest)
# print(index)
print("TIMESSSS")
# print(time_percent_total)

for i in range(len(time_final3)):
    print(len(time_final3[i]))




plottingmap(time_final3,ex_final,ey_final,ez_final,accx_final,accy_final,accz_final,sixty_percent_final,counter,time_percent_total,index)
# plottingmap(time_final3,ey_final,"ey")
# plottingmap(time_final3,ez_final,"ez")
# plottingmap(time_final3,accx_final)
# plottingmap(time_final3,accy_final)
# plottingmap(time_final3,accz_final)
