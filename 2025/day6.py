import numpy as np

with open("day6_input.txt") as file:
    data = file.read().splitlines()

homework = np.array([d.split() for d in data]).T
#print(homework)
    
solutions_sum = 0
for problem in homework:
    if problem[-1] == "*":
        solution = int(problem[0]) * int(problem[1]) * int(problem[2]) * int(problem[3])
    elif problem[-1] == "+":
        solution = int(problem[0]) + int(problem[1]) + int(problem[2]) + int(problem[3])

    solutions_sum += solution

print("Part 1: ", solutions_sum)

homework = np.array([list(d) for d in data[:-1]]).T
homework = [''.join(d) for d in list(homework)]

group = []
homework_nums = []
for num in homework:
    if num == '    ':
        homework_nums.append(group)
        group = []
    else:
        group.append(int(num))

homework_nums.append(group)

homework_signes = data[-1].split()
#print(len(homework_nums))
#print(len(homework_signes))
#print(homework_nums)
#print(homework_signes)

import math
solutions_sum = 0
for num, sign in zip(homework_nums, homework_signes):
    if sign == "*":
        solution = math.prod(num)
    elif sign == "+":
        solution = sum(num)
    solutions_sum += solution

print("Part 2: ", solutions_sum)
