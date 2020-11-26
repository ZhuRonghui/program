# with open("file\\1.txt",encoding='UTF-8') as f:
#     p1 = f.readlines()
# for i in range (0,len(p1)):
#     p1[i] = str(i+1) + ' ' + p1[i]
# print(p1)
#
# with open("file\\2.txt",'w',encoding="UTF-8") as f1:
#     f1.writelines(p1)

import os

def count(fname):
    with open(fname,encoding='UTF-8') as f:
        p1 = f.readlines()
    print(fname + "\t" + str(len(p1)))

path = '../testdata'
for fname in os.listdir(path):
    if fname.endswith('.txt') or fname.endswith('.py'):
        file_path = os.path.join(path, fname)
        count(fname)

        if os.path.exists('../out'):
            os.mkdir('../'+fname)
