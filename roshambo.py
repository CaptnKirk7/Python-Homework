#encoding=utf-8
#rock:0 scissor:1 paper:2

import random
import time

i=0
drawCount=0
winCount=0
loseCount=0

roundCount=int(input("你一共想玩几把【锤子剪刀布】的游戏？:"))

while i<roundCount:

	print("-+-"*15)
	playerInput=input("石头:0 剪刀:1 布:2\n请选择:")

	player=int(playerInput)

	pc=random.randint(0,2)

	playerChoice=""
	pcChoice=""

	if player==0:
		playerChoice="石头"
	elif player==1:
		playerChoice="剪刀"
	elif player==2:
		playerChoice="布"

	if pc==0:
		pcChoice="石头"
	elif pc==1:
		pcChoice="剪刀"
	elif pc==2:
		pcChoice="布"

	time.sleep(1)

	print("你的\"%s\" VS 电脑的\"%s\""%(playerChoice,pcChoice))


	time.sleep(1)

	if player==pc:
		print("平局！")
		drawCount+=1
	elif (player==0 and pc==1) or (player==1 and pc==2) or (player==2 and pc==0) :
		print("你赢啦！")
		winCount+=1
	elif (player==0 and pc==2) or (player==1 and pc==0) or (player==2 and pc==1) :
		print("你输啦！")
		loseCount+=1
	

	i+=1
print("-+-"*15)
print("总计%d局：赢%d局 输%d局 平%d局"%(roundCount,winCount,loseCount,drawCount))
if winCount>loseCount:
	print("恭喜！你最终战胜了电脑！！")
else :
	print("继续努力！")