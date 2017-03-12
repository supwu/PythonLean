#!/usr/bin/env python
# -*- coding:utf-8 -*-

li = ["alec", "aric", "Alex", "rain"]
tu = ("alec", "aric", "Alex", "Tony", "rain")
dic = {"k1":"alec", "k2":"aric", "k3":"Alex", "k4":"Tony"}

# 结果集
ret_li = []
ret_tu = []
ret_dic = {}

# 遍历列表、元组、字典，记录符合条件的数据
for tmp_str in li:
    if tmp_str[0]=='a' or tmp_str[0] == 'A':
        if tmp_str[tmp_str.__len__()-1] == 'c':
            ret_li.append(tmp_str)
for tmp_str in tu:
    if tmp_str[0]=='a' or tmp_str[0] == 'A':
        if tmp_str[tmp_str.__len__()-1] == 'c':
            ret_tu.append(tmp_str)
keys = dic.keys()
for key in keys:
    tmp_str = dic[key]
    if tmp_str[0]=='a' or tmp_str[0] == 'A':
        if tmp_str[tmp_str.__len__()-1] == 'c':
            ret_dic[key] = tmp_str


print(ret_li)
print(ret_tu)
print(ret_dic)
