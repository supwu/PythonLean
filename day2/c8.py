#!/usr/bin/env python
# -*- coding:utf-8 -*-

#成员运算

li = ["桌子","椅子","黑板","粉笔"]

# ret = "ads" in li
# ret1 = "asdf" not in li
# print(ret)
# print(ret1)

#enumerate序列化,形成键值对
for key,item in enumerate(li):
    print(key,item)

inp = input("请输入：")
print(li[int(inp)])

