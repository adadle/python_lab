#!coding=utf-8
'''
练习表达式的demo,基础语法
'''
__Author__ = 'Tony'

def get_perimeter(length, width):
    """
    计算长方形的面积
    """
    return length * width

def get_area(length, width):
    """
    """
    return 2*(length+width)


if __name__ == '__main__':
    print "rectangle's square: ",get_area(2,3)
    print "rectangle's perimeter: ",get_perimeter(2,3)
