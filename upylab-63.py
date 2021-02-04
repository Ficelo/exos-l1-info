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
