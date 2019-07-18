#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   12_detailBasicType.py
@Time    :   2019/07/08 11:40:38
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

# here put the import lib
# 1.数字类型（int）
power_int = 2 ** 40
print("power_int：", power_int)
print("power_int_type：", type(power_int))
str_int = int('123')
print("str_int_type：", type(str_int))
# 将数字转换为二进制，并返回最少位二进制的位数
bit_length_int = 123
print(bit_length_int.bit_length())


# ---------------------------------------------------------------------
# 2.bool类型（bool）
none_value = bool(None)
print("none_value: ", none_value)
blank_1 = bool([])
print("blank_1: ", blank_1)
blank_2 = bool({})
print("blank_2: ", blank_2)
blank_3 = bool("")
print("blank_3: ", blank_3)
blank_4 = bool(())
print("blank_4: ", blank_4)
zero_value = bool(0)
print("zero_value: ", zero_value)


# ------------------------------------------------------
# 3.字符串类型（str）
# （1）索引
# index()与find()的区别：若索引的该字符或者序列不在字符串内，
#  index-->返回ValueError: substring not found，而find -->返回 -1
string1 = "没有什么独特"
index_str = string1.index("没", 0)
print("index_str: ", index_str)
find_str = string1.find("有", 2)
print("find_str: ", find_str)

# （2）切片
string2= "这是一首简单的歌"
section_str = string2[0: 1]
print("section_str: ", section_str)

# （3）长度
string3 = "试着带入我的心事"
len_str = len(string3)
print("len_str: ", len_str)

# （4） 遍历
string4 = "它那么幼稚"
for ergodic_str in string4:
    print("ergodic_str: ", ergodic_str)
for index in range(len(string4)):
    print("ergodic_str2: ", string4[index])

# （5）删除
string5 = "像个顽皮的孩子"
del string5
# print("del_str: ", string5)

# （6）分割【partition制定分隔符，split指定分隔符分割几次】
string6 = "多么-可笑的-心事 TEST METHOD YOU LOSE"
partition_str = string6.partition("-")
print("partition_str: ", partition_str)
split_str = string6.split(" ", 2)
print("split_str: ", split_str)

# （7）替换【replace、strip、lstrip、rstrip】
string7 = " 顽皮的像个孩子的大人 "
replace_str = string7.replace('的', "XX", 2)
print("replace_str: ", replace_str)
strip_str = string7.strip()
print("strip_str去掉两边的空格:", strip_str)
lstrip_str = string7.lstrip()
print("lstrip_str去掉左边的空格:", lstrip_str)
rstrip_str = string7.rsplit()
print("rstrip_str去掉右边的空格：", rstrip_str)

# （8）连接【join】
string8 = "MOREANDMORE"
join_str = '*'.join(string8)
print("join_str: ", join_str)
list8 = ['xi', 'as', 'peo']
join_list = "->".join(list8)
print("join_list: ", join_list)

# （9）大小写转换【capitalize、】
string9 = "start is More and More"
capitalize_str = string9.capitalize()
print("capitalize_str: ", capitalize_str)
lower_str = string9.lower()
print("lower_str: ", lower_str)
upper_str = string9.upper()
print("upper_str: ", upper_str)
tittle_str = string9.title()
print("tittle_str: ", tittle_str)
swapcase_str = string9.swapcase()
print("swapcase_str: ", swapcase_str)

# （10）判断以什么开头【startswith()、endswith()】
string10 = "How are 你?"
startswith_str = string10.startswith("How")
print("startswith_str: ", startswith_str)
endswith_str = string10.endswith("?")
print("endswith_str: ", endswith_str)

# （11）判断字符串的内容【isalnum、isalpha、isdigit】
string11 = "Howare1213"
isalnum_str = string11.isalnum()
print("isalnum字符串是数字或字母的组合: ", isalnum_str)
isalpha_str = string11.isalpha()
print("isalpha字符串全部是字母：", isalpha_str)
isdigit_str = string11.isdigit()
print("isdigit字符串数字的组合：", isdigit_str)

# （12）格式化输出【format 、format_map】
string12 = "My name is {name}, I'am {age} years old."
print(string12.format(name="XIAO MI", age=9))
print(string12.format_map({"name": "MI", "age": 90}))

#（13）扩展【expandtabs】
string13 = "name\tage\tsex\nA\t22\tmale\nB\t23\tfmale"
expandtabs_str = string13.expandtabs()
print("expandtabs_str: \n", expandtabs_str)