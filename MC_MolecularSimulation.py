#----------------------------------------　---------------------------------------
#  -*- coding: UTF-8 -*-
#Name:        MC_MolecularSimulation
# Purpose:モンテカルロ法を用いた結晶生成のシミュレーション
#
# Author:      俊一郎
#
# Created:     03/07/2014
# Copyright:   (c) 俊一郎 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random,math,os,pylab

################################################################################
#定数宣言
img = 0#描画関数内部で使う変数
COLORS = ['r', 'b', 'g', 'orange']#描画関数で使う色
L = []#剛体円の座標を格納するリスト
N = 1000#粒子個数
TOTAL_PARTICLE_DENSITY = 3.3E-5
sigma_sq = TOTAL_PARTICLE_DENSITY /(math.pi * N )#密度および粒子個数から計算した粒子半径（二乗）
sigma = math.sqrt(sigma_sq)#粒子サイズ
print sigma
delta = 0.05 #MC一回毎の移動距離
n_steps =1000 #粒子を動かす回数
accept_ratio =0.0#移動が許容された回数
temperature  = 100 #系の温度、吸着エネルギーを計算する時に用いる
prob_join = 500/temperature
output_dir = 'bimolecular_interaction'#出力先のフォルダ


################################################################################
#距離を算出する関数(周期的境界条件）
def dist(x,y):
    d_x = abs(x[0] - y[0]) % 1.0
    d_x = min(d_x, 1.0 - d_x)
    d_y = abs(x[1] - y[1]) % 1.0
    d_y = min(d_y, 1.0 - d_y)
    return  (d_x**2 + d_y**2)

################################################################################
#MC法による粒子の移動と接触判定、結合位置への移動
def mc_bonding(M,N):
    b = [M[0] + random.uniform(-delta, delta), M[1] + random.uniform(-delta, delta),'r']
    for c in N   :#全ての粒子との接触判定
        if c !=M:
           if dist(b,c) < 4.0 * sigma_sq :#もし他の粒子と衝突orめり込んだ場合,接触する位置まで移動させる
              M[0] = 2*sigma *(M[0]-c[0])/math.sqrt((c[0]-M[0])**2 + (c[1]-M[1])**2)
              M[1] = 2*sigma *(M[1]-c[1])/math.sqrt((c[0]-M[0])**2 + (c[1]-M[1])**2)
              M[2] = 'b'
              c[2] = 'b'

    if M[2] != 'b':M[:] = [b[0]%1.0,b[1]%1.0,'r']#上の接触判定を全て行って、どれとも結合していなければ、乱数振った移動先に移動させる。
    return M

################################################################################
#描画する関数：吸着しているやつは色変えたいな
def snapshot(pos,steps):
    global img
    pylab.subplots_adjust(left=0.10, right=0.90, top=0.90, bottom=0.10)
    pylab.gcf().set_size_inches(6, 6)
    pylab.axis([0, 1, 0, 1])
    pylab.setp(pylab.gca(), xticks=[0, 1], yticks=[0, 1])
    for (x, y, c) in pos:
        for ix in range(-1,2):
            for iy in range(-1,2):
                circle = pylab.Circle((x + ix, y + iy), radius=sigma, fc=c)
                pylab.gca().add_patch(circle)
    pylab.savefig(os.path.join(output_dir, '%04d.png' % steps), transparent=False)
    pylab.close()
    img += 1
    pylab.show

def show_conf(M, sigma, title, fname):#周期的境界条件用
    pylab.axes()
    pylab.clf()
    for [x, y] in M:
        for ix in range(-1, 2):
            for iy in range(-1, 2):
                cir = pylab.Circle((x + ix, y + iy), radius = sigma,  fc = 'r')
                pylab.gca().add_patch(cir)
    pylab.axis('scaled')
    pylab.title(title)
    pylab.axis([0.0, 1.0, 0.0, 1.0])
    pylab.savefig(fname)
#    pylab.show()
################################################################################
#初期配置決め関数（ダイレクトサンプリング）
def initialize_direct(N):
    initialize_flag = False#初期化時に用いるフラグ変数
    tabula_lasa_count = 0 #初期配置失敗の回数カウント用変数
    while initialize_flag == False:
        L=[]
        alpha = [random.uniform(sigma,1.0),random.uniform(sigma,1.0),'r']
        L.append(alpha)
        for k in range(1, N):
            alpha = [random.uniform(sigma,1.0-sigma),random.uniform(sigma,1.0-sigma),'r']
            min_dist = min(dist(alpha, beta) for beta in L)
            if min_dist < 4.0 * sigma_sq:
                initialize_flag = False
                tabula_lasa_count +=1
                break
            else:
                L.append(alpha)
                initialize_flag = True
    return L
    print L ,'tabula lasa count:', tabula_lasa_count/N
################################################################################
def main():
    L = initialize_direct(N)#Lの初期化
    #フォルダ作る関数
    if not os.path.exists(output_dir): os.makedirs(output_dir)#もしoutput_dirのディレクトリが無かったら作成する。

    for steps in range(n_steps):#MCチェインで粒子を動かすループ
        snapshot(L,steps)#L:配置&色,steps:ステップ数
        a = random.choice(L)
        if a[2] == 'r': #吸着していない粒子が選択された場合
           a = mc_bonding(a,L)
        elif a[2] == 'b':#吸着している粒子が選ばれた場合
             if random.uniform(0,1) >prob_join:#乱数が結合エネルギーを超えて振り切った場合
                a = mc_bonding(a,L)



    print L

if __name__ == '__main__':
    main()
