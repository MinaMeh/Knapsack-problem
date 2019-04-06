def knapsack_dp(items, C):
    # order by max value per item weight
    items = sorted(items, key=lambda item: item[VALUE] / float(item[WEIGHT]), reverse=True)

    # Sack keeps track of max value so far as well as the count of each item in the tab
    tab = [(0, [0 for i in items]) for i in range(0, C + 1)]  # value, [item tab]

    for i, item in enumerate(items):
        name, weight, value = item
        for c in range(weight, C + 1):
            tabbefore = tab[c - weight]  # previous max tab to try adding this item to
            new_value = tabbefore[0] + value
            used = tabbefore[1][i]
            if tab[c][0] < new_value:
                # old max tab wi        th this added item is better
                tab[c] = (new_value, tabbefore[1][:])
                tab[c][1][i] += 1  # use one more

    value, bagged = tab[C]
    numbagged = sum(bagged)
    weight = sum(items[i][1] * n for i, n in enumerate(bagged))
    # convert to (iten, count) pairs) in name order
    bagged = sorted((items[i][NAME], n) for i, n in enumerate(bagged) if n)
    return value, weight, bagged

NAME, WEIGHT, VALUE = range(3)

capacity= int(input("Donnez la capacité du sac à dos: "))
nbr= int(input("Donnez le nombre d'objets: "))
items= []
for i in range(nbr):
    name=input("nom de l'objet: ")
    weight=int(input("poids de l\'objet: "))
    value=int(input("valeur de l\'objet: "))
    items.append([name,weight,value])

print(items)
print (knapsack_dp(items,capacity))
