w = int(input("donnez la largeur "))
h = int(input("donnez la longueur "))

def my_draw_rec(width):
    for i in range(width):
        if (i == 0 or i == width - 1):
            print('+', end='')
        else:
            print('|', end= '')
        for j in range(width - 2):
            if (i == 0 or i == width - 1):
                print('-', end='')
            else:
                if(j == width - i - 2):
                    print(' ', end='')
                else:
                    print('#', end='')
        if (i == 0 or i == width - 1):
            print('+')
        else:
            print('|')

my_draw_rec(w)