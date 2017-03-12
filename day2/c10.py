#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 用户输入总资产
TotAmt = 0.00
PayaMount = 0.00
MoreAmt = 0.00

inp = input("总资产是:")
TotAmt += float(inp)


#商品列表、价格列表
products = {"001":"手机", "002":"电脑", "003":"鼠标垫", "004":"游艇"}
prices = {"001":1000, "002":2000, "003":20,"004":1000000}
#购物车列表
buys = []

# 输出商品列表
print("所有商品如下：")
for key in products.keys():
    print(key,products[key])

# 添加到购物车
while True:
    inp = input("请输入商品编号，加入购物车,输入OK结束购买:")
    if inp == "OK":
        break
    if inp not in products.keys():
        print("您输入了一个错误的商品编号!")
        continue
    buys.append(inp)

# 输出购物车商品
for item in buys:
    print(item,products[item],prices[item])



# 移除商品、购买、充值
while True:
    inp = input("移除商品请输入商品编号,充值请输入MORE,购买请输入BUY,取消请输入CANCEL")
    #充值
    if inp == "MORE":
        inp = input("请输入充值金额:")
        TotAmt += float(inp)
        continue

    #取消购买
    if inp == "CANCEL":
        print("购买取消！")
        break

    #购买
    if inp == "BUY":
        for item in buys:
            PayaMount += prices[item]
        if PayaMount > TotAmt:
            print("余额不足!")
            continue
        print("购买完成！余额:", TotAmt-PayaMount)
        break

    # 移除商品
    if inp not in buys:
        print("您输入了一个错误的商品编号！")
        continue
    del buys[int(inp)]

