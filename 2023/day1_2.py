import numpy as np

def findCalibrationSum(filename):
    with open(filename) as f:
        lines = f.readlines()

        sum = 0
        for line in lines:
            sum += valuePerLine(line)

        return sum
    
def valuePerLine(line):
    spelled = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for i in range(9):
        print(i)
        if spelled[i] in line:
            line.replace(spelled[i], str(i+1))
            

    st = ""
    for c in line:
        if c.isalpha():
            pass
        else:  
            st += c
            print(st)
            
    if len(st) == 0:
        return 0
    if len(st) == 1:
        return int(st)
    
    a = st[0]
    b = int(st)%10

    s = str(a) + str(b)

    print("returnerer: " + s)

    return int(s)

print(valuePerLine("one"))
#print("svaret er " + str(findCalibrationSum("input.txt")))
    