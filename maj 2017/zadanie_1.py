A = [4, 34, 16, 8, 6, 22, 14, 12, 2, 7 ]
n = 6
p = 2

def zad1(A, n, p):
    nowe_A = []

    for liczba in A:
        if liczba % p != 0: # nie jest podzielne przez p
            nowe_A.append(liczba)

    nowe_A = sorted(nowe_A, reverse=True)

    if len(nowe_A) < 2:
        return 0

    return nowe_A[0]*nowe_A[1]

print(zad1(A,n,p))
