L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

def my_len(list):
    stop = 0
    for i in list:
        stop += 1
    return(stop)

def my_arrondi(i):
    for j in range(2):
        if (i % 10 < 5):
            i -= i % 10
        else:
            i -= i % 10 + 10
        i /= 10
    return(i)


for i in range(len(L)):
    L[i] *= 100
    L[i] = my_arrondi(L[i])

print(L)
