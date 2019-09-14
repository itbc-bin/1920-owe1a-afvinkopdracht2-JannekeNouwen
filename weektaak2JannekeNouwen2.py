#author: Janneke Nouwen

#eerst wordt gevraagd van welk bestand je het gc% en het aantal nucleotiden wilt weten
bestand = input("Van welk bestand je het gc% en het aantal nucleotiden weten? ")  

#dit is een functie genaamd fasta om het fasta bestand te kunnen lezen en de benodigde gegevens eruit te halen
def fasta (lines):
    #er wordt een variabele aangemaakt, waarin straks de sequentie wordt opgeslagen
    sequentie = ""
    for line in lines:
        #als de regel die wordt gelezen niet begint met ">", is het dus onderdeel van de sequentie
        if not line.startswith(">"):
            #de enters worden nu uit de sequentie gehaald met line.rstrip("\n")
            sequentie += line.rstrip("\n")
    #het resultaat van de functie moet de DNA sequentie zijn
    return sequentie

#de inhoud van de variabele "sequentie" moet de inhoud van het fasta bestand zijn,
#maar eerst wordt het bestand uiteengetrokken in lines, op de plekken waar enters zitten
#op die manier kan de funtie straks iedere line apart bekijken,
#en kijken of het een sequentie is, of de naam van de fasta
sequentie = fasta(open(bestand, "r").read().split("\n"))

#het aantal "G" en het aantal "C" wordt getelt en bij eklaar opgeteld
#dit wordt opgeslagen in de variabele "aantal_gc"
aantal_gc = sequentie.count("C") + sequentie.count("G")
#de lengte van de sequentie wordt bepaalt, Dit is 100%
#hiermee wordt het gc% berekend
procent_gc = aantal_gc * 100 / len(sequentie)
#vervolgens worden de berekende gegevens geprint om de resultaten aan de gebruiker te weergeven
print("Het aantal nucleotiden in deze sequentie is: " + len(sequentie))
print("Het gc% is: " + procent_gc + "%")
