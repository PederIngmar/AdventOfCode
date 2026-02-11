import itertools
import math

with open("day8_input.txt") as file:
    data = file.read().splitlines()

box_xyz = [tuple(int(i) for i in d.split(",")) for d in data]
pairs = itertools.combinations(range(len(box_xyz)), 2)

def box_distance(box1, box2):
    x1, y1, z1 = box1
    x2, y2, z2 = box2
    r = (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2
    return r

sorted_pairs = sorted(pairs, key=lambda pair: box_distance(box_xyz[pair[0]], box_xyz[pair[1]]))
circuits = [set(p) for p in sorted_pairs]

def connect_circuit(connected_circuits, new_circuit):
    changed = False
    connected_circuit = new_circuit.copy()
    remaining = []
    for circuit in connected_circuits:
        if circuit & new_circuit:
            connected_circuit |= circuit
            changed = True
        else:
            remaining.append(circuit)

    remaining.append(connected_circuit)
    return remaining


connected_circuits = []
for circuit in circuits[:1000]:
    connected_circuits = connect_circuit(connected_circuits, circuit)

circuit_lengths = [len(c) for c in connected_circuits]
answer = math.prod(sorted(circuit_lengths)[-3:])
print("Part 1: ", answer)

connected_circuits = []
i = 0
new_circuit = circuits[i]
while (len(connected_circuits) != 1 or i < 1000):
    new_circuit = circuits[i]
    connected_circuits = connect_circuit(connected_circuits, new_circuit)
    i += 1

#print(circuit)
#print(connected_circuits)
i, j = new_circuit
x1, y1, z1 = box_xyz[i]
x2, y2, z2 = box_xyz[j]
print("Part 2: ", x1*x2)
