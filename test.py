#!/usr/bin/python
#coding:utf-8
import os
import sys

"""
(1)这里可以看到，i的类型是string
(2)print打印的时候，逗号，表示并列的关系，输出的都是变量,类型可以不一样
(3)print打印的时候，加号，表示字符串链接,必须都是字符串类型  
"""
def base_rules_1():
    age = 24
    name = "summer"
    for i in "123456":
		print i
		print "this is no:",i
		print "do it:"+i
    print "name:%s,age:%d" % (name,age)
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

def base_rules_4():
    days=['monday',"tuesday","wednesday","thursday","friday"]
    for each in days:
        print each
    pass

def base_rules_5():
    if (1):
        print "if can use ()";
    while(1):
        print "while 1 can use ()";
        break;
    for i in range(1,4):
        print "for test",i
    return True

'''
(1)这里要注意，print输出的是一个字符串，可以作为命令
(2)str1的格式，就是用的print的格式，来给字符串赋值
'''
def base_rules_6():
    string="abc"
    var1 = "_"
    var2 = None
    string += var1 + "123"
    print string
    str1 = '%s%s_%d' % (string,"456",23)
    print str1
    str2 = ("fuck") if var2 is not None else "pi"
    print str2
    pass

'''
(1)注意，os的system的参数，必须是字符串
'''
def module_os_use1():
    os.system("pwd");
    pass

if __name__=="__main__":
    #base_rules_1()
    #base_rules_2()
    print "========================"
    #base_rules_3()
    print "========================"
    #base_rules_4()
    print "========================"
    #if ( base_rules_5() == True ):
	#	print "base_rules_5 pass"
    print "========================"
    #base_rules_6();
    print "========================"
    module_os_use1()

