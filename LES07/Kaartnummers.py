infile = open('EX8_1.txt', 'r')
regels = infile.readlines()
infile.close()
#print (regels)

for regel in regels:
    kaartinfo = regel.split(', ')
    #print (regel)
    #print(kaartinfo[0])
    #print(kaartinfo[1])
    print('{} heeft kaartnummer: {}'.format(kaartinfo[1].strip(), kaartinfo[0]))