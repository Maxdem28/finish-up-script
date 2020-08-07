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

while 1:
    carta = deck[rand.randint(0, len(deck)-1)]
    print(carta)
    if carta != "Imprevisto":
        qualita = rand.randint(0,9)
        if qualita < 2:
            print("Brutto")
        elif qualita < 5:
            print("Scarso")
        elif qualita < 8:
            print("Buono")
        else:
            print("Bello")
    if (input()):
        exit()