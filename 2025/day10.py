import itertools
import math

with open("day10_input_tst.txt") as file:
    data = file.read().splitlines()

n_presses_part1 = 0
n_presses_part2 = 0
for d in data:
    problem = d.split(" ")
    lights = tuple(1 if light=="#" else 0 for light in problem[0][1:-1])
    buttons = [tuple(int(n) for n in button[1:-1].split(",")) for button in problem[1:-1]]
    joltage_requirement = tuple(int(n) for n in problem[-1][1:-1].split(","))

    press_list = tuple(b for i in range(1, len(buttons)) for b in itertools.combinations(buttons, i))

    for presses in list(press_list):
        current_lights = list(lights)
        for press in presses:
            for light in press:
                current_lights[light] = not(current_lights[light])

        if all(x == 0 for x in current_lights):
            n_presses_part1 += len(presses)
            break

    joltage_solutions = {}
    joltages = [0 for i in range(len(joltage_requirement))]

    def reach_joltage_requirement(joltages, joltage_requirement):
        if joltages in joltage_solutions:
            return joltage_solutions[joltages]
        
        for button in buttons:
            for light in button:
                if joltages[light] >= joltage_requirement[light]:
                    break
                joltages[light] += 1
                reach_joltage_requirement(joltages, joltage_requirement)


                if all(joltages[i] < joltage_requirement[i] for i in range(len(joltage_requirement))):
                    n_presses_part2 += len(presses)
                    break
    

print("Part 1: ", n_presses_part1)
print("Part 2: ", n_presses_part2)