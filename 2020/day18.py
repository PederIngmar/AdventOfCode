data = [d.replace(" ", "")+")" for d in open("input_day18.txt").read().splitlines()]

def summer(L, s, t):
    global i
    while L[i] != ")":
        if L[i] == "(":
            i += 1
            if t == "+":
                s += summer(L, 0, "+")
            elif t == "*":
                s = s*summer(L, 0, "+")
        elif L[i] == "+" or L[i] == "*":
            t = L[i]
        else:
            if t == "+":
                s += int(L[i])
            elif t == "*":
                s = s * int(L[i])
        i += 1
    return s

s = 0
for d in data:
    i = 0
    s += summer(d, 0, "+")

print("part 1:", s)

def summer2(L,s,t):
    global i
    while L[i] != ")":
        if L[i] == "(":
            i += 1
            if t == "+":
                if L[i-3] == "*":
                    print(L[i-2],L[i])
                    s = (s/int(L[i-2]))*(summer2(L, 0, "+")+int(L[i-2]))
                else:
                    s += summer2(L, 0, "+")
            elif t == "*":
                s = s*summer2(L, 0, "+")
        elif L[i] == "+" or L[i] == "*":
            t = L[i]
        else:
            if t == "+":
                if L[i-3] == "*":
                    s = (s/int(L[i-2]))*(int(L[i])+int(L[i-2]))
                else:
                    s += int(L[i])
            elif t == "*":
                s = s * int(L[i])
        i += 1
    return s


for d in data:
    i = 0
    print(d, summer2(d, 0, "*")