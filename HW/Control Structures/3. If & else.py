leeftijd = eval(input('Wat is je leeftijd? '))
paspoort = input('Ben je in bezit van een Nederlands paspoort? ')

if leeftijd >= 18 and (paspoort == 'ja' or paspoort == 'Ja'):
    print ('Je mag stemmen!')
else:
    print ('Je mag niet stemmen')