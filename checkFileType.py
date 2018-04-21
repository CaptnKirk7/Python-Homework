#encoding=utf-8
import time

fileNames=["01.py","02.py","03.rar","04.c",
"05.cpp","06.php","07.java","index.html","readme.doc"]

i=0
count=len(fileNames)

while i<count:
	tempFile = fileNames[i]
	tempDotIndex = tempFile.rfind(".")
	tempType = fileNames[i][tempDotIndex:]
	print(tempType)
	time.sleep(0.5)
	i+=1

