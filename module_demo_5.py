#!coding=utf-8
'''
comment
- when import subfolder,you need add __init__.py as package
'''
import sys
#import guess_numer_3
from module.guess_numer_3 import main
__Author__ = 'Tony'

if __name__ == '__main__':
    #
   #print sys.argv # as list,list[0] is filename 
   #print sys.path
   #guess_numer_3.main(10)
   main(10)
else:
    print "I'm imported."

