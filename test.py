#!/usr/bin/python
#coding:utf-8
import os

"""
(1)这里可以看到，i的类型是string
(2)print打印的时候，逗号，只允许同类型的变量
(3)print打印的时候，加号，表示字符串链接 
"""
def base_rules_1():
    for i in "123456":
		print i
		print "this is no:",i
		print "do it:"+i
    pass

'''
(1)count现在是int类型。
(2)我们已经说过，逗号，在print中只允许相同的类型，并列的关系
(3)print "字符串",count(int类型),运行会报错！！！！！
'''
def base_rules_2():
    count=1
    while count<10:
        count = count + 1
        print count
        print "try:",count
        print "try again:"+count
    pass

def base_rules_3():
    count = 4
    while count < 10 :
        print count
        count = count + 1 
    else:
        print "while-else"
    pass
        

if __name__=="__main__":
    base_rules_1()
    #base_rules_2()
    print "========================"
    base_rules_3()
