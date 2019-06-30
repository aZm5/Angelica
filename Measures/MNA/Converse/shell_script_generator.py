f=open("bit_score_generator.sh","w")
#X=["cat",'cow','dog','guinea_pig','sheep',"rabbit","rat","pig","mouse","horse"]
X=['human','cow','rta','dog','mouse','cat','guinea_pig','sheep','rabbit','pig', 'horse']


d={'cat': 12,'cow': 8,'dog': 13,'guinea_pig': 14, 'sheep': 11, 'rabbit': 15, 'rta': 2, 'pig': 10, 'mouse': 3, 'horse': 9,'human':1}
s=set()

#11: 11*10/2=55 55+11 => 66


for x in d:
    for y in d:
        s.add("-".join(sorted([x,y])))



print(s)
print(len(s))
f.write("#!/bin/bash\n")
for each in sorted(s):
    sp1,sp2=each.split("-")
    #f.write(f"s1={sp1};s2={sp2};\n")
    #f.write("echo ${"+"s1"+"}_${"+"s2"+"}\n")
    #f.write("awk '{print $"+str(d[sp1])+",$"+str(d[sp2])+"}' $Max | fgrep -f - ${"+"s1"+"}-${"+"s2"+"}.align | wc -l\n")
    #f.write("awk '$"+str(d[sp1])+" != "+'"NA" && $'+str(d[sp2])+" != "+'"NA" {print $'+str(d[sp1])+",$"+str(d[sp2])+"}' $Max | wc -l\n")
    f.write(f"cat {each} | awk '!a[$1"+ '" "$2]++{print}'+"'  > ../Converse/uniq_simility/" + f"{sp1}-{sp2}")
    f.write("\n")
    
f.close()
