from licz_czas import licz_czas
from tablice.los_pos import losowa_posortowana
from tablice.los_niepos import losowa_nieposortowana
from tablice.los_pos_odwrotnie import losowa_odwrotnie_posortowana

def bubble_sort(tablica):
    n=len(tablica)
    while n>1:
        for i in range (0,n-1):
            if tablica[i]>= tablica[i+1]:
                tablica[i], tablica[i+1] = tablica[i+1], tablica[i]
        n=n-1

def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A




los_niepos = licz_czas(bubble_sort, losowa_nieposortowana)

print("Czas wykonania (losowa nieposortowana): ", los_niepos)

los_pos = licz_czas(bubble_sort, losowa_posortowana)

print("Czas wykonania (losowa posortowana): ", los_pos)

los_odwrotnie = licz_czas(bubble_sort, losowa_odwrotnie_posortowana)

print("Czas wykonania (losowa odwrotnie posortowana): ", los_odwrotnie)




# print(tab)