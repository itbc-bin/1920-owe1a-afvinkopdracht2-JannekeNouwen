#last edited: 11/09/2019 17.47
#author: Janneke Nouwen

bestand = open("genoom_Pan_paniscus.txt")
DNAsequentie = bestand.read()

aantal_gc = DNAsequentie.count("C") + DNAsequentie.count("G")

procent_gc = aantal_gc * 100 / len(DNAsequentie)

print (aantal_gc)
print (str(procent_gc) + " %")
