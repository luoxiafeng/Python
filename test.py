#!/usr/bin/python
#coding:utf-8
import os

"""
(1)������Կ�����i��������string
(2)print��ӡ��ʱ�򣬶��ţ�ֻ����ͬ���͵ı���
(3)print��ӡ��ʱ�򣬼Ӻţ���ʾ�ַ������� 
"""
def base_rules_1():
    for i in "123456":
		print i
		print "this is no:",i
		print "do it:"+i
    pass

'''
(1)count������int���͡�
(2)�����Ѿ�˵�������ţ���print��ֻ������ͬ�����ͣ����еĹ�ϵ
(3)print "�ַ���",count(int����),���лᱨ����������
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
