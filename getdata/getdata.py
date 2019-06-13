import pandas as pd
import csv
text = input()
long = len(text)
text1 = []
text_a = ""
a = 0
lable = ""
b = 0
for i in text:
    if a<long-1:
        text1.append(i)
        text_a = text_a + i + "\002"
        a=a+1
    else:
        text_a = text_a + i

for i in range(long):
    if b<long-1:
        lable = lable + 'p-B' + "\002"
        b= b + 1
    else:
        lable = lable + 'p-B'
print(text)
print(long)
print(text1)

print(text_a)
print(lable)
tsvFile = open("testline.tsv",'w')
tsvFile.write("text_a")
tsvFile.write("\t")
tsvFile.write("label")
tsvFile.write("\n")
tsvFile.write(text_a)
tsvFile.write("\t")
tsvFile.write(lable)
tsvFile.close()