l1 = []
l2 = []

with open("day1_input.txt") as lines:
    for line in lines:
        num1, num2 = map(int, line.split())
        l1.append(num1)
        l2.append(num2)


l1 = sorted(l1)
l2 = sorted(l2)

def distance(a, b):
    if a < b:
        return b-a
    else:
        return a-b

total = 0
for i in range(len(l1)):
    total += distance(l1[i], l2[i])

print(total)