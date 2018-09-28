stations = ['Schagen', 'Heerhugowaard','Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk','Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', "’s-Hertogenbosch", 'Eindhoven', 'Weert', 'Sittard', 'Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)

def inlezen_beginstation(stations):
    beginstation = input('Wat is uw beginstation? ')
    if beginstation in stations:
        return stations
    else:
        beginstation = input('Wat is uw beginstation? ')

def inlezen_eindstation(stations, beginstation):
    eindstation = input ('Wat is uw eindstation? ')
    if eindstation >= beginstation:
        return stations
    else:
        return input('Dit station is niet in dit traject... Wat is uw eindstation? ')

def omroepen_reis(stations, beginstation, eindstation):


