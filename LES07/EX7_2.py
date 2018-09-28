s = 'voorbeeeld'
print (s.capitalize())
print(s)
print(s.count('e'))
print(s.find('e'))
print(s.replace('e', 'a'))
print(s.lower())
print(s.upper())

s = '  voorbeeld  \n'
print(s.strip())

s = 'dit is een voorbeeld'
print(s.split())

s = 'dit-is-een-voorbeeld'
print(s.split())

woord = 'eenHeelErgLangWoord'
for letter in woord:
    print(letter, end = ' ')