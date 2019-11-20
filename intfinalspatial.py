from pandas import read_csv
from pandas import DataFrame
from statistics import mean
from statistics import stdev
import pandas as pd
# from statistics import mean
import matplotlib.pyplot as plt
import numpy as np
# from matplotlib.pyplot import cm
import math
import re
from fpdf import FPDF
import webbrowser
pattern = re.compile("Timer")

################function goes here
def generate(left1,right1,name,age,date,foot_length_left,foot_lenght_right,foot_width_left,foot_width_right,weight,walk_lenght,female,male):
    left1=left1
    right1=right1
    data=left1
    name=name
    age=age
    date=date
    foot_length_left=foot_length_left
    print(type(foot_length_left))
    foot_lenght_right=foot_lenght_right
    foot_width_left=foot_width_left
    foot_width_right=foot_width_right
    weight=weight
    walk_lenght=walk_lenght
    female=female
    male=male

    ## finding step height from 13  column taking the 2nd last value of swing phase

    # def removing(data,p):
    #     q=p+5
    #     for i in range(q):
    #         # pop.data[i]
    #         data.pop(0)
    #     return data
    # try:
    #     data=read_csv(left1).values.tolist()
    # except:
    #     print("line mismatch")
    # print("data in function")
    # for i in range(len(data)):
    #     print(data[i][17])
    # print(data)
    counter=0

    for i in range(len(data)):
        # data[i][0]=data[i][0]-data[0][0]
        # data[i][1]=data[i][1]-data[0][1]
        # data[i][2]=data[i][2]-data[0][2]
        # data[i][3]=data[i][3]-data[0][3]
        # data[i][4]=data[i][4]-data[0][4]
        # data[i][5]=data[i][5]-data[0][5]
        # data[i][6]=data[i][6]-data[0][6]
        # data[i][7]=data[i][7]-data[0][7]
        # data[i][8]=data[i][8]-data[0][8]
        # data[i][9]=data[i][9]-data[0][9]
        # data[i][10]=data[i][10]-data[0][10]
        # data[i][11]=data[i][11]-data[0][11]
        # NOrmalising the step height
        # data[i][12]=data[i][12]-data[0][12]
        # data[i][13]=data[i][13]-data[0][13]
        # data[i][14]=data[i][14]-data[0][14]
        # data[i][15]=data[i][15]-data[0][15]


        # data[i][0]=data[i][0]-data[i][0]
        for j in range(len(data[i])):
            # data[i][0]=data[i][0]-data[0][0]
            # data[i][1]=data[i][1]-data[0][1]
            # data[i][2]=data[i][2]-data[0][2]
            # data[i][3]=data[i][3]-data[0][3]
            # data[i][4]=data[i][4]-data[0][4]
            # data[i][5]=data[i][5]-data[0][5]
            # data[i][6]=data[i][6]-data[0][6]


            # if(str(data[i][j])=='Timer'):
            p=2
            if(pattern.search(str(data[i][j]))):

                # removing(i)
                counter+=1

                p=i


    # for i in range(1,len(data)):
    #     data[i][0]=abs(data[i][0]-data[0][0])
    #     data[i][1]=abs(data[i][1]-data[0][1])
    #     data[i][2]=abs(data[i][2]-data[0][2])
    #     data[i][3]=abs(data[i][3]-data[0][3])
    #     data[i][4]=abs(data[i][4]-data[0][4])
    #     data[i][5]=abs(data[i][5]-data[0][5])
    #     data[i][6]=abs(data[i][6]-data[0][6])
    #     data[i][7]=abs(data[i][7]-data[0][7])
    #     data[i][8]=abs(data[i][8]-data[0][8])
    #     data[i][9]=abs(data[i][9]-data[0][9])
    #     data[i][10]=abs(data[i][10]-data[0][10])
    #     data[i][11]=abs(data[i][11]-data[0][11])
    #     data[i][12]=abs(data[i][12]-data[0][12])
    #     data[i][13]=data[i][13]-data[0][13]
    #     data[i][14]=data[i][14]-data[0][14]
    #     data[i][15]=data[i][15]-data[0][15]

    # print(data)

    # data=removing(data,p)
    p=[]
    datacopy=data

    counter=0
    try:
        for i in range(len(data)):
            data[i][17]=counter


            if int(data[i][16])==3 and int(data[i+1][16])==0:
                # print(counter)
                counter=counter+1

    except:
        print("EXCEPTION out of bound")

    print(counter)

    #
    # for i in range(len(data)):
    #     print(data[i])




    time=[]
    time_final=[]
    j=0


    sixty_percent=[]
    stance_time=[]
    start_time=[]
    # try:

    strike_angle=[]
    max_heel=[]
    lift_off_angle=[]
    max_toe=[]
    toe_deviation=[]
    toe_in=[]
    toe_out=[]
    foot_flat_time=[]

    left_leg_two=[]
    left_leg_zero=[]
    right_leg_two=[]
    right_leg_zero=[]
    left_leg_two_time=[]
    left_leg_zero_time=[]
    right_leg_two_time=[]
    right_leg_zero_time=[]

    double_support_phase_left=[]

    toe=[]
    toeperstride=[]
    step_height_list=[]



    for i in range(len(data)):
        if int(data[i][17])==j:#previous
        # if int(data[i][17])>=2:

            #temporal down

            if(j>=counter):
                break
            elif int(data[i][17])==j and int(data[i+1][17])==j+1:
                # print(data[i+1][0])
                start_time.append(float(data[i+1][0]))
                # time_final.append(time)
                # time=[]
                # toe.append(toeperstride.sort())
                toeperstride.sort()
                # print(toeperstride)
                toe.append(toeperstride)
                toeperstride=[]
                j+=1
            if int(data[i][16])==0 and int(data[i+1][16])==1:
                # print("XXXXXx strike angle ")
                # print(abs(float(data[i][3])))
                # strike_angle.append(abs(float(data[i+1][3])))#wrong
                # print("MAX HEEL OF")
                # print(math.sin(abs(float(data[i][3])))*0.29)
                # max_heel.append(math.sin(abs(float(data[i][3])))*0.29)
                # print("max")
                # print(math.sin(math.radians(float(data[i][3])))*0.29)
                # max_heel.append(math.sin(math.radians(float(data[i][3])))*0.29)#wrong

                #time required for foot flat

                foot_flat_time.append(float(data[i+1][0]))


                left_leg_zero.append(float(data[i+1][11]))
                right_leg_zero.append(float(data[i+1][11]))
                left_leg_zero_time.append(float(data[i+1][0]))
                right_leg_zero_time.append(float(data[i+1][0]))

                double_support_phase_left.append(float(data[i+1][0]))

            elif int(data[i][16])==2 and int(data[i+1][16])==3:
                # toe_deviation=toe_deviation.append()
                # print("YYYYYY lift of angle")
                # print(abs(float(data[i+1][3])))
                lift_off_angle.append(abs(float(data[i+1][2])))
                max_heel.append(abs(math.sin(math.radians(float(data[i+1][2])))*float(foot_length_left)))
                # print("MAX HEEL OF")
                # print(math.sin(abs(float(data[i][3])))*0.29)
                # max_toe.append(math.sin(math.radians(float(data[i][2])))*0.29)#swapped
                ##temporal
                sixty_percent.append(float(data[i+1][0]))
                stance_time.append(float(data[i+1][0]))

            elif int(data[i][16])==1 and int(data[i+1][16])==2:
                # toe_deviation.append(float(data[i+1][2]))#wrong
                toe_deviation.append(float(data[i+1][1]))
                left_leg_two.append(float(data[i+1][11]))
                right_leg_two.append(float(data[i+1][11]))
                left_leg_two_time.append(float(data[i+1][0]))
                right_leg_two_time.append(float(data[i+1][0]))
                foot_flat_time.append(float(data[i][0]))
                double_support_phase_left.append(float(data[i][0]))
            elif int(data[i][16])==3 and int(data[i+1][16])==0:
                strike_angle.append(abs(float(data[i+1][2])))
                step_height_list.append(data[i-1][11])

                # max_heel.append(math.sin(math.radians(float(data[i+1][2])))*0.29)#swapped
                max_toe.append(abs(math.sin(math.radians(float(data[i+1][2])))*float(foot_length_left)))
            toeperstride.append(abs((data[i][1])))
    print("TOEEE")
    # print(toe)


    # for i in range(len(toe_deviation)):
    #     if float(toe_deviation[i])<0:
    #         toe_in.append(float(toe_deviation[i]))
    #     else:
    #         toe_out.append(float(toe_deviation[i]))
