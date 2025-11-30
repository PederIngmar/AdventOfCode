with open("day7_input.txt") as file:
    data = file.read().splitlines()

D = {}
current_dir = []
d = 0

while d < len(data):
    if data[d][:4] == "$ cd":
        if data[d][5:] == "..":
            current_dir.pop(-1)
        elif data[d][5:] == "/":
            current_dir = ["/"]
        else:
            current_dir.append(data[d][5:])
        if "#".join(current_dir) not in D.keys():
                D["#".join(current_dir)] = []
        d+=1
    if data[d][:4] == "$ ls":
        d+=1
        while (d < len(data)) and (data[d][:4] != "$ cd"):
            if data[d][:3] != "dir":
                for c in range(1,len(current_dir)+1):
                    nokkel = "#".join(current_dir[:c])
                    D[nokkel].append(int(data[d].split(" ")[0]))
            d+=1            

disk_space = [sum(D[d]) for d in D]
print("part 1: ", sum([i for i in disk_space if i < 100000]))

unused_diskspace = 70000000-sum(D["/"])
for d in sorted(disk_space):
    if d >= 30000000 - unused_diskspace:
        print("part 2: ", d)
        break