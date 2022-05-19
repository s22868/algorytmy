from licz_czas import licz_czas
from tablice.los_pos import losowa_posortowana
from tablice.los_niepos import losowa_nieposortowana
from tablice.los_pos_odwrotnie import losowa_odwrotnie_posortowana

def max_heapify(arr,n,i):
    l = 2 * i + 1
    r = 2 * i + 2
     
    if l < n and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
         
    if r < n and arr[r] > arr[largest]:
        largest = r
         
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)
 
 
def build_max_heap(arr):
    n = len(arr)
    for i in range(n, -1,-1):
        max_heapify(arr, n, i)
    for i in range(n-1,0,-1):
        arr[0] ,arr[i] = arr[i], arr[0]
        max_heapify(arr, i, 0)


# build_max_heap(losowa_nieposortowana)
# print(losowa_nieposortowana)

los_niepos = licz_czas(build_max_heap, losowa_nieposortowana)

print("Czas wykonania (losowa nieposortowana): ", los_niepos)

los_pos = licz_czas(build_max_heap, losowa_posortowana)

print("Czas wykonania (losowa posortowana): ", los_pos)

los_odwrotnie = licz_czas(build_max_heap, losowa_odwrotnie_posortowana)

print("Czas wykonania (losowa odwrotnie posortowana): ", los_odwrotnie)