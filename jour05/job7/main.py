mot = input('donnez un mot ')
i = 0
while i < len(mot):
    if mot[i] not in 'abcdefghijklmnopqrstuvwxyz':
        mot = input('saisie incorrecte, réessayez ')
        i = 0
    i += 1

def my_for_rev_str(str):
    res = ''
    for i in range(len(str) -1, -1, -1):
        res += str[i]
    return(res)

def my_cript(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    j = 0
    i = 0
    res = ''
    flag = 0

    while (i < len(str)):
        if (str[i] != 'z' and flag == 0):
            while (alphabet[j] != str[i]):
                j += 1
            res += alphabet[j + 1]
            flag = 1
        else:
            res += str[i]
        i += 1
    return(res)

print(my_for_rev_str(my_cript(my_for_rev_str(mot))))