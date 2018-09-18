#!/usr/bin/python
#_*_coding:utf-8_*_
count_win = 0
count_lost= 0
import random
all_choice = ["石头","剪刀","布"]
win_list = ["石头","剪刀"],["剪刀","布"],["布","石头"]
prompt = "(0)石头 (1)剪刀 (2)布 请选择(0/1/2):"
while count_win < 2 and count_lost < 2:


if count_win == 2 :
    print ("获得最终胜利")
else:
    print("最终失败")
