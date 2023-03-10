w = int(input("donnez la largeur "))
h = int(input("donnez la longueur "))

def my_draw_rec(width, height):
    for i in range(height):
        print('|', end= '')
        for j in range(width - 2):
            if (i == 0 or i == height - 1):
                print('-', end='')
            else:
                print(' ', end='')
        print('|')
print('caca')
my_draw_rec(w, h)