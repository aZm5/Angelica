# from collections import Counter
import math
def fo(file_name):
    fo_dict={}
    file=open(file_name,'r')
    for lines in file.readlines():
        line=lines.rstrip().split('\t')
        if len(line)>1:
            fo_dict[line[0]]=line[1:]
    return fo_dict
A_fo=fo('./CG/A.fo')
B_fo=fo('./CG/B.fo')
C_fo=fo('./CG/C.fo')
D_fo=fo('./CG/D.fo')
E_fo=fo('./CG/E.fo')
F_fo=fo('./CG/F.fo')
G_fo=fo('./CG/G.fo')
H_fo=fo('./CG/H.fo')
def fo_map(data):
    if (data[0]).upper() == 'A':
        fo_dic = A_fo
    elif (data[0]).upper() == 'B':
        fo_dic = B_fo
    elif (data[0]).upper() == 'C':
        fo_dic = C_fo
    elif (data[0]).upper() == 'D':
        fo_dic = D_fo
    elif (data[0]).upper() == 'E':
        fo_dic = E_fo
    elif (data[0]).upper() == 'F':
        fo_dic = F_fo
    elif (data[0]).upper() == 'G':
        fo_dic = G_fo
    elif (data[0]).upper() == 'H':
        fo_dic = H_fo
    return fo_dic
'''
收集一个簇中不同的GO注释
'''
def go_set(cluster):
    save = set()
    for protein in cluster: #对簇中的每一个蛋白质进行操作
        fo_dic=fo_map(protein)
        if protein in fo_dic.keys():#如果该蛋白质有注释
            for i in fo_dic[protein]:
                save.add(i)  # 记录不同GO注释
    return list(save)

'''
计算ne
'''
def ne(cluster):
    # 找到簇中不同的Go注释
    GO_list=list(go_set(cluster))
    d = len(GO_list)
    p=0
    NE=0
    # 找出簇中被注释的蛋白质数目
    an_pro_num=0
    for pro in cluster:
        fo_dic = fo_map(pro)
        if pro in fo_dic.keys():
            an_pro_num=an_pro_num+1

    if d > 1:
        for term in GO_list:
            count = 0
            for data in each_cluster:  # 对簇中的每一个蛋白质进行操作
                ratio = 0
                fo_dic = fo_map(data)
                if data in fo_dic.keys() :
                    for each in fo_dic[data]:
                        if each == term:
                            count = count + 1  # 找到和此Go术语相同的蛋白质数目+1
            # ratio = count / len(each_cluster)  #分母为簇中蛋白质总数
            ratio = count/ an_pro_num   #分母为簇中被注释的蛋白质总数
            p = p + ratio * math.log(ratio)
        NE = -1 * (1 / math.log(d)) * p
    return NE





f=open('smetana_8CG_28.1s.txt','r')
# f=open('smetana.txt','r')
#对每一个簇进行操作
MNE=0

# 1.寻找被注释的簇
annotated_cluster=[]
cluster_number=0
for lines in f.readlines():
    cluster=lines.rstrip().split(' ')
    num=0
    for protein in cluster:
        fo_dic = fo_map(protein)
        if protein in fo_dic.keys():#蛋白质被注释了
            num = num + 1
        if num == 2:  # 至少两个蛋白质Go术语标注过
            break
    if num == 2:
        annotated_cluster.append(cluster)
        cluster_number = cluster_number + 1
print("注释簇数目：%d"%cluster_number)
print(annotated_cluster)



#计算MNE
mne=0
for each_cluster in annotated_cluster:
    NE=ne(each_cluster)
    mne=mne+NE
mne=mne/cluster_number
print(mne)






