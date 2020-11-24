import math

data = open('frikvenser.txt').readlines()
frekvens = 0

frekvenslogg= []
seenonce = []
seentwice = []

for linje in data:
    frekvens = frekvens + int(linje)
    frekvenslogg.append(frekvens)
    
    #print(str(linje) + "," + str(frekvens))


mellom = 0

for i in range(200):  
    for linje in frekvenslogg:
        if linje + mellom not in seenonce:
            seenonce.append(linje + frekvens)
            
        elif linje + mellom in seenonce:
            seentwice.append(linje + frekvens)
            print("twice, " + str(linje))
        mellom = mellom + 582
        
print(seentwice)

    