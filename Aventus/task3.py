from collections import defaultdict


list = ["random words paper place words butterfly compiler then there words "]

temp = defaultdict(int)

for i in list:
    for wrd in i.split():
        temp[wrd] += 1

newlist = max(temp , key=temp.get)


print("Word with maximum frequency : " + str(newlist))