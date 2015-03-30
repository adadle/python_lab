#!/usr/bin/python
#coding=utf-8
"""
题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
"""

#方案一： 三层嵌套循环遍历
def solution1():
	""" print out: 
1 2 3
1 2 4
1 3 2
1 3 4
1 4 2
1 4 3
2 1 3
2 1 4
2 3 1
2 3 4
2 4 1
2 4 3
3 1 2
3 1 4
3 2 1
3 2 4
3 4 1
3 4 2
4 1 2
4 1 3
4 2 1
4 2 3
4 3 1
4 3 2
qualifiedNum is : 24
"""
	dict = [1,2,3,4]
	qualifiedNum = 0
	for i in xrange(0,4):
		hundredNum = dict[i]
	#	print "i:",i,"num: ",hundredNum
		for j in xrange(0,4):
			tenNum = dict[j]
	#		print "j:",j
			if hundredNum == tenNum:
				pass
			else:
				for k in xrange(0,4):
					lastNum = dict[k]
	#				print "k:",k
					if lastNum == tenNum or lastNum == hundredNum:
						pass
					else:
						qualifiedNum += 1
						print hundredNum,tenNum,lastNum
	print "qualifiedNum is :",qualifiedNum	

#方案二： 先排序
def solution2():
	dict = [1,2,3,4]
	qualifiedNum = 0
	
if __name__ == '__main__':
	solution1()


	
