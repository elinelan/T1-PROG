leeftijd = eval(input ('Wat is je leeftijd? '))
if leeftijd < 18:
    print ('Je bent een kind')
elif leeftijd >= 18 and leeftijd < 65:
    print ('Je bent volwassen')
else:
    print('Je bent bejaard')