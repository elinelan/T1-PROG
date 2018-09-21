getallenrij = [2,4,6,8,10,9,7]

zoekgetal = int(input('Voer een getal in: '))
gevonden = False

for getal in getallenrij:
    if getal == zoekgetal:
        gevonden = True

print (gevonden)