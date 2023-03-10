def my_cript(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    j = 0
    res = ''

    for i in range(len(str)):
        while (alphabet[j] != str[i]):
            j += 1
        if (j + 3 > 25):
            j = (j + 3) % 25
            res += alphabet[j]
        else :
            res += alphabet[j + 3]
        j = 0
    return(res)

print(my_cript('bonzour'))
