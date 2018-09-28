def kwadraten_som(grondgetallen):
    result = 0
    for getal in grondgetallen:
        if getal > 0:
            kwadrant = getal**2
            result = result + kwadrant
    return result

lijst = [2,3,4,-1,-2]
print( kwadraten_som(lijst))


