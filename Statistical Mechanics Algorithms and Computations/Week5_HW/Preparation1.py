#coding:UTF-8

Names = {}
Names['Albert'] = 'Einstein'
Names['Satyendra'] = 'Bose'
Names['Richard'] = 'Feynman'
Names['Ludwig'] = 'Boltzmann'
L = [1.4,1.5]
print "checkpoint 1"
for name in Names: print name, Names[name]
a = Names.pop('Albert') #popメソッドは指定したキーに該当する要素を削除、値を返す
print "checkpoint 2"
for name in Names: print name, Names[name]
del Names['Richard'] #del文は引数に指定した項目を削除する。
print "checkpoint 3"
for name in Names: print name, Names[name]
L = Names.keys()#keysメソッドはキーのリストの取得
M = Names.values()#valuesは値のリストの取得
print 'The datatypes of L and M are %s and %s ' % (type(L),type(M)) 
print "checkpoint 4"
for name in Names: print name, Names[name]
b = 'Wolfgang' in Names
print "checkpoint 5"
for name in Names: print name, Names[name]
print 'b :%s'%b
Names['3.141592'] = 'pi'
Names[L] = 'list_L'
for name in Names: print name, Names[name]
