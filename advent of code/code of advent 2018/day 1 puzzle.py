import math

data = open('frikvenser.txt').readlines()
frekvens = 0

frekvenslogg= []
seenonce = []
seentwice = []

melo = 0
for k in range(100):
    for linje in data:
        frekvens = frekvens + int(linje)
        frekvenslogg.append(frekvens + melo)
    
    melo = melo + 582
    
#print(frekvenslogg)    
    #print(str(linje) + "," + str(frekvens))


for linje in frekvenslogg:
    if linje not in seenonce:
        seenonce.append(linje)
        
    elif linje in seenonce:
        seentwice.append(linje)
        print("twice, " + str(linje))
            
    
print(seentwice)

    