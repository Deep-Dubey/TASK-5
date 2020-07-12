import pandas as pd

df=pd.read_csv("C:\\Users\\AKS\\Desktop\\MLOps_workspace\\access_log.csv")

df=df[['IP','Time']]

freq = {} 

for item in df['IP']: 

    if (item in freq): 

        freq[item] += 1

    else: 

        freq[item] = 1

key_list = list(freq.keys())  

val_list = list(freq.values()) 

def str_ip2_int(s_ip):

    lst = [int(item) for item in s_ip.split('.')]

    int_ip = lst[3] | lst[2] << 8 | lst[1] << 16 | lst[0] << 24

    return int_ip

j=0

for i in key_list:

   i=i.strip("[ -]")

   if i.split(".")[-1]=='':

   df['IP'][j]=(str_ip2_int(i))

   j=j+1

import matplotlib.pyplot as plt

plt.scatter(key_list,val_list)
import matplotlib.pyplot as plt

import ipaddress

import os

j=0

for i in df['freq']:

    if int(i)>=300:

        ip=ipaddress.ip_address(df['IP'][j]).__str__()

        with open('blocked_ip.txt','a+') as file:

            file.write(""+ip+"\n")

        file.close()

        plt.scatter(df['IP'][j],i,c='red')

    else:

        plt.scatter(df['IP'][j],i,c='green')

        j+=1


plt.show()
