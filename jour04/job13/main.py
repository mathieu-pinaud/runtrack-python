def my_append(liste, i):
    liste += [i]
    return(liste)

def my_len(list):
    stop = 0
    for i in list:
        stop += 1
    return(stop)

L = [10,20,30,20,10,50,60,40,80,50,40]
new_l = []
i = 0

while i < my_len(L):
    if (L[i] not in new_l):
        my_append(new_l, L[i])
    i += 1
print(new_l)