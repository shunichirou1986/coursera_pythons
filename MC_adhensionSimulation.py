#encoding :utf-8
import random,math,os,pylab

#とりあえず粒子間相互作用は完全に無視、壁への衝突と吸着のみを表現。壁からの脱離も無し


#定数、変数宣言
img = 0#描画関数内部で使う変数
COLORS = ['r', 'b', 'g', 'orange']#描画関数で使う色
L = []#剛体円の座標を格納するリスト
N = 10#粒子個数
TOTAL_PARTICLE_DENSITY = 3.3E-7
sigma_sq = 1.0* TOTAL_PARTICLE_DENSITY /(math.pi * N )#密度および粒子個数から計算した粒子半径（二乗）
sigma = math.sqrt(sigma_sq)#粒子サイズ
print sigma
delta = 0.05 #MC一回毎の移動距離
n_steps =100 #粒子を動かす回数
accept_ratio =0.0#移動が許容された回数
#関数

#距離を算出する関数
def dist(x,y):
    d_x = abs(x[0] - y[0]) % 1.0
    d_x = min(d_x, 1.0 - d_x)
    d_y = abs(x[1] - y[1]) % 1.0
    d_y = min(d_y, 1.0 - d_y)
    return  (d_x**2 + d_y**2)

#描画する関数：吸着しているやつは色変えたいな
def snapshot(pos,steps):
    global img
    pylab.subplots_adjust(left=0.10, right=0.90, top=0.90, bottom=0.10)
    pylab.gcf().set_size_inches(6, 6)
    pylab.axis([0, 1, 0, 1])
    pylab.setp(pylab.gca(), xticks=[0, 1], yticks=[0, 1])
    for (x, y, c) in pos:
        circle = pylab.Circle((x, y), radius=sigma, fc=c)
        pylab.gca().add_patch(circle)
    pylab.savefig(os.path.join(output_dir, '%04d.png' % steps), transparent=False)
    pylab.close()
    img += 1

#フォルダ作る関数
output_dir = 'Adhension_Simulation'
if not os.path.exists(output_dir): os.makedirs(output_dir)#もしoutput_dirのディレクトリが無かったら作成する。


#モンテカルロ法で動かして、判定する関数


#ポテンシャルを表現する関数

#初期配置決め関数（ダイレクトサンプリング）
def initialize_direct(N):
    initialize_flag = False#初期化時に用いるフラグ変数
    tabula_lasa_count = 0 #初期配置失敗の回数カウント用変数
    while initialize_flag == False:
        L=[]
        alpha = [random.uniform(sigma,1.0-sigma),random.uniform(sigma,1.0-sigma),'r']
        L.append(alpha)
        for k in range(1, N):
            alpha = [random.uniform(sigma,1.0-sigma),random.uniform(sigma,1.0-sigma),'r']
            min_dist = min(dist(alpha, beta) for beta in L)
            if min_dist < 4.0 * sigma_sq: 
                initialize_flag = False
#                tabula_lasa_count +=1
                break
            else:
                L.append(alpha)
                initialize_flag = True
    return L
    print L #,'tabula lasa count:', tabula_lasa_count


    

#メイン：初期配置決めて（最初はダイレクトサンプリングアルゴリズム））→ポテンシャルに基づいてモンテカルロ法で動かして（ループ）→フォルダ作って→描画して可視化

L = initialize_direct(N)

for steps in range(n_steps):#MCチェインで粒子を動かすループ
    a = random.choice(L)
    if a[2] == 'r': #吸着していない粒子が選択された場合
        b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta),'r']
        min_dist = min(dist(b,c) for c in L if c != a)
        if (min_dist > 4.0 * sigma**2): 
            a[:] = b#周期的境界条件には非対応
            accept_ratio += 1
        #ここから壁に衝突したパターン
        if   a[0]-sigma < 0 :#左壁に衝突
            a[0]=0 +sigma
            a[2]='b'
        elif a[0]+sigma > 1 :#右壁に衝突
            a[0]=1-sigma
            a[2]='b'
        if a[1]-sigma < 0 :#下壁に衝突
            a[1]=0+sigma
            a[2]='b'
        elif a[1]+sigma > 1 :#上壁に衝突
            a[1]=1-sigma
            a[2]='b'
    snapshot(L,steps)#L:配置&色,steps:ステップ数
    


#    show_conf(L,sigma,'intermediate_configuration'+str(steps),intermediate_filename)
print 'final configuration',L ,'accept ratio',accept_ratio/n_steps

