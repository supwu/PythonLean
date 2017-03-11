#!usr/bin/env python
# -*- coding:utf-8 -*-

#import lib

#print('hello world')
import getpass

i1 = input("Username:")
#i2 = input("Password:")
i2 = getpass.getpass("Password:")
print(i1)
print(i2)