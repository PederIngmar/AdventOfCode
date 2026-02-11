import numpy as np

with open("day2_input.txt") as file:
    data = file.read().splitlines()[0]

data = [d.split("-") for d in data.split(",")]

invalid_ids = set()
for id_range_start, id_range_end in data:
    #print("Range: ", id_range_start, id_range_end)
    id_length_mismatch = (len(id_range_start) < len(id_range_end))

    if (len(id_range_start) % 2) == 0:
        i = len(id_range_start) // 2
        id_gen_start = int(id_range_start[:i])
        if id_length_mismatch:
            id_gen_end = int('9'*i)
        else:
            id_gen_end = int(id_range_end[:i])

        for j in range(id_gen_start, id_gen_end + 1):
            invalid_id = int(str(j) * (len(id_range_start) // i))
            if ( invalid_id <= int(id_range_end) ) and ( invalid_id >= int(id_range_start) ):
                invalid_ids.add(invalid_id)

    elif id_length_mismatch:
        i = len(id_range_end) // 2
        id_gen_start = int('1'+'0'*(i-1))
        id_gen_end = int(id_range_end[:i])
        for j in range(id_gen_start, id_gen_end + 1):
            invalid_id = int(str(j) * (len(id_range_end) // i))
            if ( invalid_id <= int(id_range_end) ) and ( invalid_id >= int(id_range_start) ):
                invalid_ids.add(invalid_id)

#print(invalid_ids)
print("part 1: ", sum(list(invalid_ids)))


invalid_ids = set()
for id_range_start, id_range_end in data:
    #print("Range: ", id_range_start, id_range_end)
    id_length_mismatch = (len(id_range_start) < len(id_range_end))

    for i in range(1, len(id_range_start) // 2 + 1):
        if (len(id_range_start) % i) != 0: continue
        id_gen_start = int(id_range_start[:i])
        id_gen_end = int(id_range_end[:i])
        if id_length_mismatch:
            id_gen_end = int('9'*i)
        for j in range(id_gen_start, id_gen_end + 1):
            invalid_id = int(str(j) * (len(id_range_start) // i))
            if ( invalid_id <= int(id_range_end) ) and ( invalid_id >= int(id_range_start) ):
                invalid_ids.add(invalid_id)

    if id_length_mismatch:
        for i in range(1, len(id_range_end) // 2 + 1):
            if (len(id_range_end) % i) != 0: continue
            id_gen_start = int(id_range_start[:i])
            id_gen_end = int(id_range_end[:i])
            if id_length_mismatch:
                id_gen_start = int('1'+'0'*(i-1))
            for j in range(id_gen_start, id_gen_end + 1):
                invalid_id = int(str(j) * (len(id_range_end) // i))
                if ( invalid_id <= int(id_range_end) ) and ( invalid_id >= int(id_range_start) ):
                    invalid_ids.add(invalid_id)

#print(invalid_ids)
print("part 2: ", sum(list(invalid_ids)))
