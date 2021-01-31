def substitue(message, abreviation):
    mes = list(message.split(' '))
    for i in mes:
        if i in abreviation:
            message = message.replace(i, abreviation[i])
    return message

print(substitue('C. N. cpt 2 to inf', {'cpt': 'counted', 'C.': 'Chuck', 'inf': 'infinity', '2': '2 times', 'N.': 'Norris'}))