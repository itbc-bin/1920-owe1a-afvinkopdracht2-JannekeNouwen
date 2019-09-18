p1 = float(input("Hoeveel kost het eerste product dat je gekocht hebt?"))
p2 = float(input("Hoeveel kost het tweede product dat je gekocht hebt?"))
p3 = float(input("Hoeveel kost het derde product dat je gekocht hebt?"))
p4 = float(input("Hoeveel kost het vierde product dat je gekocht hebt?"))
p5 = float(input("Hoeveel kost het vijfde product dat je gekocht hebt?"))

subtotaal = p1 + p2 + p3 + p4 + p5
BTW = subtotaal*0.07
totaal = BTW + subtotaal

print("Het subtotaal is " + str(subtotaal))
print("BTW: " + str(BTW))
print("Het totale bonbedrag is " + str(totaal))
