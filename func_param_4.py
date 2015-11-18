#!coding=utf-8
'''
function definition and args usages.
'''
__Author__ = 'Tony'

x = "x is global"
def get_max(a,b):
    """
    function comment 
    """
    if a > b:
        return a
    else:
        return b

def test_global():
    '''
    定义的变量x, 在该方法中被声明为global后,在test_global_1()中可以获取状态的更新.
    '''
    global x
    print x
    x = "x is x"
    print x

def test_global_1():
    print x 
    
def default_arg(key, value="value"):
    print key,value

def key_arg(name,value,age=0):
    print name,value,age
    

if __name__ == '__main__':
    #print get_max(8,9)
    # demo global args.
    #test_global()
    #test_global_1()
    # demo default args.
    #default_arg("tony") 
    #default_arg("tony","lee") 
    # demo key args
    key_arg(value="li",name="tony")
    print test_global.__doc__ 


