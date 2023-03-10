l = ['debut', 'milieu', 'fin']

if (len(l) >= 1):
    tmp = l[0]
    l[0] = l[len(l) - 1]
    l[len(l) - 1] = tmp
