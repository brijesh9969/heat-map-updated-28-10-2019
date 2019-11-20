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


def generate_left(data,name):
    # pattern = re.compile("Timer")

    #getting AND storing the data
    # data=read_csv("./test_21_10_2019/jeffin_1/test_1_right.csv",usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]).values.tolist()
    # data=read_csv(data,usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]).values.tolist()
    data=data
    name=name

    # def removing(data,p):
    #     q=p+2
    #     for i in range(q):
    #         # pop.data[i]
    #         data.pop(0)
    #     return data


    # counter=0
    # for i in range(len(data)):
    #     for j in range(len(data[i])):
    #         # if(str(data[i][j])=='Timer'):
    #         p=0
    #         if(pattern.search(str(data[i][j]))):
    #
    #             # removing(i)
    #             counter+=1
    #
    #             p=i

    # print(counter)

    # data=removing(data,p)

    # print(data)




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
    # print(data)


    # for i in range(len(data)):
    #     fifteen_col.append(data[i][15])
    #     sixteen_col.append(data[i][16])
    #
    # #taking the fifteen and sixteen column
    # #
    # # print(fifteen_col)
    # # print(sixteen_col)
    #
    # final_list_ten = []
    #
    # for i in range(0, 10):
    #     max1 = 0
    #
    #     for j in range(len(fifteen_col)):
    #         if float(fifteen_col[j]) > max1:
    #             max1 = fifteen_col[j];
    #
    #     fifteen_col.remove(max1);
    #     final_list_ten.append(max1)


    #print(final_list_ten)
    #print(mean(final_list_ten))


    ##################################

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

    def plottingmap(time_final3,ex_final,ey_final,ez_final,accx_final,accy_final,accz_final,sixty_percent_final,counter):
        print("@@@@@@@@@@@@@@@@@@####################")
        # max_ex_final=max(ex_final)
        # print("max ex value")
        # print(max_ex_final)

        # plt.plot(time_final3[i], ex_final[i],'-',c=c,label="cycle"+str(i+1))4
        # plt.title('Left')
        print("EX final")
        print(ex_final)


        plt.subplot(311)
        color=iter(cm.rainbow(np.linspace(0,1,10)))
        for i in range(counter-1):
            c=next(color)
            c=next(color)
            plt.ylim(-30, 30)
            plt.plot(time_final3[i], ex_final[i],'-',c=c,label="cycle"+str(i+1))
            # for()
            x=[]
            y_sixty=[]

            #finding max of the each set for plotting a 60 percent line
            # max_ex_final=abs(min(ex_final[i]))
            # print("max Ex final")
            # print(math.ceil(max_ex_final))
            # # print(math.ceil(max_ex_final),-math.ceil(max_ex_final),-1)
            # for j in range(math.ceil(max_ex_final)):
            #     y_sixty.append(j)
            #
            # for j in range(math.ceil(max_ex_final)):
            #     x.append(sixty_percent_final[i])
            # print("okkkkkkkkkkkkkkkkk")
            # print(x)
            # print(y_sixty)
            # print("okkkkkkkkkkkkkkkkk")

            ###########
            # plt.plot(x,y_sixty,':',c=c)
            # plt.ylim(-30, 30)
            plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
            # plt.title('time (s) in percent')
            plt.title('Left Foot(All angles are referenced with the ground)')

            plt.ylabel('toe in/out')


        plt.subplot(312)
        color=iter(cm.rainbow(np.linspace(0,1,10)))
        for i in range(counter-1):
            c=next(color)
            c=next(color)
            # plt.ylim(-30, 30)
            plt.plot(time_final3[i], ey_final[i],'-',c=c,label="cycle"+str(i+1))
            # for()
            x=[]
            y_sixty=[]
            #finding max of the each set for plotting a 60 percent line
            max_ey_final=max(ey_final[i])
            print(math.ceil(max_ey_final))
            # plt.ylim(-30, 30)
            # for j in range(math.ceil(max_ey_final)):
            #     y_sixty.append(j)
            #
            # for j in range(math.ceil(max_ey_final)):
            #     x.append(sixty_percent_final[i])

            plt.plot(x,y_sixty,':',c=c)
            plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
            # plt.title('time (s) in percent')
            plt.ylabel('dorsi-planter flexion')

        plt.subplot(313)
        color=iter(cm.rainbow(np.linspace(0,1,10)))
        for i in range(counter-1):
            c=next(color)
            c=next(color)
            # plt.ylim(-30, 30)
            plt.plot(time_final3[i], ez_final[i],'-',c=c,label="cycle"+str(i+1))
            # for()
            x=[]
            y_sixty=[]
            #finding max of the each set for plotting a 60 percent line
            max_ez_final=max(ez_final[i])
            print(math.ceil(max_ez_final))
            # for j in range(math.ceil(max_ez_final)):
            #     y_sixty.append(j)
            #
            # for j in range(math.ceil(max_ez_final)):
            #     x.append(sixty_percent_final[i])

            plt.plot(x,y_sixty,':',c=c)
            plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
            plt.xlabel('Time (s) in percent')
            plt.ylabel('I/E rotation')
        file_name=name+" left leg.png"
        plt.savefig(file_name,dpi=200)
        plt.show()
        # plt.savefig('brijeshright7.png')

        # w = 4
        # h = 3
        # d = 70
        # plt.figure(figsize=(w, h), dpi=d)
        # plt.subplot(polar=True)
        # color=iter(cm.rainbow(np.linspace(0,1,10)))
        # for i in range(counter-1):
        #     c=next(color)
        #     c=next(color)
        #     plt.plot(ex_final[i],time_final3[i],c=c,label="cycle"+str(i+1))
        #     plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        #     # plt.show()
        # plt.show()



    # print("XXXXXXXXXXXXXXXXXXXXX MAX cycle")
    # max2=[]
    # for i in range(len(data)):
    #     max2.append(data[i][-1])
    # max3=max(max2)
    # print(max3)

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

    plottingmap(time_final3,ex_final,ey_final,ez_final,accx_final,accy_final,accz_final,sixty_percent_final,counter)
# plottingmap(time_final3,ey_final,"ey")
# plottingmap(time_final3,ez_final,"ez")
# plottingmap(time_final3,accx_final)
# plottingmap(time_final3,accy_final)
# plottingmap(time_final3,accz_final)
