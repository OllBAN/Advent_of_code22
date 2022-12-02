import heapq

with open('aoc_1.txt') as f:
    list = f.readlines()

counter_list = []
counter = 0

for item in list:
    if item == "\n":
        counter_list.append(counter)
        counter = 0
    else:
        counter += int(item)


print(max(counter_list))
# print(heapq.nlargest(3, counter_list))
apa = sorted(counter_list, reverse=True)
print(apa[:3])
print(apa[0]+apa[1]+apa[2])
