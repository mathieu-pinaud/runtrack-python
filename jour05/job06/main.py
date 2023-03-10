def luke_arrondi(l):
    for i in range(len(l)):
        if (l[i] % 5 >= 3):
            l[i] += 5 - (l[i] % 5)
    return(l)