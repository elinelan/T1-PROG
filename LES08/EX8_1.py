infile = open('EX8_1.txt', 'r')
regels = infile.readlines()
infile.close()
#print (regels)

outfile = open('kaartnummersuit.txt', 'w')
for regel in regels:
    kaartinfo = regel.split(', ')
    outfile.write('{} heeft kaartnummer: {}\n'.format(kaartinfo[1].strip(), kaartinfo[0]))
outfile.close()
