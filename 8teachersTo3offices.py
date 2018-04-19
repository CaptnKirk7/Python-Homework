#encoding=utf-8
import random
#题目：随机将8名老师分配到3个办公室，且每个办公室至少有2名老师

#老师列表
teachers=["Mike","Tom","Harry","Rose","Jack","Frank","Pipe","Smith"]
#设置3个空的办公室列表
office=[[],[],[]]

#循环计算次数
roundCount=0

#办公室随机数
officeRandNum=0

#当每个办公室人数小于2人时，循环计算
while len(office[0])<2 or len(office[1])<2 or len(office[2])<2:
	#重制办公室列表为空
	office=[[],[],[]]
	#循环次数
	roundCount+=1

	for teacherName in teachers:
		#随机办公室序号
		officeRandNum=random.randint(0,2)
		#将老师名称放入办公室嵌套列表
		office[officeRandNum].append(teacherName)

#输入结果
print("-"*40)
num=1
for officeStaff in office:
	print("第%d办公室："%num)
	for members in officeStaff:
		print(members)
	num+=1
	print("-"*40)
print("本次计算共循环了%d次得出结果："%roundCount)
print("-"*40)