#coding:UTF-8

Names = {}
Names['Albert'] = 'Einstein'
Names['Satyendra'] = 'Bose'
Names['Richard'] = 'Feynman'
Names['Ludwig'] = 'Boltzmann'
L = [1.4,1.5]
print "checkpoint 1"
for name in Names: print name, Names[name]
a = Names.pop('Albert') #pop���\�b�h�͎w�肵���L�[�ɊY������v�f���폜�A�l��Ԃ�
print "checkpoint 2"
for name in Names: print name, Names[name]
del Names['Richard'] #del���͈����Ɏw�肵�����ڂ��폜����B
print "checkpoint 3"
for name in Names: print name, Names[name]
L = Names.keys()#keys���\�b�h�̓L�[�̃��X�g�̎擾
M = Names.values()#values�͒l�̃��X�g�̎擾
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
