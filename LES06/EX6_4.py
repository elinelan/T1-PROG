def rng (lijst):
    res = max(lijst) - min(lijst)
    return res

lijst = [4,0,1,-2]
maxverschil = rng(lijst)

print (maxverschil) #or
print (rng(lijst))