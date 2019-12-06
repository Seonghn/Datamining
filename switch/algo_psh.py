depth = 16
d_list = []
for i in range(0, depth+1):
    c = 2 ** i
    d_list.append(c)
print(d_list)
fn = [[1, 0],[2, 0],[4, 0],[8, 0],[16, 0],[32, 0]]
#     ,[64, 0],[128, 0]
# ,[256, 0]
# ,[512, 0]
# ,[1024, 0]
# ,[2048, 0]
# ,[4096, 0]
# ,[8192, 0]
# ,[16384, 0]
# ,[32768, 0]
# ,[65536, 0]
# ,[131072, 0]
# ,[262144, 0]
# ,[524288, 0]
# ,[1048576, 0]
# ,[2097152, 0]
# ,[4194304, 0]
# ,[8388608, 0]]
fn0=[1, 0]
fn1=[2, 0]
fn2=[4, 0]
fn3=[8, 0]
fn4=[16, 0]
fn5=[32, 0]
fn6=[64, 0]
fn7=[128, 0]
fn8=[256, 0]
fn9=[512, 0]
fn10=[1024, 0]
fn11=[2048, 0]
fn12=[4096, 0]
fn13=[8192, 0]
fn14=[16384, 0]
fn15=[32768, 0]
fn16=[65536, 0]
fn17=[131072, 0]
fn18=[262144, 0]
fn19=[524288, 0]
fn20=[1048576, 0]
fn21=[2097152, 0]
fn22=[4194304, 0]
fn23=[8388608, 0]

ar = []
with open('15f.txt','r') as f:
    for i in f.readlines():
        if i.find('->') != -1:
            if i.find(' [la') != -1:
                ar.append(i.split(' [la')[0])
            else:
                ar.append(i.split(' ;')[0])
print(ar)

node = [[0, 1]]
d = 1
for i in ar:
    a = int(i.split(' -> ')[0])
    b = int(i.split(' -> ')[1])
    if b-a==1:
        for j in node:
            if j[0]==a:
                d = j[1] * 2
                node.append([b, d])
    # elif b-a==2:
    #     # for i in node:
    #     #     if i[0] == a:
    #     #         d=i[1]*2+1
    #     #         node.append([b,d])
    #     node.append([b,d+1])
    else:
        # ab = node[a][1]
        # node.append([b,ab*2+1])
        for k in node:
            if k[0]==a:
                d = k[1] * 2 + 1
                node.append([b, d])
print(node)