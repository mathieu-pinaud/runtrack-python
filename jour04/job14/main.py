def my_len(list):
    stop = 0
    for i in list:
        stop += 1
    return(stop)

def my_long_word(min, str):
    i = 0
    while(i < my_len(str)):
        mot = ''
        while((str[i] != ' ') and (i < my_len(str) - 1)):
            mot += str[i]
            i += 1
        i += 1
        if (i == my_len(str)):
            mot += str[my_len(str) - 1]
        if(my_len(mot) > min):
            print(mot, end=' ')

my_long_word(3, "La peur est le chemin vers le côté obscur la peur mène à la colère la colère mène à la haine la haine mène à la souffrance")