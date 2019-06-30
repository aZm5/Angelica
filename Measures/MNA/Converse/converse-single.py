import pickle

# d={'human':1,'mouse': 3,'rta': 2}
d = {'cat': 12, 'cow': 8, 'dog': 13, 'guinea_pig': 14, 'sheep': 11, 'rabbit': 15, 'rta': 2, 'pig': 10, 'mouse': 3,
     'horse': 9, 'human': 1}
s = set()

# 11: 11*10/2=55 55+11 => 66


for x in d:
    y=x
    s.add("-".join(sorted([x, y])))
print(s)

for each in sorted(s):
    sp1, sp2 = each.split("-")

    first_net = open(f"./dict/{sp1}_dict", "rb")
    second_net = open(f"./dict/{sp2}_dict", "rb")

    first_net = open(f"./dict/{sp1}_dict", "rb")
    second_net = open(f"./dict/{sp2}_dict", "rb")

    dFirst = pickle.load(first_net)
    dSecond = pickle.load(second_net)

    # print(dFirst)

    f = open(f"./uniq_simility/{each}", "r")
    f1 = open(f"./Eval_sim_by_tab/{sp1[0:2]}-{sp2[0:2]}.sim", "w")  # "\t"
    f2 = open(f"./Eval_sim_by_white/{sp1[0:2]}-{sp2[0:2]}.sim", "w")  # " "


    # f3=open("human-mouse.txt","w")# " "

    for line in f:
        #    print(line)i
        Saved = set()
        # print(line.lstrip().rstrip().split(' '))
        p1, p2, a, b, c, bit_score, evalue = line.lstrip().rstrip().split(' ')
        if p1 in dFirst.keys() and p2 in dSecond.keys() and p1 + p2 not in Saved:
            Saved.add(p1 + p2)
            # if 'Q8NB50'+'D3Z901' in Saved:
            #     print('!')
            f1.write(f"{dFirst[p1]}\t{dSecond[p2]}\t{evalue}\n")
            f2.write(f"{dFirst[p1]} {dSecond[p2]} {evalue}\n")

