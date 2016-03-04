#coding: utf-8

import os
import sys
import fnmatch
import glob

def getdirs(path):#pathにあるディレクトリを全部抜き出してリストに格納する関数
     dirs=[]
     for item in os.listdir(path):
         if os.path.isdir(os.path.join(path,item)):
             dirs.append(item)
     return dirs

curdir = os.getcwd()#カレントディレクトリ名を取得
importdirs = getdirs(curdir)

for dir_now in importdirs:#importdirsのすべての要素を一つ一つ分解してforループ
    print dir_now
    op_path = os.path.join(curdir,dir_now)#統合元ファイルのパス
    for py_filename in glob.glob(os.path.join(op_path,"*.py")):#globでｐｙファイルのパスを取得
        print '+++++++++++++++++++++' ,py_filename , '+++++++++++++++++++++'
        w = open(dir_now + '_merge.txt','a')#統合先ファイルのオープン
        py_Kugiri = '@@@@@@@@@@@@@@@@@@@@@@@@'+py_filename +'@@@@@@@@@@@@@@@@@@@@@@@@'#ファイルネーム間の仕切り
        w.write(py_Kugiri)
        for line in open(py_filename,'r'):
            w.write(line)

    w.close()
            