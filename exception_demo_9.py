# coding=utf-8
'''
Exception.
1. raise like throws in java.
2. 
'''
__Author__ = 'Tony'
import time

class RaiseException(Exception):
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

def simple_demo():
    try:
        1/0
    except:
        print 'error '
    print 'not exit'

def with_raise():
    '''
    retry 3 times.
    '''
    for i in range(3):
        try:
            s = raw_input('Enter a str...')
            if len(s) < 3:
                raise RaiseException(len(s),3)
            break
        except RaiseException, x:
            print '''ShortInputException: The input was of length %d, was expecting at least %d''' % (x.length, x.atleast)
    else:
        print 'more than three times.'

def with_finally():
    try:
        f =file('exception_demo.py')
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            time.sleep(3)
            print line
    finally:
        f.close() #f在此处可访问
        print 'close file'

if __name__ == '__main__':
    #simple()
    with_raise()
   # with_finally()
