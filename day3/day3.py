import re

pattern = r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"

string = ""
with open("input.txt", "r") as file:
    for line in file:
        string += line
expressions = re.findall(pattern, string)

total = 0

counting = True

for num1, num2, do, dont in expressions:
    if do:
        counting = True
    if dont:
        counting = False

    if num1 and num2 and counting:
        total += int(num1) * int(num2)

print("total", total)
