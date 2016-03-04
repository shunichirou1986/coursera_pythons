#coding:utf-8
#-------------------------------------------------------------------------------
# Name:        fastframe_analysis
# Purpose:  to get carriar drift time from fast frame analysis
#
# Author:      Shunichiro Watanabe
#
# Created:     19/11/2014
# Copyright:   (c) souken48 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy
import matplotlib
import sys
import os
import logging
import csv
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def main():
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename='analysis.log',level=logging.DEBUG)
    filename =sys.argv[1]#コマンドライン引数から処理ファイル名を取得
    print filename
    p_file = open(filename,'r')#コマンドライン引数から取得したファイルを読みこみ
    dataReader = csv.reader(p_file)#CSVリーダーでファイルを解析

    icount = 0
    nframecounts = 0
    nreccounts = 0
    aldatafframe = []
    lcsv_temp = []
    for row in dataReader:
        if icount == 0:
            recmax = int(row[1])#Record Length をstrからintに変換してから取得
        elif icount == 6:
            framemax = int(row[1])#Frame Counts をstrからintに変換してから取得
        icount = icount +1
        lcsv_temp.append([float(row[3]),float(row[4])])
    print recmax
    print framemax

    aldatafframe = zip(*[iter(lcsv_temp)]*recmax)#csvから読み込んだリストをrecmax置きに格納し直し
    print aldatafframe

####解析、ドリフト時間算出

##################グラフプロット
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for z in range(0,1):
        for i in range(0,recmax):
            xs.append(aldatafframe[z][i][0])
            print xs
            ys.append(aldatafframe[z][i][1])
            print ys

#        ax.scatter(xs, ys,zs=z, zdir='y')
　       if z%100 == 0:
            print u"残り%f",z/framemax
    ax.set_xlabel('time')
    ax.set_ylabel('counts')
    ax.set_zlabel('frame')

    plt.show()



if __name__ == '__main__':
    main()