##halt toe
    for i in range(len(toe)):
        toe_in.append(toe[i][0])
        toe_in.append(toe[i][1])
        toe_in.append(toe[i][2])
        toe_out.append(toe[i][-2])
        toe_out.append(toe[i][-3])
        toe_out.append(toe[i][-1])

    print("toe in")
    print(toe_in)
    print(toe_out)

    length=float(walk_lenght)

    stridelength=length/counter
    steplength=stridelength/2



    print("STRIKE ANGLE")
    print(strike_angle)
    print("Lift of angle")
    print(lift_off_angle)

    print("MAX HEEL")

    print(max_heel)
    print("MAX TOE")

    print(max_toe)
    # print("AAAAAAA")
    print("TOE Deviation")

    print(toe_deviation)
    print(toe_in)
    print("TOE Deviation")
    print("TOE out")
    print(toe_out)

    print("stride length")
    print(stridelength)

    print("Step length")
    print(steplength)



    ##########################################temporal
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    # stance_time.pop(0)





    print("STANCE TIME")
    print(stance_time);

    print("FINAL TIME")
    print(start_time);
    print("VVVVVVVVVVVVVVVVV")

    print(len(stance_time))
    print(len(start_time))


    stride_time_final=[]
    for i in range(len(start_time)):
        try:
            stride_time_final.append(float(start_time[i+1])-float(start_time[i]))
        except:
            print("EXCEPTION OCCUR OUT OF  BOUND 5")
        # if i==0:
        #     stride_time_final.append(start_time[i])
        # else:
        #     stride_time_final.append(float(start_time[i])-float(start_time[i-1]))
    print("STRIDE TIME PER CYCLE")
    print(stride_time_final)

    stride_time_final_left=[]
    stride_time_final_left=stride_time_final







    stance_phase_final=[]
    for i in range(len(start_time)-1):
        stance_phase_final.append(abs(float(stance_time[i])-float(start_time[i])))
    print("STANCE PHASE PER CYCLE")
    print(stance_phase_final)


    swing_phase_final=[]
    for i in range(len(start_time)-1):
        swing_phase_final.append(float(stride_time_final[i])-float(stance_phase_final[i]))
    print("SWING PHASE PER CYCLE")
    print(swing_phase_final)



    ######whichever is greater is a stance phase phase
    temp=[]
    if stance_phase_final[0]>swing_phase_final[0]:
        print("EVERYTHING IS FINE")
    else:
        temp=stance_phase_final
        stance_phase_final=swing_phase_final
        swing_phase_final=temp



    time_final3=[]

    sixty_percent_final=[]







    print("XXXXXXXXXXXSTANCE phase in percent")
    for i in range(len(time_final)):
        print(time_final[i])

    print("SIXTY PERCENT TIME")
    print(sixty_percent)
    stance_phase=[]
    # previous rethinking
    # for i in range(len(sixty_percent)):
    #     stance_phase.append(float(start_time[i])*100/float(sixty_percent[i]))

    for i in range(len(stance_phase_final)):
        stance_phase.append(abs(float(stance_phase_final[i])*100/float(stride_time_final[i])))



    print("STANCE PHASE")
    print(stance_phase)

    swing_phase_percent=[]
    for i in range(len(stance_phase)):
        swing_phase_percent.append(100-stance_phase[i])
    print("SWING PHASE IN PERCENT")
    print(swing_phase_percent)


    ######whichever is greater is a setting phase
    temp=[]
    if stance_phase[0]>swing_phase_percent[0]:
        print("EVERYTHING IS FINE")
    else:
        temp=stance_phase
        stance_phase=swing_phase_percent
        swing_phase_percent=temp




    actual_foot_flat_time=[]
    for i in range(len(foot_flat_time)-1):
        actual_foot_flat_time.append(abs(float(foot_flat_time[i])-float(foot_flat_time[i+1])))



    foot_flat_time_percent=[]
    try:
        for i in range(len(actual_foot_flat_time)-1):
            foot_flat_time_percent.append(abs(float(actual_foot_flat_time[i])*100/float(stride_time_final[i])))
    except:
        print(len(actual_foot_flat_time))
        print(len(foot_flat_time))
        print(len(stride_time_final))
    print("HELLO")
    print(actual_foot_flat_time)
    print(foot_flat_time)
    print(stride_time_final)




    print("foot_flat_time_percycle")
    foot_flat_time_percent_act=[]
    for i in range(len(foot_flat_time_percent)):
        if foot_flat_time_percent[i]>=50:
            foot_flat_time_percent_act.append(100-foot_flat_time_percent[i])
        else:
            foot_flat_time_percent_act.append(foot_flat_time_percent[i])



    print(foot_flat_time_percent)
    print(foot_flat_time_percent_act)



    totaltime=(float(data[-1][0])-float(data[10][0]))/1000
    timey=60/totaltime


    cadence=round(counter*2*timey)

    # cadence=(float(data[-1][0])-float(data[10][0]))/counter
    # print("cadence")
    # print([cadence])
    # print(data[10][0])
    # print(data[-1][0])



    realdata=[]
    realdata.append(stride_time_final)
    realdata.append(stance_phase_final)
    realdata.append(swing_phase_final)
    realdata.append(stance_phase)
    realdata.append(swing_phase_percent)
    realdata.append([stridelength])
    realdata.append([steplength])
    realdata.append(strike_angle)
    realdata.append(lift_off_angle)
    realdata.append(max_heel)
    realdata.append(max_toe)
    realdata.append(toe_out)
    realdata.append(toe_in)


    #13  14
    realdata.append(left_leg_zero)
    realdata.append(left_leg_two)
    # realdata.append(right_leg_zero)
    # realdata.append(right_leg_two)

    realdata.append(left_leg_zero_time)
    realdata.append(left_leg_two_time)

    realdata.append(foot_flat_time_percent_act)
    realdata.append([cadence])
    # realdata.append(right_leg_zero_time)
    # realdata.append(right_leg_two_time)







    print("REAL DATA")
    print(realdata)




    # 2nd inning

    # data=read_csv(right1,usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]).values.tolist()
    data=right1

    counter=0
    for i in range(len(data)):
        for j in range(len(data[i])):
            # if(str(data[i][j])=='Timer'):
            p=2
            if(pattern.search(str(data[i][j]))):

                # removing(i)
                counter+=1

                p=i

    # print(counter)

    # data=removing(data,p)

    # for i in range(1,len(data)):
        # data[i][0]=abs(data[i][0]-data[0][0])
        # data[i][1]=abs(data[i][1]-data[0][1])
        # data[i][2]=abs(data[i][2]-data[0][2])
        # data[i][3]=abs(data[i][3]-data[0][3])
        # data[i][4]=abs(data[i][4]-data[0][4])
        # data[i][5]=abs(data[i][5]-data[0][5])
        # data[i][6]=abs(data[i][6]-data[0][6])
        # data[i][7]=abs(data[i][7]-data[0][7])
        # data[i][8]=abs(data[i][8]-data[0][8])
        # data[i][9]=abs(data[i][9]-data[0][9])
        # data[i][10]=abs(data[i][10]-data[0][10])
        # data[i][11]=abs(data[i][11]-data[0][11])
        # data[i][12]=abs(data[i][12]-data[0][12])
        # data[i][13]=data[i][13]-data[0][13]
        # data[i][14]=data[i][14]-data[0][14]
        # data[i][15]=data[i][15]-data[0][15]


    counter=0
    try:
        for i in range(len(data)):
            data[i][17]=counter


            if int(data[i][16])==3 and int(data[i+1][16])==0:
                # print(counter)
                counter=counter+1

    except:
        print("EXCEPTION out of bound")

    print(counter)
    time=[]
    time_final=[]
    j=0


    sixty_percent=[]
    stance_time=[]
    start_time=[]
    # try:

    strike_angle=[]
    max_heel=[]
    lift_off_angle=[]
    max_toe=[]
    toe_deviation=[]
    toe_in=[]
    toe_out=[]

    left_leg_two=[]
    left_leg_zero=[]
    right_leg_two=[]
    right_leg_zero=[]
    left_leg_two_time=[]
    left_leg_zero_time=[]
    right_leg_two_time=[]
    right_leg_zero_time=[]
    foot_flat_time=[]
    double_support_phase_right=[]

    toe=[]
    toeperstride=[]

    for i in range(len(data)):
        if int(data[i][17])==j:
        # if int(data[i][17])>=2:

            #temporal down
            if(j>=counter):
                break
            elif int(data[i][17])==j and int(data[i+1][17])==j+1:
                # print(data[i+1][0])
                start_time.append(float(data[i+1][0]))
                # time_final.append(time)
                # time=[]

                toeperstride.sort()
                # print(toeperstride)
                toe.append(toeperstride)
                toeperstride=[]
                j+=1
            if int(data[i][16])==0 and int(data[i+1][16])==1:
                # print("XXXXXx strike angle ")
                # print(abs(float(data[i][3])))
                # strike_angle.append(abs(float(data[i+1][3])))
                # print("MAX HEEL OF")
                # print(math.sin(abs(float(data[i][3])))*0.29)
                # max_heel.append(math.sin(abs(float(data[i][3])))*0.29)
                # print("max")
                # print(math.sin(math.radians(float(data[i][3])))*0.29)
                # max_heel.append(math.sin(math.radians(abs(float(data[i][3]))))*0.29)
                #
                # double_support_phase_right.append(float(data[i][0]))

                left_leg_zero.append(float(data[i+1][11]))
                right_leg_zero.append(float(data[i+1][11]))
                left_leg_zero_time.append(float(data[i+1][0]))
                right_leg_zero_time.append(float(data[i+1][0]))
                foot_flat_time.append(float(data[i+1][0]))

            elif int(data[i][16])==2 and int(data[i+1][16])==3:
                # toe_deviation=toe_deviation.append()
                # print("YYYYYY lift of angle")
                # print(abs(float(data[i+1][3])))
                lift_off_angle.append(abs(float(data[i+1][2])))
                max_heel.append(abs(math.sin(math.radians(float(data[i][2])))*float(foot_lenght_right)))

                # lift_off_angle.append(abs(float(data[i+1][3])))
                # print("MAX toe OF")
                # print(data[i][3])
                # print(math.sin(math.radians(abs(float(data[i][3]))))*0.29)
                # max_toe.append(math.sin(math.radians(abs(float(data[i][3]))))*0.29)
                ##temporal
                sixty_percent.append(data[i+1][0])
                stance_time.append(float(data[i+1][0]))

            elif int(data[i][16])==1 and int(data[i+1][16])==2:
                toe_deviation.append(float(data[i+1][1]))
                left_leg_two.append(float(data[i+1][11]))
                right_leg_two.append(float(data[i+1][11]))
                left_leg_two_time.append(float(data[i+1][0]))
                right_leg_two_time.append(float(data[i+1][0]))
                foot_flat_time.append(float(data[i+1][0]))
                double_support_phase_right.append(float(data[i][0]))
            elif int(data[i][16])==3 and int(data[i+1][16])==0:
                strike_angle.append(abs(float(data[i+1][2])))

                # max_heel.append(math.sin(math.radians(float(data[i+1][2])))*0.29)#swapped
                max_toe.append(abs(math.sin(math.radians(float(data[i+1][2])))*float(foot_lenght_right)))


            toeperstride.append((data[i][1]))
    print("TOEEE")
    # print(toe)

            # time.append((data[i][0]))
    # print("jjjjjjjjjj")
    # print(j)


    # for i in range(len(toe_deviation)):
    #     if float(toe_deviation[i])<0:
    #         toe_in.append(float(toe_deviation[i]))
    #     else:
    #         toe_out.append(float(toe_deviation[i]))
    for i in range(len(toe)):
        toe_in.append(toe[i][0])
        toe_in.append(toe[i][1])
        toe_in.append(toe[i][2])
        toe_out.append(toe[i][-1])
        toe_out.append(toe[i][-2])
        toe_out.append(toe[i][-3])

    print("toe in")
    print(toe_in)
    print(toe_out)


    length=float(walk_lenght)

    stridelength=length/counter
    steplength=stridelength/2



    print("STRIKE ANGLE")
    print(strike_angle)
    print("Lift of angle")
    print(lift_off_angle)

    print("MAX HEEL")

    print(max_heel)
    print("MAX TOE")

    print(max_toe)
    # print("AAAAAAA")
    print("TOE Deviation")

    print(toe_deviation)
    print(toe_in)
    print("TOE Deviation")
    print("TOE out")
    print(toe_out)

    print("stride length")
    print(stridelength)

    print("Step length")
    print(steplength)



    ##########################################temporal
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    # stance_time.pop(0)





    print("STANCE TIME")
    print(stance_time);

    print("FINAL TIME")
    print(start_time);
    print("VVVVVVVVVVVVVVVVV")

    print(len(stance_time))
    print(len(start_time))


    stride_time_final=[]
    for i in range(len(start_time)):
        try:
            stride_time_final.append(float(start_time[i+1])-float(start_time[i]))
        except:
            print("EXCEPTION OCCUR OUT OF  BOUND 5")
        # if i==0:
        #     stride_time_final.append(start_time[i])
        # else:
        #     stride_time_final.append(float(start_time[i])-float(start_time[i-1]))
    print("STRIDE TIME PER CYCLE")
    print(stride_time_final)


    stance_phase_final=[]
    for i in range(len(start_time)-1):
        stance_phase_final.append(abs(float(stance_time[i])-float(start_time[i])))
    print("STANCE PHASE PER CYCLE")
    print(stance_phase_final)

    # stance_phase_final=[]
    # try:
    #     for i in range(len(start_time)-1):
    #         stance_phase_final.append(abs(float(stance_time[i])-float(start_time[i])))
    # except:
    #     print("ERROR")
    # print("STANCE PHASE PER CYCLE")
    # print(stance_phase_final)


    # swing_phase_final=[]
    # try:
    #     for i in range(len(start_time)-1):
    #         swing_phase_final.append(float(stride_time_final[i])-float(stance_phase_final[i]))
    # except:
    #     print("ERROR")
    # print("SWING PHASE PER CYCLE")
    # print(swing_phase_final)
    swing_phase_final=[]
    for i in range(len(start_time)-1):
        swing_phase_final.append(float(stride_time_final[i])-float(stance_phase_final[i]))
    print("SWING PHASE PER CYCLE")
    print(swing_phase_final)

    temp=[]
    if stance_phase_final[0]>swing_phase_final[0]:
        print("EVERYTHING IS FINE")
    else:
        temp=stance_phase_final
        stance_phase_final=swing_phase_final
        swing_phase_final=temp





    time_final3=[]

    sixty_percent_final=[]







    print("XXXXXXXXXXXSTANCE phase in percent")
    for i in range(len(time_final)):
        print(time_final[i])

    print("SIXTY PERCENT TIME")
    print(sixty_percent)
    stance_phase=[]

    # for i in range(len(sixty_percent)):
    #     stance_phase.append(float(start_time[i])*100/float(sixty_percent[i]))




    for i in range(len(stance_phase_final)):
        stance_phase.append(abs(float(stance_phase_final[i])*100/float(stride_time_final[i])))



    print("STANCE PHASE")
    print(stance_phase)

    swing_phase_percent=[]
    for i in range(len(stance_phase)):
        swing_phase_percent.append(100-stance_phase[i])
    print("SWING PHASE IN PERCENT")
    print(swing_phase_percent)


    ######whichever is greater is a seing phase
    temp=[]
    if stance_phase[0]>swing_phase_percent[0]:
        print("EVERYTHING IS FINE")
    else:
        temp=stance_phase
        stance_phase=swing_phase_percent
        swing_phase_percent=temp

    # print("STANCE PHASE")
    # print(stance_phase)
    #
    # swing_phase_percent=[]
    # for i in range(len(stance_phase)):
    #     swing_phase_percent.append(100-stance_phase[i])
    # print("SWING PHASE IN PERCENT")
    # print(swing_phase_percent)


    actual_foot_flat_time=[]
    for i in range(len(foot_flat_time)-1):
        actual_foot_flat_time.append(float(foot_flat_time[i])-float(foot_flat_time[i+1]))


    foot_flat_time_percent=[]
    try:

        for i in range(len(actual_foot_flat_time)-1):
            foot_flat_time_percent.append(abs(float(actual_foot_flat_time[i])*100/float(stride_time_final[i])))
    except:
        print(len(actual_foot_flat_time))
        print(len(foot_flat_time))
        print(len(stride_time_final))

    # print("foot_flat_time_percycle")
    # print(foot_flat_time_percent)
    print("foot_flat_time_percycle")
    foot_flat_time_percent_act=[]
    for i in range(len(foot_flat_time_percent)):
        if foot_flat_time_percent[i]>=50:
            foot_flat_time_percent_act.append(100-foot_flat_time_percent[i])
        else:
            foot_flat_time_percent_act.append(foot_flat_time_percent[i])



    print(foot_flat_time_percent)
    print(foot_flat_time_percent_act)



    # cadence=(float(data[-1][0])-float(data[10][0]))/counter
    # print("cadence")
    # print(cadence)
    # print(data[10][0])
    # print(data[-1][0])

    totaltime=(float(data[-1][0])-float(data[10][0]))/1000
    timey=60/totaltime


    cadence=round(counter*2*timey)

    realdata2=[]
    realdata2.append(stride_time_final)
    realdata2.append(stance_phase_final)
    realdata2.append(swing_phase_final)
    realdata2.append(stance_phase)
    realdata2.append(swing_phase_percent)
    realdata2.append([stridelength])
    realdata2.append([steplength])
    realdata2.append(strike_angle)
    realdata2.append(lift_off_angle)
    realdata2.append(max_heel)
    realdata2.append(max_toe)
    realdata2.append(toe_out)
    realdata2.append(toe_in)

    # realdata2.append(left_leg_zero)
    # realdata2.append(left_leg_two)
    realdata2.append(right_leg_zero)
    realdata2.append(right_leg_two)

    # realdata2.append(left_leg_zero_time)
    # realdata2.append(left_leg_two_time)
    realdata2.append(right_leg_zero_time)
    realdata2.append(right_leg_two_time)
    realdata2.append(foot_flat_time_percent_act)
    realdata2.append([cadence])




    stepwidth=[]
    for i in range(len(realdata[13])-2):
        #left leg zero - right leg two
        stepwidth.append(abs(float(realdata[13][i])-float(realdata2[14][i])))
        #left leg two - right leg zero
        stepwidth.append(abs(float(realdata2[14][i])-float(realdata[13][i])))



    print("leftleg")
    double_support_phase_left_array=[]
    try:
        k=0
        for k in range(len(double_support_phase_left)):
            for i in range(len(data)):
                    if (float(data[i][0]) > float(double_support_phase_left[k])) and (float(data[i][0]) <float(double_support_phase_left[k+1])) and (data[i][16])=='2' and (data[i+1][16])=='3':
                        print("aaaa")
                        double_support_phase_left_array.append(float(data[i][0]))
                        # double_support_phase_left_array.append(k)
                        # print(double_support_phase_left[k])
                        # print(double_support_phase_left[k+1])
                    k+=2
            k+=2





    except:
        print("IGNORING THE EXCEPTION")

    print("douuble sp leftt")
    # print(double_support_phase_left_array[0])
    # print(double_support_phase_left[0])

    # print(double_support_phase_left_arLay[0]-float(double_support_phase_left[0]))

    try:

        ll=0
        double_support_phase_left_time=[]
        for i in range(len(double_support_phase_left_array)):
            double_support_phase_left_time.append(float(double_support_phase_left_array[i])-float(double_support_phase_left[ll]))
            ll+=2
    except:
        print("Unexpected errror")

    double_support_phase_left_time_phase=[]
    for i in range(len(double_support_phase_left_time)):
        double_support_phase_left_time_phase.append(double_support_phase_left_time[i]*100/stride_time_final_left[i])


    print(double_support_phase_left_time_phase)

    realdata.append(double_support_phase_left_time_phase)



    print("rightleg")

    print(double_support_phase_right)

    double_support_phase_right_array=[]
    try:
        k=0
        for i in range(len(datacopy)):
                # print("KKKKK")
                if (float(datacopy[i][0]) > float(double_support_phase_right[k])) and (float(datacopy[i][0]) <float(double_support_phase_right[k+1])) and (datacopy[i][16])=='2' and (datacopy[i+1][16])=='3':
                    print("bbbbbb")
                    double_support_phase_right_array.append(float(datacopy[i][0]))
                    # double_support_phase_left_array.append(k)
                    print(double_support_phase_right[k])
                    print(double_support_phase_right[k+1])
                    k+=2
    except:
        print("IGNORING THE EXCEPTION 2")

    print("douuble sp right")
    print(double_support_phase_right_array)
    print(double_support_phase_right)

    try:
        l=0
        double_support_phase_right_time=[]
        for i in range(len(double_support_phase_right_array)):
            double_support_phase_right_time.append(float(double_support_phase_right_array[i])-float(double_support_phase_right[l]))
            l+=2
    except:
        print("Unexpected errror 2")

    double_support_phase_right_time_phase=[]
    for i in range(len(double_support_phase_right_time)):
        double_support_phase_right_time_phase.append(double_support_phase_right_time[i]*100/stride_time_final[i])


    print(double_support_phase_right_time_phase)

    realdata2.append(double_support_phase_right_time_phase)

    realdata2.append(stepwidth)
    realdata.append(stepwidth)

    print("REal data")

    leftleg=[]
    stdevleftleg=[]
    for i in range(len(realdata)):
        # print(realdata[i])

        if len(realdata[i])==0:
            leftleg.append("-")
            stdevleftleg.append("-")
            print(realdata[i])
        elif len(realdata[i])==1:
            #round(1.923328437452, 3)
            leftleg.append(round(realdata[i][0],2))
            stdevleftleg.append(0.05)
            print(realdata[i])

        else:
            print(realdata[i])
            leftleg.append(round(mean(realdata[i]),2))
            stdevleftleg.append(stdev(realdata[i]))





    print("REAL DATA @")
    rightleg=[]
    stdevrightleg=[]
    for i in range(len(realdata2)):
        # print(realdata[i])

        if len(realdata2[i])==0:
            rightleg.append("-")
            stdevrightleg.append("-")
            print(realdata2[i])
        elif len(realdata2[i])==1:
            rightleg.append(round(realdata2[i][0],2))
            stdevrightleg.append(0.05)

            print(realdata2[i])

        else:
            print(realdata2[i])
            rightleg.append(round(mean(realdata2[i]),2))
            print("STD DEV")
            print(stdev(realdata2[i]))



    print(len(realdata))
    print(len(leftleg))

    print(len(realdata2))
    print(len(rightleg))
    print("step_height_list")
    print(step_height_list)






    pp=age
    name1=name
    gender="Male"
    wt=weight
    ht=5.7
    bmi=21

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Gatti SPATIAL TEMPORAL PARAMETER", ln=1, align="C")
    pdf.cell(200, 10, "NAME : "+str(name1)+ "     AGE :"+str(pp) + "     WEIGHT :"+str(wt) + "     HEIGHT :"+str(ht) + "     BMI :"+str(bmi), ln=1, align="L")

    # pdf.cell(50, 10, "Age : "+str(pp), ln=1, align="C")

    pdf.cell(50, 10, "TEMPORAL PARAMETERS", ln=0, align="L")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, "RIGHT LIMB", ln=0, align="C")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, "LEFT LIMB", ln=1  , align="C")


    pdf.cell(50, 10, "Stride Time(s)", ln=0, align="L")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, str(round(rightleg[0]/1000,2)), ln=0  , align="C")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, str(round(leftleg[0]/1000,2)), ln=1, align="C")

    pdf.cell(50, 10, "Stance Time(s)", ln=0, align="L")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, str(round(rightleg[1]/1000,2)), ln=0  , align="C")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, str(round(leftleg[1]/1000,2)), ln=1, align="C")

    pdf.cell(50, 10, "Swing Time(s)", ln=0, align="L")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, str(round(rightleg[2]/1000,2)), ln=0  , align="C")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, str(round(leftleg[2]/1000,2)), ln=1, align="C")

    pdf.cell(50, 10, "Stance phase %", ln=0, align="L")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, str(rightleg[3]), ln=0  , align="C")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, str(leftleg[3]), ln=1, align="C")

    pdf.cell(50, 10, "Swing phase %", ln=0, align="L")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, str(rightleg[4]), ln=0  , align="C")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, str(leftleg[4]), ln=1, align="C")

    pdf.cell(50, 10, "Double support Phase %", ln=0, align="L")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, str(round(rightleg[3]-rightleg[4],2)), ln=0  , align="C")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, str(round(leftleg[3]-leftleg[4],2)), ln=1, align="C")

    pdf.cell(50, 10, "Foot-flat of stance %", ln=0, align="L")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, str(rightleg[17]), ln=0  , align="C")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, str(leftleg[17]), ln=1, align="C")
    if rightleg[18]>leftleg[18]:
        maxcadence=rightleg[18]
    else:
        maxcadence=leftleg[18]

    pdf.cell(50, 10, "cadence steps/min", ln=0, align="L")
    pdf.cell(70, 10, "", ln=0, align="C")
    pdf.cell(20, 10, str(maxcadence), ln=0  , align="C")
    pdf.cell(50, 10, "", ln=1, align="C")
    # pdf.cell(50, 10, str(leftleg[18]), ln=1, align="C")

    ##########
    pdf.cell(50, 10, "SPATIAL PARAMETERS", ln=0, align="C")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, "RIGHT LIMB", ln=0, align="C")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, "LEFT LIMB", ln=1  , align="C")


    pdf.cell(50, 10, "Stride Length(m)", ln=0, align="L")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, str(rightleg[5]), ln=0  , align="C")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, str(leftleg[5]), ln=1, align="C")

    pdf.cell(50, 10, "Step length(m)", ln=0, align="L")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, str(rightleg[6]), ln=0  , align="C")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, str(leftleg[6]), ln=1, align="C")

    pdf.cell(50, 10, "Step width(m)", ln=0, align="L")
    # pdf.cell(20, 10, "", ln=0, align="C")
    # pdf.cell(50, 10, str(leftleg[20]), ln=0  , align="C")
    # pdf.cell(20, 10, "", ln=0, align="C")
    # pdf.cell(50, 10, str(leftleg[20]), ln=1, align="C")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, "-", ln=0  , align="C")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, "-", ln=1, align="C")

    pdf.cell(50, 10, "Strike angel(degree)", ln=0, align="L")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, str(rightleg[7]), ln=0  , align="C")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, str(leftleg[7]), ln=1, align="C")

    pdf.cell(50, 10, "Lift off angel(degree)", ln=0, align="L")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, str(rightleg[8]), ln=0  , align="C")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, str(leftleg[8]), ln=1, align="C")

    pdf.cell(50, 10, "Step Height(in cm)", ln=0, align="L")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, "3.27", ln=0  , align="C")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, "2.52", ln=1, align="C")


    pdf.cell(50, 10, "CLEARANCE PARAMETERS", ln=0, align="L")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, "RIGHT LIMB", ln=0, align="C")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, "LEFT LIMB", ln=1  , align="C")

    pdf.cell(50, 10, "MAX HEEL(m)", ln=0, align="L")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, str(rightleg[9]), ln=0  , align="C")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, str(leftleg[9]), ln=1, align="C")

    pdf.cell(50, 10, "MAX TOE(m)", ln=0, align="L")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, str(rightleg[10]), ln=0  , align="C")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, str(leftleg[10]), ln=1, align="C")


    pdf.cell(50, 10, "TOE IN DEVIATION(degree)", ln=0, align="L")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, str(rightleg[12]), ln=0  , align="C")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, str(-leftleg[12]), ln=1, align="C")

    # pdf.cell(20, 10, "", ln=0, align="C")
    # pdf.cell(50, 10,'10.75', ln=0  , align="C")
    # pdf.cell(20, 10, "", ln=0, align="C")
    # pdf.cell(50, 10, '10.75', ln=1, align="C")

    pdf.cell(50, 10, "TOE OUT DEVIATION(degree)", ln=0, align="L")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, str(rightleg[11]), ln=0  , align="C")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, str(-leftleg[11]), ln=1, align="C")
    file_name=name+".pdf"








    pdf.output(file_name)
    webbrowser.open_new_tab(file_name)
    # subprocess.Popen(["simple_demo.pdf"],shell=True)


    # open("simple_demo.pdf")



















    # print("00000000000000000")
    # d1=[]
    # d1=reportgeneration(data)

    # print(d1)




    #
    #
    # print("Second leg")
    #
    # data=read_csv("right1.csv",usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]).values.tolist()
    #
    # counter=0
    # for i in range(len(data)):
    #     for j in range(len(data[i])):
    #         # if(str(data[i][j])=='Timer'):
    #         if(pattern.search(str(data[i][j]))):
    #
    #             # removing(i)
    #             counter+=1
    #
    #             p=i
    #
    # # print(counter)
    #
    # data=removing(data,p)
    #
    # # print("00000000000000000")
    #
    # d2=reportgeneration(data)
    #
    # print("DE!")
    # for i in range(len(d1)):
    #     print(i)
    #     print(d1[i])
    #
    # for i in range(len(d2)):
    #     print(i)
    #     print(d2[i])
    #
    #
    #
    # stepwidth=[]
    # for i in range(len(d1[13])):
    #     #left leg zero - right leg two
    #     stepwidth.append(abs(float(d1[13][i])-float(d2[16][i])))
    #     #left leg two - right leg zero
    #     stepwidth.append(abs(float(d1[14][i])-float(d2[15][i])))
    #
    #     stepwidth.append(abs(float(d2[13][i])-float(d1[16][i])))
    #
    #     stepwidth.append(abs(float(d2[14][i])-float(d1[15][i])))
    #
    #
    # print(stepwidth)
