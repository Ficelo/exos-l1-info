def calcul_prix(produits, catalogue):
    prix_total = 0
    for element in produits:
        prix_total += produits[element] * catalogue[element]
    return prix_total

