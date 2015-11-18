# coding=utf-8
'''

'''
__Author__ = 'Tony'

import os

s='''
def get_perimeter(length, width):
    """
    function comment 
    """
    return length * width

if __name__ == '__main__':
    #
'''

f = file('file.log','w')
f.write(s)
f.close()
print "write ok."


f = file('file.log')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print line

f.close

os.rmdir('./file.log')
print 'remove file'
