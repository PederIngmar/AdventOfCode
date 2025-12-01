data=open("input_day3.txt").read().splitlines()
def slope(x,y):
    X,Y,c = 0,0,0
    while Y<len(data):
        if data[Y][X%len(data[0])] == "#":
            c+=1
        X+=x
        Y+=y
    return c
print("part 1:",slope(3,1), "part 2:", slope(3,1)* slope(1,1)* slope(5,1)*slope(7,1)*slope(1,2))