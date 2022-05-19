from licz_czas import licz_czas
from tablice.los_pos import losowa_posortowana
from tablice.los_niepos import losowa_nieposortowana
from tablice.los_pos_odwrotnie import losowa_odwrotnie_posortowana

def qs(A, p, r):
    if p<r:
        q = partition(A, p, r)
        qs(A, p, q-1)
        qs(A, q+1, r)


def partition(A, p, r):
    x=A[r]
    i=p-1
    for j in range(p, r):
        if A[j] <= x:
            i= i+1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


# A[1], A[0] = A[0], A[1]  - zamiana


# qs(A, 0, len(A)-1)

# print(A)

try:
    los_niepos = licz_czas(qs, losowa_nieposortowana, 0, len(losowa_nieposortowana)-1)
    print("Czas wykonania (losowa nieposortowana): ", los_niepos)
except:
    print("Czas wykonania (losowa nieposortowana): ", "Nie udalo sie, limit wywolan rekurencji")

try:
    los_pos = licz_czas(qs, losowa_posortowana, 0, len(losowa_posortowana)-1)
    print("Czas wykonania (losowa posortowana): ", los_pos)
except:
    print("Czas wykonania (losowa posortowana): ", "Nie udalo sie, limit wywolan rekurencji")

try:
    los_odwrotnie = licz_czas(qs, losowa_odwrotnie_posortowana, 0, len(losowa_odwrotnie_posortowana)-1)
    print("Czas wykonania (losowa odwrotnie posortowana): ", los_odwrotnie)
except:
    print("Czas wykonania (losowa odwrotnie posortowana): ", "Nie udalo sie, limit wywolan rekurencji")