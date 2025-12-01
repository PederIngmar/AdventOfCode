data= [int(d) for d in open("input_day1.txt").read().splitlines()]
k,j =0,0
for a in data:
    for b in data:
        if a+b==2020 and a!=b and k==0:
            print("part 1:", a*b)
            k=1
        for c in data:
            if a+b+c==2020 and (a!=b) and (a!=c) and (b!=c) and j==0:
                print("part 2", a*b*c)
                j=1
