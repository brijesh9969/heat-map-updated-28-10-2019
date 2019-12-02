from pandas import read_csv
from pandas import DataFrame
from statistics import mean
import intfinalspatial as ip
import leftgraph as lg
import rightgraph as rg

def data_read(datacsv,name,age,date,foot_length_left,foot_lenght_right,foot_width_left,foot_width_right,weight,walk_lenght,female,male):
    path=datacsv
    name=name
    age=age
    date=date
    foot_length_left=foot_length_left
    foot_lenght_right=foot_lenght_right
    foot_width_left=foot_width_left
    foot_width_right=foot_width_right
    weight=weight
    walk_lenght=walk_lenght
    female=female
    male=male
    print("Expecting path")
    left=[]
    right=[]
    #getting AND storing the data
    data=read_csv(path,usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,36]).values.tolist()
    data2=read_csv(path,usecols=[18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]).values.tolist()
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

    # for i in range(len(right)):
    #     # if(data[i][17]==1):
    #     print(right[i])



    # lg.generate_left(left,name)
    # rg.generate_right(right,name)
    return ip.generate(left,right,name,age,date,foot_length_left,foot_lenght_right,foot_width_left,foot_width_right,weight,walk_lenght,female,male)
