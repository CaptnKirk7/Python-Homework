# encoding=utf-8
import jieba # pip install jieba

'''
Kewei@2018
程序实现：通过对文本的识别和切片，反馈切片后的词语出现频次
'''

# 文本引入
inputString = input("输入需要切分的句子：")
# 通过jieba.cut()方法将文本进行切分
segString = jieba.cut(inputString)
# 将切分后的文本转换为列表方式
list_segString=list(segString)
# print(list_segString)

# 格式化结果列表
resultCount = []

# 针对每个切片结果进行次数统计，并以字典形式{'keyword': 'kewei', 'count': 2}加入到resultCount列表中
for n in list_segString:
    coutNum = 0
    for x in list_segString:
        if n == x:
            coutNum += 1
    resultCount.append({'keyword': n, 'count': coutNum})

# 针对列表字典结果进行去重和排序
arrangeResult = []
arrangeResult.append(resultCount[0])

for x in resultCount:
    k=0
    for y in arrangeResult :
        if x['keyword'] != y['keyword']:
            k = k+1
        else:
            break
        if k == len(arrangeResult):
            arrangeResult.append(x)
#排序，出现频次由高至低
sorted_arrangeResult = sorted(arrangeResult, key=lambda x: (x['count']),reverse=True)

#输出前5名结果
print(sorted_arrangeResult[0:5])