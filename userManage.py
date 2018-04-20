#encoding=utf-8
#通过字典模拟登陆系统，填写用户名及密码，具备修改密码功能，并验证登陆
#Kewei-homework-20180420

import getpass
import random
import time
import hashlib

#显示菜单
def displayMenu():
	print("\n","="*10,"用户管理模拟系统","="*10,"\n")
	print("       1:查看所有用户\n")
	print("       2:新建用户\n")
	print("       3:修改指定用户密码\n")
	print("       4:删除用户\n")
	print("       5:登陆验证\n")
	print("       6:显示数据库\n")
	print("       q:退出")
	print("\n","="*38)

#选择菜单，从键盘获取数字确定菜单
def selectMenu():
	menuNum = str(input(" 【系统提示】请选择菜单序号:"))
	while menuNum !='1' and menuNum !='2' and menuNum !='3' and menuNum !='4' and menuNum !='5' and menuNum !='6' and menuNum !='q':
		print("错误！请重新选择！")
		menuNum = str(input("请选择:"))
		if menuNum == 'q':
			break
	return menuNum
#print(selectMenu())

#菜单操作
def actionMenu(menuNum):
	if menuNum == "1": 	#1:查看所有用户
		listDb()
		sleepTime()
	elif menuNum =="2":	#2:新建用户
		addNewUser()
		sleepTime()
	elif menuNum =="3":	#3:修改用户密码
		editPwd()
		sleepTime()
	elif menuNum =="4": #4:删除用户
		delUser()
		sleepTime()	
	elif menuNum =="5": #5:登陆验证
		loginTest()
		sleepTime()
	elif menuNum =="6": #6:查看数据库便于调试
		print("\n","【Key-Value】")
		seq=1
		for user in userDb:
			print("  %d.%s"%(seq,user))
			seq+=1
		sleepTime()
	

#创建字典 填入几个测试数据
userDb=[{'NAME':'kewei','PWD':'123','UPDATETIME':"2018-04-20 20:20:20"},{'NAME':'aaa','PWD':'123','UPDATETIME':"2018-04-20 20:20:20"},{'NAME':'bbb','PWD':'123','UPDATETIME':"2018-04-20 20:20:20"}]
#查看所有用户数据
def listDb():
	if userDb=={}:
		print("系统提示：目前没有任何数据！\n\n")
	else :
		print("\n","系统目前有%d个用户:"%len(userDb))
		seq=1
		for k in userDb :
			print("  %d.%s"%(seq,k['NAME']))
			seq+=1


#新增用户及分配密码
def addNewUser():
	print("\n","【新增用户】\n")
	userName = str(input("  用户名:"))
	for k in userDb:
		while k['NAME']==userName or userName=="":
			userName=str(input("  该用户名已注册，请重新输入:"))
	userPwd = str(getpass.getpass("  请输入密码:"))
	userAddtime = updateTime()
	userAddLine = {'NAME':userName,'PWD':userPwd,'UPDATETIME':userAddtime}
	userDb.append(userAddLine)
	
	print("\n","【系统提示】新用户“%s”添加成功！"%userName,end="")
	print("%s"%userAddtime)

#修改指定用户的密码
def editPwd():
	print("\n","【修改用户密码】\n")
	searchUsrName=input("  请输入将要查找的用户名：")
	findKey=0 #初始化用户是否找到，0：未找到，1：找到
	for k in userDb:
		if k['NAME']==searchUsrName:
			findKey=1
			userDic=k
			userDb.remove(k)
	if findKey==1:
		inputOriginPwd = getpass.getpass("  请输入原密码：")
	
		if inputOriginPwd == userDic['PWD']:
			inputNewPwd=getpass.getpass("  原密码正确，请输入新密码：")
			userAddtime = updateTime()
			userAddLine = {'NAME':searchUsrName,'PWD':inputNewPwd,'UPDATETIME':userAddtime}
			userDb.append(userAddLine)
			print("\n","【系统提示】密码更新成功！")	
		else:
			print("\n","【系统提示】密码错误，禁止修改")
	elif findKey==0:
		print("\n【系统提示】未找到用户！")

#删除指定用户
def delUser():
	print("\n","【删除用户】\n")
	searchUsrName=input("  请输入将要[删除]的用户：")
	findKey=0 #初始化用户是否找到，0：未找到，1：找到
	for k in userDb:
		if k['NAME']==searchUsrName:
			userDic=k
			findKey=1
	if findKey==1:
		inputOriginPwd = getpass.getpass("  请输入密码：")
		if inputOriginPwd == userDic['PWD']:
			delConfirm=input("  确认删除？Y/N:")
			if delConfirm=='Y'or'y':	
				userDb.remove(userDic)
				print("\n","【系统提示】删除成功!")
			else:
				return
		else:
			print("\n","【系统提示】密码错误！禁止删除！")
	elif findKey==0:
		print("\n","【系统提示】未找到用户！")


#验证登陆是否成功
def loginTest():
	print("\n","【登陆验证】\n")
	loginUsrName=input("  请输入用户名：")
	loginUsrPwd=getpass.getpass("  请输入密码：")

	#生成验证码
	source=['0','1','2','3','4','5','6','7','8','9','a', 'b', 'c', 'd', 'e', 'f']
	a=random.sample(source,4)
	verifyCode="".join(a)

	loginCode = input("  验证码[%s]:"%verifyCode)
	loginFlag=0

	for k in userDb:
		if k['NAME']==loginUsrName and k['PWD']==loginUsrPwd and loginCode == verifyCode:
			loginFlag=1
	
	if loginFlag==1:	
		print("\n","【系统提示】登陆成功！")		
	elif loginFlag==0:
		print("\n","【系统提示】登陆信息错误！")
		
def updateTime():
	uTime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	return uTime

#模拟系统响应时间1s
def sleepTime():
	time.sleep(1)


#------main-------
selectNum=''
while selectNum != 'q':
	displayMenu()
	selectNum = selectMenu()
	actionMenu(selectNum)

