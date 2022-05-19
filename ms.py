from licz_czas import licz_czas
from tablice.los_pos import losowa_posortowana
from tablice.los_niepos import losowa_nieposortowana
from tablice.los_pos_odwrotnie import losowa_odwrotnie_posortowana

def merge_sort(A):
    if len(A) > 1:
        mid = len(A) // 2

        left = A[:mid]
        right = A[mid:]

        merge_sort(left)
        merge_sort(right)

        i =  0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1

# tab = [7, 13, 24, 1, 5, 18, 9]

# merge_sort(tab)
# print(tab)

los_niepos = licz_czas(merge_sort, losowa_nieposortowana)

print("Czas wykonania (losowa nieposortowana): ", los_niepos)

los_pos = licz_czas(merge_sort, losowa_posortowana)

print("Czas wykonania (losowa posortowana): ", los_pos)

los_odwrotnie = licz_czas(merge_sort, losowa_odwrotnie_posortowana)

print("Czas wykonania (losowa odwrotnie posortowana): ", los_odwrotnie)