import itertools
import math

with open("day9_input.txt") as file:
    data = file.read().splitlines()

red_tiles_xy = [tuple(int(i) for i in d.split(",")) for d in data]
pairs = list(itertools.combinations(red_tiles_xy, 2))

def tile_area(tile1, tile2):
    x1, y1 = tile1
    x2, y2 = tile2
    r = (abs(x2-x1)+1)*(abs(y2-y1)+1)
    return r

pair_areas = [tile_area(*pair) for pair in pairs]
print("Part 1: ", max(pair_areas))

lines_x = []
lines_y = []
for i in range(len(red_tiles_xy)):
    tile1 = red_tiles_xy[i]
    tile2 = red_tiles_xy[i-1]
    x1, y1 = tile1
    x2, y2 = tile2
    if x1 == x2:
        lines_x.append(tuple((tile1, tile2)))
    elif y1 == y2:
         lines_y.append(tuple((tile1, tile2)))

sorted_pairs = sorted(pairs, key=lambda pair: tile_area(*pair), reverse=True)
answer_pair = 0
for pair in sorted_pairs:
    tile1, tile2 = pair
    x1, y1 = tile1
    x2, y2 = tile2

    min_x = min(x1, x2)
    max_x = max(x1, x2)
    min_y = min(y1, y2)
    max_y = max(y1, y2)

    overlap_flag = False

    for line in lines_x:
        (ax, ay), (bx, by) = line
        linex = ax
        ystart = min(ay, by)
        yend   = max(ay, by)

        if min_x < linex < max_x:
            if not (yend <= min_y or ystart >= max_y):
                overlap_flag = True
                break

    if not overlap_flag:
        for line in lines_y:
            (ax, ay), (bx, by) = line
            liney = ay
            xstart = min(ax, bx)
            xend   = max(ax, bx)

            if min_y < liney < max_y:
                if not (xend <= min_x or xstart >= max_x):
                    overlap_flag = True
                    break

    if not overlap_flag:
        answer_pair = pair
        break

area = tile_area(*answer_pair)
print("Part 2: ", area)
