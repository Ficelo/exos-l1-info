def top_3_candidats(moyenne):
    vals = list(moyenne.values())
    keys = list(moyenne.keys())
    ordered_vals = list(moyenne.values())
    ordered_vals.sort()
    meilleurs = []
    for i in range(-3, 0):
        pos = vals.index(ordered_vals[i])
        meilleurs.append(keys[pos])
    meilleurs.reverse()
    return tuple(meilleurs)

print(top_3_candidats({'Candidat 7': 2, 'Candidat 2': 38, 'Candidat 6': 85,
                 'Candidat 1': 8, 'Candidat 3': 17, 'Candidat 5': 83,
                 'Candidat 4': 33}))
