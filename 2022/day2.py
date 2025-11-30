data = open("day2_input.txt").read().splitlines()

outcomedict = {"A X":3, "A Y": 6, "A Z": 0, "B X": 0, "B Y":3, "B Z": 6, "C X": 6, "C Y": 0, "C Z":3}
RPCdict = {"X": 1, "Y": 2, "Z": 3}
score = 0
for d in data:
    score += outcomedict[d] + RPCdict[d[-1]]
print("part 1: ", score)


outcomedict2 = {"A X":3, "A Y": 1, "A Z": 2, "B X": 1, "B Y":2, "B Z": 3, "C X": 2, "C Y": 3, "C Z":1}
RPCdict2 = {"X": 0, "Y": 3, "Z": 6}
score2 = 0
for d in data:
    score2 += outcomedict2[d] + RPCdict2[d[-1]]
print("part 2: ", score2)
