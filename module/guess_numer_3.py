#!coding=utf-8
'''
Guess the target number, have fun...
'''

__Author__ = 'Tony'

def main(target,guess_time=5):
    """
    guess five times,still fail will exit.
    """
    guess = 0
    counter = 1
    allow_number = guess_time
    while guess != target and allow_number >= counter :
        guess = int(raw_input("Enter your guess number: "))
        #import pdb;pdb.set_trace()
        if guess > target:
            print " %s bigger than target," % guess,
        elif guess < target:
            print " %s less then target," % guess,
        else:
            print "**************>>>> Cons -^^-, You Got it..."
            break
        if counter == allow_number :
            print ''' I'm so sorry,you do not shoot the target in %s times,the target number is: %s. 
                      See ya!
                  ''' %(allow_number,target)
        else:
            print "You  still have %i times" % (allow_number-counter)
        counter += 1 

if __name__ == '__main__':
    target = int(raw_input("Enter your target: "))
    guess_time = int(raw_input("Guess times: "))
    for i in range(100):
        print "xx||xx"
    print "Your target is: xxx, Can you shoot it? "
    print "You have %s times,Let's go...."  % guess_time
    main(target,guess_time)
