def standaardprijs(afstandKM):
    if afstandKM <= 0:
        return 0
    elif afstandKM < 50 and afstandKM > 0:
        prijs = afstandKM * 0.80
        return prijs
    else:
        prijs = 15 + (afstandKM - 50) * 0.60
        return prijs


def ritprijs(leeftijd, weekendrit, afstandKM):
    if leeftijd < 12 or leeftijd >= 65:
        prijs = standaardprijs(afstandKM) * 0.70
    elif (leeftijd < 12 or leeftijd >= 65) and weekendrit:
        prijs = standaardprijs(afstandKM) * 0.65
    elif weekendrit:
        prijs = standaardprijs(afstandKM) * 0.60
    else:
        prijs = standaardprijs(afstandKM)
    return prijs


Leeftijd = int(input('Wat is je leeftijd? '))
Weekend = input('Is het in het weekend? ')
Weekend = True if Weekend == 'ja' else False
Afstand = int(input('Hoeveel kilometer heb je afgelegd? '))


print('Jouw rit kost ' + str(ritprijs(Leeftijd,Weekend,Afstand)) + ' euro.' )
