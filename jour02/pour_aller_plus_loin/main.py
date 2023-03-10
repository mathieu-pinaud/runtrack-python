def triangle(a, b, c):
    if ((a + b <= c) or (a + c <= b) or (b + c <= a)):
        print("on ne peut pas construire de triangle")
        return
    if (a == b == c):
        print('le triangle est equilatéral')
        return
    test_rec = 0
    if ((a * a + b * b == c * c) or (a * a + c * c == b * b) or (b * b + c * c == a * a)):
        test_rec = 1
    if (a == b or a==c or b==c):
        if(test_rec ==1):
            print('le triangle est isocele rectangle')
        else:
            print('le triangle est isocele')
        return
    if (test_rec == 1):
        print('le triangle est rectangle')
        return
    print('le triangle est quelconque')