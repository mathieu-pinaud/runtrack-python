# max_alpha = 'abcdefghijklmnopqrstuvwxyz' * 10
# cpt_ligne = 0
# cpt_char = 0
# k = 0

# while (k < len(max_alpha)):
#     while (cpt_char <= cpt_ligne and k < 260):
#         print(max_alpha[k], end='')
#         cpt_char += 1
#         k += 1
#     cpt_char = 0
#     cpt_ligne += 1
#     print('')


def for_aplha_tree():
    max_alpha = 'abcdefghijklmnopqrstuvwxyz' * 10
    cpt_ligne = 0

    for lettre in range(len(max_alpha)):
        for cpt_char in range(cpt_ligne), lettre < 260:
            print(max_alpha[lettre], end='')
        cpt_ligne += 1
        print()

for_aplha_tree()