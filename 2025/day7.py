with open("day7_input.txt") as file:
    data = file.read().splitlines()

#print(data)
beam_start = data[0].find("S")
beams = {beam_start}
data_width = len(data[0])
split_count = 0
timelines = [0 for i in range(data_width)]
timelines[beam_start] = 1

for row in data[1:]:
    new_beams = set()
    for beam in beams:
        if row[beam] == "^":
            split_count += 1
            new_beams.add(beam-1)
            new_beams.add(beam+1)
            timelines[beam-1] += timelines[beam]
            timelines[beam+1] += timelines[beam]
            timelines[beam] = 0
        else:
            new_beams.add(beam)

    beams = new_beams

print("Part 1: ", split_count)
print("Part 2: ", sum(timelines))