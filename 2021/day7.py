data = [int(i) for i in open("day7_input.txt").read().split(",")]
#print(data)
m, m2 = 999999999999, 999999999999

for i in range(max(data)):
    x = abs(sum([(i-d) for d in data if d < i]) + sum([(d-i) for d in data if d > i]))
    x2 = abs(sum([(i-d)*(i-d+1)/2 for d in data if d < i]) + sum([(d-i)*(d-i+1)/2 for d in data if d > i]))
    if x < m:
        m = x
    if x2 < m2:
        m2 = x2
print(m, int(m2))  
