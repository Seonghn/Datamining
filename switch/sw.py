sw = []

with open('15f.txt','r') as f:
    for i in f.readlines():
        sw.append(i)
print(sw)

sw2=[]
for i in sw:
    if i.find('[label=') != -1:
        if i.find('"gi') == -1:
            j = i.split(' [label="')
            print(j)
            sw2.append(j[0] + "//" + j[1].split('\\ngini')[0])
        else:
            j = i.split(' [label="')
            sw2.append(j[0] + "//x")

print(sw2)
print(len(sw2))