from licz_czas import licz_czas
from tablice.los_pos import losowa_posortowana
from tablice.los_niepos import losowa_nieposortowana
from tablice.los_pos_odwrotnie import losowa_odwrotnie_posortowana

def count_sort(arr):
    max_element = int(max(arr))
    min_element = int(min(arr))
    range_of_elements = max_element - min_element + 1
    #range_of_elements = 1001
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(arr))]
 
    for i in range(0, len(arr)):
        count_arr[arr[i]-min_element] += 1
 
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]
 
    for i in range(len(arr)-1, -1, -1):
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
        count_arr[arr[i] - min_element] -= 1
 
    for i in range(0, len(arr)):
        arr[i] = output_arr[i]
 
    return arr
 
 

# arr = [5, 10, 0, 3, 8, 5, 1, 10]
# print(count_sort(arr))

los_niepos = licz_czas(count_sort, losowa_nieposortowana)

print("Czas wykonania (losowa nieposortowana): ", los_niepos)

los_pos = licz_czas(count_sort, losowa_posortowana)

print("Czas wykonania (losowa posortowana): ", los_pos)

los_odwrotnie = licz_czas(count_sort, losowa_odwrotnie_posortowana)

print("Czas wykonania (losowa odwrotnie posortowana): ", los_odwrotnie)