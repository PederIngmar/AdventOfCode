import itertools

with open("day5_input.txt") as file:
    database = file.read().split("\n\n")
    
fresh_ingrediant_ranges = set([tuple([int(id) for id in d.split("-")]) for d in database[0].splitlines()])
availible_ingrediants = [int(id) for id in database[1].splitlines()]

#print(fresh_ingrediant_ranges)
#print(availible_ingrediants)

n_availble_fresh_ingrediants = 0
for id in availible_ingrediants:
    for ing_range in fresh_ingrediant_ranges:
        ing_range_min, ing_range_max = ing_range
        if (id > ing_range_min) and (id < ing_range_max):
            n_availble_fresh_ingrediants += 1
            break

print("Part 1: ", n_availble_fresh_ingrediants)

# Making ranges without overlaps
range_set = set(fresh_ingrediant_ranges)
progress_flag = True

while progress_flag:
    progress_flag = False
    #print(len(range_set))

    for pair in itertools.combinations(range_set, 2):
        range1, range2 = pair
        range1_min, range1_max = range1
        range2_min, range2_max = range2
        new_range = tuple()

        range1_min_in_range2 = (range1_min <= range2_max) and (range1_min >= range2_min)
        range1_max_in_range2 = (range1_max >= range2_min) and (range1_max <= range2_max)
        range2_min_in_range1 = (range2_min <= range1_max) and (range2_min >= range1_min)
        range2_max_in_range1 = (range2_max >= range1_min) and (range2_max <= range1_max)
        range1_in_range2 = range1_min_in_range2 and range1_max_in_range2
        range2_in_range1 = range2_min_in_range1 and range2_max_in_range1

        if range1_in_range2:
            new_range = range2
        elif range2_in_range1:
            new_range = range1
        elif range1_min_in_range2:
            new_range = (range2_min, range1_max)
        elif range1_max_in_range2:
            new_range = (range1_min, range2_max)
        else:
            continue

        #print(range1, range2, new_range)
        range_set.remove(range1)
        range_set.remove(range2)
        range_set.add(new_range)
        progress_flag = True
        break

total_n_ids = 0
for r in range_set:
    #print(r)
    range_min, range_max = r
    total_n_ids += range_max-range_min+1

print("Part 2: ", total_n_ids)