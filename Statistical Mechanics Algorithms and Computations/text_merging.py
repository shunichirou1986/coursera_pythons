#coding: utf-8

import os
import sys
import fnmatch
import glob

def getdirs(path):#path�ɂ���f�B���N�g����S�������o���ă��X�g�Ɋi�[����֐�
     dirs=[]
     for item in os.listdir(path):
         if os.path.isdir(os.path.join(path,item)):
             dirs.append(item)
     return dirs

curdir = os.getcwd()#�J�����g�f�B���N�g�������擾
importdirs = getdirs(curdir)

for dir_now in importdirs:#importdirs�̂��ׂĂ̗v�f������������for���[�v
    print dir_now
    op_path = os.path.join(curdir,dir_now)#�������t�@�C���̃p�X
    for py_filename in glob.glob(os.path.join(op_path,"*.py")):#glob�ł����t�@�C���̃p�X���擾
        print '+++++++++++++++++++++' ,py_filename , '+++++++++++++++++++++'
        w = open(dir_now + '_merge.txt','a')#������t�@�C���̃I�[�v��
        py_Kugiri = '@@@@@@@@@@@@@@@@@@@@@@@@'+py_filename +'@@@@@@@@@@@@@@@@@@@@@@@@'#�t�@�C���l�[���Ԃ̎d�؂�
        w.write(py_Kugiri)
        for line in open(py_filename,'r'):
            w.write(line)

    w.close()
            