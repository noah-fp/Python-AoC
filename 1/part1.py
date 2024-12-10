data = open('1/input.txt','r')
list1 = []
list2 = []
for line in data:
    value1, value2 = line.split()
    list1.append(value1)
    list2.append(value2)
list1.sort()
list2.sort()
list1 = list(map(int,list1))
list2 = list(map(int,list2))
differences = []
for i in range(len(list1)):
    result = abs(list1[i] - list2[i])
    differences.append(result)
total = sum(differences)
print('Total Distance: ',total)