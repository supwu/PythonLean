#!/usr/bin/env python
# -*- coding:utf-8 -*-

#import lib

#print('hello world')
import getpass

user = input("Username:")
pwd = getpass.getpass("Password:")

print(user)
print(pwd)

if user == "alex" and pwd == "123":
	print("yes")
else:
	print("no")
	