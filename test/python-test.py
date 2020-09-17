# -*- coding:utf-8 -*-
# 猜拳游戏

import random
switch = {1:"石头",
          2:"剪刀",
          3:"布"}

playerAction = int(input("请输入拳 石头==1 剪刀==2 布==3："))
computer = random.randint(1,3)

print(" 我：" + '' + switch[playerAction])
print("电脑：" + '' + switch[computer])
if playerAction == computer:
    print("双方平手！")
else:
    if(playerAction == 1 and computer == 2) or (playerAction == 2 and computer == 3) or (playerAction == 3 and computer == 1):
        print("你赢了！")
    else:
        print("电脑赢了！")