def my_len(list):
    stop = 0
    for i in list:
        stop += 1
    return(stop)

def my_append(liste, i):
    liste += [i]
    return(liste)

def my_supp_index(liste, index):
    new_l = []
    i = 0
    while (i < my_len(liste)):
        if (i != index):
            my_append(new_l, liste[i])
        i += 1
    return(new_l)

L = [7, 11, 42, 39, 2]
my_min = L[0]
res_L = []
j = 0

while (my_len(L) > 1):
    while (j < my_len(L)):
        if L[j] <= my_min:
            my_min = L[j]
            i_sup = j
        j += 1
    my_append(res_L, my_min)
    L = my_supp_index(L, i_sup)
    my_min = L[0]
    j = 0
    print(L)
my_append(res_L, L[0])

print(res_L)