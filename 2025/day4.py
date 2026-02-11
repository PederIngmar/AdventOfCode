
with open("day4_input.txt") as file:
    diagram = file.read().splitlines()

diagram = [list(d) for d in diagram]

forklift_accessible = 0
for r, row in enumerate(diagram):
    for c, cell in enumerate(row):
        if cell != '@': continue

        paper_neighbours = 0
        for dr in range(-1, 2):
            if (r + dr < 0) or (r + dr >= len(diagram)): continue
            for dc in range(-1, 2):
                if (dr == 0 and dc == 0): continue
                if (c + dc < 0) or (c + dc >= len(row)): continue
                if diagram[r+dr][c+dc] == '@':
                    paper_neighbours += 1
        
        if paper_neighbours < 4:
            forklift_accessible += 1


print("Part 1: ", forklift_accessible)

new_diagram = diagram.copy()
forklift_accessible = 1
paper_removed = 0

while forklift_accessible != 0:
    forklift_accessible = 0
    diagram = new_diagram.copy()

    for r, row in enumerate(diagram):
        for c, cell in enumerate(row):
            if cell != '@': continue

            paper_neighbours = 0
            for dr in range(-1, 2):
                if (r + dr < 0) or (r + dr >= len(diagram)): continue
                for dc in range(-1, 2):
                    if (dr == 0 and dc == 0): continue
                    if (c + dc < 0) or (c + dc >= len(row)): continue
                    if diagram[r+dr][c+dc] == '@':
                        paper_neighbours += 1
            
            if paper_neighbours < 4:
                new_diagram[r][c] = '.'
                paper_removed += 1
                forklift_accessible += 1

print("Part 2: ", paper_removed)