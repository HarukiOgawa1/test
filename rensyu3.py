def kaijo(n):
    if n == 1:
        return n
    return n * kaijo(n-1)
num = 5
print(num,"の階乗は",kaijo(num))


