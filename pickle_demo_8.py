# coding=utf-8
'''
与java的序列化和反序列化相似
'''
__Author__ = 'Tony'
import cPickle as p

name_list_file='name_list.dat'

name_list =['tony','lee']

f = file(name_list_file,'w')
p.dump(name_list,f)
f.close()

obj = p.dumps(name_list)
print 'dumps type:',type(obj)
print 'print obj', obj
#del name_list

f = file(name_list_file)
name_list = p.load(f)
print name_list
