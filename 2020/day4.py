data = open("input_day4.txt").read().splitlines()
data.append("")
d1=[]
valid1,valid2=0,0
for d in data:
    if d == "":
        if len(d1) == 7:
            valid1+=1
            v=0
            for d2 in d1:
                if ( ( (d2[0] == "byr") and (int(d2[1]) >=1920) and (int(d2[1])<=2002) )
                or ( (d2[0] == "iyr") and (int(d2[1]) >=2010) and (int(d2[1])<=2020) )
                or ( (d2[0] == "eyr") and (int(d2[1]) >=2020) and (int(d2[1])<=2030) )
                or ( (d2[0] == "hgt") and (d2[1][-2:]=="cm") and (int(d2[1][:-2])>=150) and (int(d2[1][:-2])<=193) )
                or ( (d2[0] == "hgt") and (d2[1][-2:]=="in") and (int(d2[1][:-2])>=59) and (int(d2[1][:-2])<=76) )
                or ( (d2[0] == "hcl") and (len(d2[1])==7) )
                or ( (d2[0] == "ecl") and (d2[1] in ["amb","blu","brn","gry","grn","hzl","oth"]) )
                or ( (d2[0] == "pid") and (len(d2[1]) == 9) ) ):
                    v+=1
                else:
                    break
            if v == 7:
                valid2+=1
        d1=[]
    else:
        for i in d.split():
            if i[:3] != "cid":
                d1.append(tuple(i.split(":")))

print("part 1:", valid1," part 2:", valid2)