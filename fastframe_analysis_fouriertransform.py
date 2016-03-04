#coding:utf-8
#-------------------------------------------------------------------------------
# Name:        fastframe_analysis
# Purpose:  to get carriar drift time from fast frame analysis
#
# Author:      Shunichiro Watanabe
#
# Created:     06/03/2015
# Copyright:   (c) souken48 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np
import matplotlib
import sys
import os
import logging
import csv
import matplotlib.pyplot as plt
import time
import scipy.signal

def update_progress(progress):
    print '\r[{0}] {1}%'.format('#'*(progress/10), progress)

def acquiredrifttime(xs,ys):
    #テンポラリー配列の初期化
    ndarr_temp = np.empty(1)
    #ペデスタルの平均値を算出(トップ)
    average_top = np.max(ys)#np.average(ys[100:])

    #ペデスタルの平均値を算出(アンダー)

    average_under = np.average(ys[10:100])

    #print average_top,average_under
    wave_height = average_top - average_under
#波高が小さすぎるときは棄却
##    if wave_height < 0.001:
##        continue
    ##立ち上がり時間の取得
    for i in reversed(range(0,xs.size)):
        if ys[i] < average_under + wave_height*0.05:

            time1 = xs[i]
            break


    for i in range(0,xs.size):
        if ys[i] > average_top - wave_height*0.05:
            time2 = xs[i]
            break

    drifttime = time2-time1
##    if drifttime < 0:#ドリフトタイムが負数の時は棄却
##        continue
    return(wave_height,drifttime,average_top,average_under,time1,time2)

def main():
#    logger = logging.getLogger(__name__)
    logging.basicConfig(filename='analysis.log',level=logging.DEBUG)
#    filename =sys.argv[1]#コマンドライン引数から処理ファイル名を取得
#####ファイルネームをハードコーディング
    filename='VB409-6_200V_137Cs000.csv'
    output_dir = u'ドリフト量検出'
    if not os.path.exists(output_dir): os.makedirs(output_dir)
    starttime = time.time()#開始時間を記録
    print filename
    p_file = open(filename,'r')#コマンドライン引数から取得したファイルを読みこみ
    if p_file==IOError:
        print "file not exists"
        logging.error("file not exists")
        sys.exit()
    dataReader = csv.reader(p_file)#CSVリーダーでファイルを解析

    icount = 0
    nframecounts = 0
    nreccounts = 0
    aldatafframe = []
    lcsv_temp = []
    xs = np.empty(1)#グラフ用X軸リスト
    ys = np.empty(1)#グラフ用Y軸リスト
    z=0#グラフ用Z軸ずらす
    ls_drifttimes = []#ドリフトタイム用リスト
    ls_wave_heights = []#波高値用リスト
    wave_height =0
    drifttime =0
    average_top=0
    average_under=0
    time1=0
    time2=0
    numbers = []
    data = []


    for row in dataReader:
        if icount == 0:
            recmax = int(row[1])#Record Length をstrからintに変換してから取得
        elif icount == 6:
            framemax = int(row[1])#Frame Counts をstrからintに変換してから取得
        icount = icount +1
        lcsv_temp.append([float(row[3]),float(row[4])])
    print u"レコード長%i" %recmax
    print u"フレーム数%i" %framemax

    nyq = recmax/2.0 #ナイキスト周波数

    fc = 10/nyq #カットオフ周波数
    numtaps = 11
    LPF_scipy = scipy.signal.firwin(numtaps,fc)


    for filecount in range(0,1):
        filename = "VB409-6_200V_137Cs00"+ str(filecount) +".csv"
        print filename
        logging.info('filename = %s' %filename)
##        if data==[]:
        data = np.loadtxt(filename,delimiter=',',usecols=(3,4))
##        else:
##            data_temp = np.loadtxt(filename,delimiter=',',usecols=(3,4))
##            data = np.vstack((data,data_temp))


        xs = data.T[0][0:recmax]
        for icount in range(0,framemax):

            ys = data.T[1][icount*recmax:icount*recmax+recmax]
    #        ys_fourier = np.fft.fft(ys)
            y_lpf = scipy.signal.lfilter(LPF_scipy,1,ys)
            wave_height,drifttime,average_top,average_under,time1,time2 = acquiredrifttime(xs,y_lpf)
            #波高値小さいモノは棄却
#            if wave_height < 0.00001:
#                break

##            print ys
##            print ys_fourier
            plt.subplot(211)
            plt.plot(xs*1000000,ys*1000)
#            plt.xlabel('time['+r'$\mu$'+'sec]')
            plt.ylabel('amplitude[mV]')
            plt.ylim(-5,100)
            plt.xlim(-10,10)

##            plt.subplot(312)
##            freq = np.fft.fftfreq(xs.shape[-1])
##            plt.plot(freq,ys_fourier.real,label='fft real part')
##            plt.plot(freq,ys_fourier.imag,label='fft imag part')
##            plt.plot(freq,abs(ys_fourier),label='fft abs')
##            plt.xlabel('frequency')
##            plt.ylabel('Amplitude')
##            plt.legend()
            plt.subplot(212)
            plt.plot(xs*1000000,y_lpf*1000)
            plt.xlabel('time['+r'$\mu$'+'sec]')
            plt.ylabel('amplitude[mV]')
            plt.ylim(-5,100)
            plt.xlim(-10,10)
            plt.axvline(x=time1*1000000,color='red',linestyle='-')
            plt.axvline(x=time2*1000000,color='green',linestyle='-')
            plt.axhline(y=average_top*1000,color='green',linestyle='-')
            plt.axhline(y=average_under*1000,color='red',linestyle='-')
            plt.text((time2+time2*0.1)*1000000,(average_top+wave_height*0.1)*1000,'WH = '+str(round(wave_height*1000,5))+' mV '+'dtime = '+str(round(drifttime*1000000,5))+r'$\mu$'+'sec',fontsize=9)
            #for counts in range(recmax):
            x_drift = [drifttime]*recmax
#            plt.plot(x_drift,y_lpf)

#        plt.show()
    #画像の保存

            plt.savefig(os.path.join(output_dir,str(filecount)+'_' +'%04d.png' % icount))
            plt.cla()
            plt.close()
            numbers.append(icount)
            ls_drifttimes.append(drifttime)
            ls_wave_heights.append(wave_height)

            if icount %100 == 0:
                sys.stderr.write(str(icount/framemax*100) +'%')
                sys.stderr.flush()

    savedata = np.array([numbers,ls_drifttimes,ls_wave_heights])
    np.savetxt(filename+"waveheightvsdrifttime.csv", savedata.T,delimiter=",",header="No.,drift time,wave height")


    endtime = time.time()
    totaltime = (endtime-starttime)/60
    logging.info('totaltime = %s'%totaltime)
    print 'total time = ' ,str(totaltime),' min'




if __name__ == '__main__':
    main()