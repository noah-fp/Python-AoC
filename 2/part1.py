data = open('2/input.txt','r')
lines = data.readlines()
floor_safety = []

def difference_check(numbers):
        line_diff = []
        for i in range(len(numbers)-1):
            diff = abs(numbers[i] - numbers[i+1])
            line_diff.append(diff)
        return line_diff
            
def sequence_check(numbers):
    increasing = 1
    decreasing = 1
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i + 1]:
            increasing = 0
        if numbers[i] < numbers[i + 1]:
            decreasing = 0
        con_change = increasing + decreasing
    return con_change

def safety_check(line_diff, con_change):
    if min(line_diff) > 0 and max(line_diff) < 4 and con_change:
        return 1
    else:
        return 0

for line in lines:
    numbers = list(map(int,line.split()))
    line_diff = difference_check(numbers)
    con_change = sequence_check(numbers)
    floor_safety.append(safety_check(line_diff,con_change))

print(sum(floor_safety))