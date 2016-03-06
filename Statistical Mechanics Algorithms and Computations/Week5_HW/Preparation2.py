#coding:utf-8
import numpy

a = numpy.array([[1, 2, 3], [4, 5, 6]])
print 'a:'
print a
print a.shape
print 'a[0,0] %d' %a[0,0]
print 'a[1,0] %d' %a[1,0]
print 'a[0,1] %d' %a[0,1]
print 'a[1,1] %d' %a[1,1]
print 'a[0,2] %d' %a[0,2]
print 'a[1,2] %d' %a[1,2]
b = numpy.array([[1, 2], [3, 4], [5, 6]])
print 'b:'
print b 
c = numpy.dot(a, b) #dot‚Í“ñ‚Â‚Ìs—ñ‚Ì“àÏB
print 'c:'
print c
d = numpy.dot(b, a)
print 'd:'
print d
e = d * 2
print 'e:'
print e
f = numpy.diag(c)
print 'f:'
print f
g = numpy.diag(c).sum()
print 'g:'
print g