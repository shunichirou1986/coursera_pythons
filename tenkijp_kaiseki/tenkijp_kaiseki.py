#-------------------------------------------------------------------------------
#  -*- coding: UTF-8 -*-
#Name:        module1
# Purpose:
#
# Author:      俊一郎
#
# Created:     22/07/2014
# Copyright:   (c) 俊一郎 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import xlrd,xlwt

def main():
    fname = "data.csv"#気象庁webからダウンロードしたcsvファイル
    L= []
    fpointer =  open(fname,'r')
    for line in fpointer:
        L.append(line.rstrip().split(","))#一ラインずつ読んでリストに格納する。”カンマ”区切り、右端の改行マーク削除
    fpointer.close()
    print L


if __name__ == '__main__':
    main()
