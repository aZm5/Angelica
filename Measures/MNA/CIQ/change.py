f=open("tax10090.txt")
f1=open("Rtax10090.txt","a+")
data=[]
for line in f.readlines():
    lineArr=line.strip().split("\t")
    data.append([lineArr[1],lineArr[2]])
# print(data)
for i in data:
    f1.write(i[0]+'\t'+i[1]+'\n')


f1.close()
f.close()