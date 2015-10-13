#!coding=utf-8
'''
Guess the target number
exercise for expr and ctr.
'''
import pdb

__Author__ = 'Tony'

def main(target):
    """
    guess five times,still fail will exit.
    """
    guess = 0
    counter = 1
    allow_number = 4
    while guess != target and allow_number >= counter :
        guess = int(raw_input("Enter your guess number: "))
#        pdb.set_trace()
        if guess > target:
            print " %s bigger than target" % guess
        elif guess < target:
            print " %s less then target" % guess
        else:
            print "You Got it..."
            break
        print "You  have %i times" % (allow_number-counter)
        counter += 1 

if __name__ == '__main__':
    target = int(raw_input("Enter your target: "))
    for i in range(100):
        print "xx||xx"
    print "Your target is: xxx"
    main(target)
