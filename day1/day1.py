from collections import Counter

list1 = []
list2 = []

with open("input.txt", "r") as file:
    for line in file:
        num1, num2 = line.split()
        list1.append(int(num1))
        list2.append(int(num2))

list1.sort()
list2.sort()

total_dist = 0
for n1, n2 in zip(list1, list2):
    total_dist += abs(n1 - n2)

print("Total Distance: ", total_dist)

similarity_score = 0
list2_dict = Counter(list2)

for num1 in list1:
    if num1 in list2_dict:
        similarity_score += num1 * list2_dict[num1]

print("Similarity score: ", similarity_score)



