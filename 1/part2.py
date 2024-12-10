data = open('1/input.txt','r')
list1 = []
list2 = []
for line in data:
    value1, value2 = line.split()
    list1.append(value1)
    list2.append(value2)
list1 = list(map(int,list1))
list2 = list(map(int,list2))
simi_list = []
for i in range(len(list1)):
    count_sim = list2.count(list1[i])
    simi_score = list1[i] * count_sim
    simi_list.append(simi_score)
list_simi_score = sum(simi_list)
print('Total list Similarity Score: ',list_simi_score)