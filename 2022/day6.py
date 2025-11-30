with open("day6_input.txt") as file:
    data = list(file.read())[:-1]

def find_section_without_par(s, n):
    for i in range(0, len(s)-n+1, 1):
        l = s[i:i+n]
        if len(set(l)) == len(l):
            return i+n


print(find_section_without_par(data,4))
print(find_section_without_par(data,14))