L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
my_min = L[0]
my_max = L[0]

for i in L:
    if i <= my_min:
        my_min = i
    if i >= my_max:
        my_max = i