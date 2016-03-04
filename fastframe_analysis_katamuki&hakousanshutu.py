#coding:utf-8
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      souken48
#
# Created:     04/02/2015
# Copyright:   (c) souken48 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np

import matplotlib.pyplot as plt
import os.path

curdir='C:\Users\souken48\Desktop'
filename='C:\Users\souken48\Documents\python\PreAmpOutput_NamaPulse_Test.csv'
data = np.loadtxt(filename,delimiter=',')

#print data.T[0],data.T[1]

for t in range(1,data.ndim):
    ####解析、ドリフト時間算出
    ###波高値の算出

    #テンポラリー配列の初期化
    ndarr_temp = np.empty(1)
    #ペデスタルの平均値を算出(トップ)
    average_top = np.average(data.T[1][-100:])

    #テンポラリー配列の初期化
    ndarr_temp = np.empty(1)
    #ペデスタルの平均値を算出(トップ)

    average_under = np.average(data.T[1][:100])

    #print average_top,average_under
    wave_height = average_top - average_under

    ####立ち上がり時間の取得
    for i in range(0,data.T[0].size)[::-1]:
        if data.T[1][i] < wave_height*0.06:

            time1 = data.T[0][i]
            break


    for i in range(i,data.size):
        if data.T[1][i] > wave_height*0.94:
            time2 = data.T[0][i]
            break

    plt.rcParams['font.size']=10
    #plt.figure(figsize=(4,3),facecolor='white')
    #plt.subplots_adjust(left=0.125,bottom=0.125)
    plt.plot(data.T[0],data.T[1],'-',label='voltage vs time')
    plt.xlabel('Voltage[mV]',fontsize=10)
    plt.ylabel('time',fontsize=10)
    plt.yscale('linear')
    plt.legend(loc='best',prop={'size':7})
    plt.text(0,0," time1 = "+str(time1)+" time2 = "+str(time2)+"wave height = "+str(wave_height),color='r', size="14", style="oblique")
    plt.axvline(x=time1,color='red')
    plt.axvline(x=time2,color='red')
    plt.axhline(y=average_top,color='red')
    plt.axhline(y=average_under,color='red')

    plt.show()

    #plt.savefig(filename+'.png')