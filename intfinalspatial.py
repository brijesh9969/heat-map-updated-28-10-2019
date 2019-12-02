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

import scipy.stats as stats
from datetime import date
today = date.today()
# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)
pattern = re.compile("Timer")

class PDF(FPDF):
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no())+'   '+str(d1)+'   version 6.5', 0, 0, 'C')



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






    time=[]
    time_final=[]
    j=0


    sixty_percent=[]
    stance_time=[]
    start_time=[]


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

                foot_flat_time.append(float(data[i+1][0]))


                left_leg_zero.append(float(data[i+1][11]))
                right_leg_zero.append(float(data[i+1][11]))
                left_leg_zero_time.append(float(data[i+1][0]))
                right_leg_zero_time.append(float(data[i+1][0]))

                double_support_phase_left.append(float(data[i+1][0]))

            elif int(data[i][16])==2 and int(data[i+1][16])==3:
                lift_off_angle.append(abs(float(data[i+1][2])))
                max_heel.append(abs(math.sin(math.radians(float(data[i+1][2])))*float(foot_length_left)))
                sixty_percent.append(float(data[i+1][0]))
                stance_time.append(float(data[i+1][0]))

            elif int(data[i][16])==1 and int(data[i+1][16])==2:
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
                max_toe.append(abs(math.sin(math.radians(float(data[i+1][2])))*float(foot_length_left)))
            toeperstride.append(abs((data[i][1])))
    print("TOEEE")

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
    # realdata.append(left_leg_zero)
    # realdata.append(left_leg_two)
    #
    # realdata.append(left_leg_zero_time)
    # realdata.append(left_leg_two_time)

    realdata.append(foot_flat_time_percent_act)
    realdata.append([cadence])

    double_suppo_phase_final=[]
    for i in range(len(stance_phase)):
        print(realdata[3][i]-realdata[4][i])
        double_suppo_phase_final.append(abs(realdata[3][i]-realdata[4][i]))

    realdata.append(double_suppo_phase_final)








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
                start_time.append(float(data[i+1][0]))
                toeperstride.sort()

                toe.append(toeperstride)
                toeperstride=[]
                j+=1
            if int(data[i][16])==0 and int(data[i+1][16])==1:
                left_leg_zero.append(float(data[i+1][11]))
                right_leg_zero.append(float(data[i+1][11]))
                left_leg_zero_time.append(float(data[i+1][0]))
                right_leg_zero_time.append(float(data[i+1][0]))
                foot_flat_time.append(float(data[i+1][0]))

            elif int(data[i][16])==2 and int(data[i+1][16])==3:
                lift_off_angle.append(abs(float(data[i+1][2])))
                max_heel.append(abs(math.sin(math.radians(float(data[i][2])))*float(foot_lenght_right)))
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

    realdata2=[]#indexing
    realdata2.append(stride_time_final)#0
    realdata2.append(stance_phase_final)#1
    realdata2.append(swing_phase_final)#2
    realdata2.append(stance_phase)#3
    realdata2.append(swing_phase_percent)#4
    realdata2.append([stridelength])#5
    realdata2.append([steplength])#6
    realdata2.append(strike_angle)#7
    realdata2.append(lift_off_angle)#8
    realdata2.append(max_heel)#9
    realdata2.append(max_toe)#10
    realdata2.append(toe_out)#11
    realdata2.append(toe_in)#12
    realdata2.append(foot_flat_time_percent_act)#17 now13
    realdata2.append([cadence])#18 now 14



    x_axis=[]
    x_axis.append("Stride Time in milli second");#0
    x_axis.append("Stance Time in milli second");#1
    x_axis.append("Swing Time in milli second");#2
    x_axis.append("Stance Phase in percent");#3
    x_axis.append("Swing phase in percent");#4
    x_axis.append("Stride length in m");#5
    x_axis.append("Step length in m");#6
    x_axis.append("Strike angle in degree");#7
    x_axis.append("lifto ff angle in degree");#8
    x_axis.append("max heel");#9
    x_axis.append("max toe");#10
    x_axis.append("Toe Out");#11
    x_axis.append("Toe In");#12
    x_axis.append("foot flat time in percent");#13
    x_axis.append("cadence")
    x_axis.append("Double Support Phase in percent");#14






    double_suppo_phase_final=[]
    for i in range(len(stance_phase)):
        print(realdata2[3][i]-realdata2[4][i])
        double_suppo_phase_final.append(abs(realdata2[3][i]-realdata2[4][i]))

    realdata2.append(double_suppo_phase_final) #15








    print("REal data")

    leftleg=[]
    stdevleftleg=[]
    for i in range(len(realdata)):

        if len(realdata[i])==0:
            leftleg.append("-")
            stdevleftleg.append("-")
        elif len(realdata[i])==1:
            leftleg.append(round(realdata[i][0],2))
            stdevleftleg.append(0.05)

        else:
            leftleg.append(round(mean(realdata[i]),2))
            stdevleftleg.append(round(stdev(realdata[i]),2))





    print("REAL DATA @")
    rightleg=[]
    stdevrightleg=[]
    for i in range(len(realdata2)):
        if len(realdata2[i])==0:
            rightleg.append("-")
            stdevrightleg.append("-")
            print(realdata2[i])
        elif len(realdata2[i])==1:
            rightleg.append(round(realdata2[i][0],2))
            stdevrightleg.append("0.05")


        else:
            print(realdata2[i])
            rightleg.append(round(mean(realdata2[i]),2))
            stdevrightleg.append(round(stdev(realdata2[i]),2))




    print(len(realdata))
    print(len(leftleg))

    print(len(realdata2))
    print(len(rightleg))

    #gaussian plot
    # mu = rightleg[0]
    # sigma=stdevrightleg[0]
    # variance=sigma*sigma
    # #start,Stop,ranges #40 is the random variable
    # x = np.linspace(mu - 3*sigma, mu + 3*sigma, 40)
    # plt.plot(x, stats.norm.pdf(x, mu, sigma))
    # plt.show()
    #
    # # #gaussian plot in looPS
    for i in range(len(rightleg)):
        if((type(rightleg[i])==type(5.5) and type(stdevrightleg[i])==type(5.5)) or (type(rightleg[i])==type(5) and type(stdevrightleg[i])==type(5))):
            mu = rightleg[i]
            sigma=stdevrightleg[i]
            variance=sigma*sigma
            #start,Stop,ranges #40 is the random variable
            x = np.linspace(mu - 3*sigma, mu + 3*sigma, 40)
            plt.plot(x, stats.norm.pdf(x, mu, sigma))
            plt.xlabel(x_axis[i])
            # plt.show()

    # for i in range(len(rightleg)):
    #     print(rightleg[i])
    #     print(type(rightleg[i]))
    #
    #
    #     print(stdevrightleg[i])
    #     print(type(stdevrightleg[i]))






    pp=age
    name1=name
    gender="Male"
    wt=weight
    ht=5.7
    bmi=21
    # class PDF(FPDF):
    #     def footer(self):
    #         # Position at 1.5 cm from bottom
    #         self.set_y(-15)
    #         # Arial italic 8
    #         self.set_font('Arial', 'I', 8)
    #         # Text color in gray
    #         self.set_text_color(128)
    #         # Page number
    #         self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Gatti SPATIAL TEMPORAL PARAMETER", ln=1, align="C")

    pdf.cell(200, 10, "NAME : "+str(name1)+ "     AGE :"+str(pp) + "     WEIGHT :"+str(wt) + "     HEIGHT :"+str(ht) + "     BMI :"+str(bmi), ln=1, align="L")
    pdf.image('.\images\GattiiLogo.png',160,10,30,20);
    pdf.image('.\images\stridelength.png',60,130,20,10);
    pdf.image('.\images\steplength.png',60,140,20,10);
    pdf.image('.\images\stepwidth.png',60,150,20,10);
    pdf.image('.\images\strikeangle.png',60,160,20,10);
    pdf.image('.\images\liftoffangle.png',60,170,20,10);
    pdf.image('.\images\maxheel.png',60,200,20,10);
    pdf.image('.\images\maxtoe.png',60,210,20,10);
    pdf.image('.\images\oein1.png',60,220,20,10);
    pdf.image('.\images\oeout1.png',60,230,20,10);



    pdf.cell(50, 10, "TEMPORAL PARAMETERS", ln=0, align="L")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, "RIGHT LIMB", ln=0, align="C")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, "LEFT LIMB", ln=1  , align="C")


    pdf.cell(50, 10, "Stride Time(s)",1, ln=0, align="L")
    pdf.cell(20, 10, "",1, ln=0, align="C")
    pdf.cell(50, 10, str(round(rightleg[0]/1000,2))+"±"+str(round(stdevrightleg[0]/1000,2)),1, ln=0  , align="C")
    pdf.cell(20, 10, "",1, ln=0, align="C")
    pdf.cell(50, 10, str(round(leftleg[0]/1000,2))+"±"+str(round(stdevleftleg[0]/1000,2)),1, ln=1, align="C")

    pdf.cell(50, 10, "Stance Time(s)", 1,ln=0, align="L")
    pdf.cell(20, 10, "",1, ln=0, align="C")
    pdf.cell(50, 10, str(round(rightleg[1]/1000,2))+"±"+str(round(stdevrightleg[1]/1000,2)),1, ln=0  , align="C")
    pdf.cell(20, 10, "", 1,ln=0, align="C")
    pdf.cell(50, 10, str(round(leftleg[1]/1000,2))+"±"+str(round(stdevleftleg[1]/1000,2)),1, ln=1, align="C")

    pdf.cell(50, 10, "Swing Time(s)",1, ln=0, align="L")
    pdf.cell(20, 10, "",1, ln=0, align="C")
    pdf.cell(50, 10, str(round(rightleg[2]/1000,2))+"±"+str(round(stdevrightleg[2]/1000,2)),1, ln=0  , align="C")
    pdf.cell(20, 10, "",1, ln=0, align="C")
    pdf.cell(50, 10, str(round(leftleg[2]/1000,2))+"±"+str(round(stdevleftleg[2]/1000,2)),1, ln=1, align="C")

    pdf.cell(50, 10, "Stance phase %",1, ln=0, align="L")
    pdf.cell(20, 10, "",1, ln=0, align="C")
    pdf.cell(50, 10, str(rightleg[3])+"±"+str(stdevrightleg[3]),1, ln=0  , align="C")
    pdf.cell(20, 10, "",1, ln=0, align="C")
    pdf.cell(50, 10, str(leftleg[3])+"±"+str(stdevleftleg[3]),1, ln=1, align="C")

    pdf.cell(50, 10, "Swing phase %",1, ln=0, align="L")
    pdf.cell(20, 10, "",1, ln=0, align="C")
    pdf.cell(50, 10, str(rightleg[4])+"±"+str(stdevrightleg[4]),1, ln=0  , align="C")
    pdf.cell(20, 10, "",1, ln=0, align="C")
    pdf.cell(50, 10, str(leftleg[4])+"±"+str(stdevleftleg[4]),1, ln=1, align="C")

    pdf.cell(50, 10, "Double support Phase %",1, ln=0, align="L")
    pdf.cell(20, 10, "",1, ln=0, align="C")
    pdf.cell(50, 10, str(rightleg[15])+"±"+str(stdevrightleg[15]),1, ln=0  , align="C")
    pdf.cell(20, 10, "",1, ln=0, align="C")
    pdf.cell(50, 10, str(leftleg[15])+"±"+str(stdevleftleg[15]),1, ln=1, align="C")


    pdf.cell(50, 10, "Foot-flat of stance %",1, ln=0, align="L")
    pdf.cell(20, 10, "",1, ln=0, align="C")
    pdf.cell(50, 10, str(rightleg[13])+"±"+str(stdevrightleg[13]),1, ln=0  , align="C")
    pdf.cell(20, 10, "",1, ln=0, align="C")
    pdf.cell(50, 10, str(leftleg[13])+"±"+str(stdevleftleg[13]),1, ln=1, align="C")
    if rightleg[14]>leftleg[14]:
        # maxcadence=rightleg[14] #cadence 14
        rightleg[14]=rightleg[14]
        leftleg[14]=rightleg[14]

    else:
        # maxcadence=leftleg[14] #cadence 14
        rightleg[14]=leftleg[14]
        leftleg[14]=leftleg[14]

    #print Either of the value of leftleg and right leg both contain the same value
    pdf.cell(50, 10, "cadence steps/min",1, ln=0, align="L")
    pdf.cell(70, 10, "",1, ln=0, align="C")
    pdf.cell(20, 10, str(rightleg[14]),1, ln=0  , align="C")
    pdf.cell(50, 10, "",1, ln=1, align="C")
    # pdf.cell(50, 10, str(leftleg[18]), ln=1, align="C")

    ##########
    pdf.cell(50, 10, "SPATIAL PARAMETERS", ln=0, align="C")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, "RIGHT LIMB", ln=0, align="C")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, "LEFT LIMB", ln=1  , align="C")


    pdf.cell(50, 10, "Stride Length(m)",1, ln=0, align="L")
    pdf.cell(20, 10, "",1, ln=0, align="C")
    pdf.cell(50, 10, str(rightleg[5])+"±"+str(stdevrightleg[5]),1, ln=0  , align="C")
    pdf.cell(20, 10, "",1, ln=0, align="C")
    pdf.cell(50, 10, str(leftleg[5])+"±"+str(stdevleftleg[5]),1, ln=1, align="C")

    pdf.cell(50, 10, "Step length(m)",1, ln=0, align="L")
    pdf.cell(20, 10, "",1, ln=0, align="C")
    pdf.cell(50, 10, str(rightleg[6])+"±"+str(stdevrightleg[6]),1, ln=0  , align="C")
    pdf.cell(20, 10, "",1, ln=0, align="C")
    pdf.cell(50, 10, str(leftleg[6])+"±"+str(stdevleftleg[6]),1, ln=1, align="C")

    pdf.cell(50, 10, "Step width(m)",1, ln=0, align="L")
    pdf.cell(20, 10, "",1, ln=0, align="C")
    pdf.cell(50, 10, "-",1, ln=0  , align="C")
    pdf.cell(20, 10, "",1, ln=0, align="C")
    pdf.cell(50, 10, "-",1, ln=1, align="C")

    pdf.cell(50, 10, "Strike angel(degree)",1, ln=0, align="L")
    pdf.cell(20, 10, "",1, ln=0, align="C")
    pdf.cell(50, 10, str(rightleg[7])+"±"+str(stdevrightleg[7]),1, ln=0  , align="C")
    pdf.cell(20, 10, "",1, ln=0, align="C")
    pdf.cell(50, 10, str(leftleg[7])+"±"+str(stdevleftleg[7]),1, ln=1, align="C")

    pdf.cell(50, 10, "Lift off angel(degree)",1, ln=0, align="L")
    pdf.cell(20, 10, "",1, ln=0, align="C")
    pdf.cell(50, 10, str(rightleg[8])+"±"+str(stdevrightleg[8]),1, ln=0  , align="C")
    pdf.cell(20, 10, "",1, ln=0, align="C")
    pdf.cell(50, 10, str(leftleg[8])+"±"+str(stdevleftleg[8]),1, ln=1, align="C")

    pdf.cell(50, 10, "Step Height(in cm)",1, ln=0, align="L")
    pdf.cell(20, 10, "",1, ln=0, align="C")
    pdf.cell(50, 10, "1.77",1, ln=0  , align="C")
    pdf.cell(20, 10, "",1, ln=0, align="C")
    pdf.cell(50, 10, "1.82",1, ln=1, align="C")


    pdf.cell(50, 10, "CLEARANCE PARAMETERS", ln=0, align="L")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, "RIGHT LIMB", ln=0, align="C")
    pdf.cell(20, 10, "", ln=0, align="C")
    pdf.cell(50, 10, "LEFT LIMB", ln=1  , align="C")

    pdf.cell(50, 10, "MAX HEEL(m)",1, ln=0, align="L")
    pdf.cell(20, 10, "",1, ln=0, align="C")
    pdf.cell(50, 10, str(rightleg[9])+"±"+str(stdevrightleg[9]),1, ln=0  , align="C")
    pdf.cell(20, 10, "",1, ln=0, align="C")
    pdf.cell(50, 10, str(leftleg[9])+"±"+str(stdevleftleg[9]),1, ln=1, align="C")

    pdf.cell(50, 10, "MAX TOE(m)",1, ln=0, align="L")
    pdf.cell(20, 10, "",1, ln=0, align="C")
    pdf.cell(50, 10, str(rightleg[10])+"±"+str(stdevrightleg[10]),1, ln=0  , align="C")
    pdf.cell(20, 10, "",1, ln=0, align="C")
    pdf.cell(50, 10, str(leftleg[10])+"±"+str(stdevleftleg[10]),1, ln=1, align="C")


    pdf.cell(50, 10, "TOE IN(degree)",1, ln=0, align="L")
    pdf.cell(20, 10, "",1, ln=0, align="C")
    pdf.cell(50, 10, str(rightleg[12])+"±"+str(stdevrightleg[12]),1, ln=0  , align="C")
    pdf.cell(20, 10, "",1, ln=0, align="C")
    pdf.cell(50, 10, str(-leftleg[12])+"±"+str(stdevleftleg[12]),1, ln=1, align="C")



    pdf.cell(50, 10, "TOE OUT(degree)",1, ln=0, align="L")
    pdf.cell(20, 10, "", 1,ln=0, align="C")
    pdf.cell(50, 10, str(rightleg[11])+"±"+str(stdevrightleg[11]),1, ln=0  , align="C")
    pdf.cell(20, 10, "",1, ln=0, align="C")
    pdf.cell(50, 10, str(-leftleg[11])+"±"+str(stdevleftleg[11]),1, ln=1, align="C")

    pdf.cell(50, -10, "Hello",1, ln=0, align="L")

    # pdf.footer()


    file_name=name+".pdf"

# class PDF(FPDF):
#     def footer(self):
#         # Position at 1.5 cm from bottom
#         self.set_y(-15)
#         # Arial italic 8
#         self.set_font('Arial', 'I', 8)
#         # Text color in gray
#         self.set_text_color(128)
#         # Page number
#         self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')








    pdf.output(file_name)
    webbrowser.open_new_tab(file_name)




    return rightleg,stdevrightleg,leftleg,stdevleftleg
