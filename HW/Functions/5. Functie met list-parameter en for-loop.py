def kwadraten_som(grondgetallen):
    if grondgetallen >= 0:
        som = sum(grondgetallen ** 2)
        return som

grondgetallen = [2,3,5,-2,-3]
res = kwadraten_som(grondgetallen)
print(res)



