str = input('donnez un mot ')
res = ''
i = len(str) - 1
while (i >= 0):
    res += str[i]
    i -= 1
print(res)

# def my_for_rev_str(str):
#     res = ''
#     for i in range(len(str) -1, -1, -1):
#         res += str[i]
#     print(res)

# my_for_rev_str(str)