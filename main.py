import random
rand = random.SystemRandom()

nImprevisti = 17
pesi = {"Legno":20, "Metallo":26, "Olio":6, "Pezzi di animale":3,
        "Pietra":3, "Plastica":3, "Polvere alimentare":6, "Silicio":9,
        "Solvente":12, "Sostanza chimica":6, "Stoffa":3, "Vegetale":6}
deck = []

for materiale in pesi:
    for n in range(pesi[materiale]):
        deck.append(materiale)

for n in range(nImprevisti):
    deck.append("Imprevisto")

def genQualita():
    qualita = rand.randint(0,9)
        if qualita < 2:
            return("Brutto")
        elif qualita < 5:
            return("Scarso")
        elif qualita < 8:
            return("Buono")
        else:
            return("Bello")
while 1:
    carta = deck[rand.randint(0, len(deck)-1)]
    print(carta)
    if carta != "Imprevisto":
        print(genQualita)
    if (input()):
        exit()