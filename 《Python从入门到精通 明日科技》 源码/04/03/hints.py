﻿# -*- coding:utf-8 -*-

'''
   @ 功能：根据年龄输出不同的提示
   @ author:无语
   @ create:2018-3-30

'''

your_age = int(input("请输入您的年龄："))            # 获取用户输入的年龄，并转换为整型
if your_age <= 18:                       # 调用if语句判断输入的数据是否小于等于18
    # 如果小于等于18则输出提示信息
    print("您的年龄还小，要努力学习哦！")
elif 18 < your_age <= 30:    # 判断是否大于18岁，并且小于30岁
    # 如果输入的年龄大于18岁并且小于30岁则输出提示信息
    print("您现在的阶段正是努力奋斗的黄金阶段！")
elif 30 < your_age <= 50:     # 判断输入的年龄是否大于30岁小于等于50岁
    # 如果输入的年龄大于30岁而小于等于50岁则输出提示信息
    print("您现在的阶段正是人生的黄金阶段！")
else:
    print("最美不过夕阳红！")
