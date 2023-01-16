import matplotlib.pyplot as plt


def assignment(new_list, i, old_list, j):
    new_list[i] = old_list[j]
    
    
def assign_remainder(new_list, i, old_list, j):
    while j < len(old_list):
        assignment(new_list, i, old_list, j)
        i += 1
        j += 1


def merge_sort(to_sort_list):
    # A list with less than 2 elements does not need sorting
    if len(to_sort_list) < 2:
        return
    
    # Split the array into two parts of (nearly) equal size and sort them
    mid = len(to_sort_list) // 2
    left = to_sort_list[:mid]
    right = to_sort_list[mid:]

    merge_sort(left)
    merge_sort(right)

    l = 0
    r = 0
    i = 0

    # Merge the sorted parts by comparing one item of each part and adding the smaller one to the final list
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            assignment(new_list=to_sort_list, i=i, old_list=left, j=l)
            l += 1
        else:
            assignment(new_list=to_sort_list, i=i, old_list=right, j=r)
            r += 1
        i += 1

    # If the previous while loop is finished, one part has no further elements so the remainder of the other can be added
    assign_remainder(new_list=to_sort_list, i=i, old_list=left, j=l)
    assign_remainder(new_list=to_sort_list, i=i, old_list=right, j=r)
    
    
import math
import matplotlib.pyplot as plt

def plot_list(numbers_list, title):
    x = range(len(numbers_list))
    plt.bar(x, numbers_list)
    
    tick_distance_raw = round(max(numbers_list) / 5)
    tick_distance_magnitude = math.floor(math.log10(tick_distance_raw))
    tick_distance_shift = math.pow(10, tick_distance_magnitude)
    tick_distance = math.ceil(tick_distance_raw / tick_distance_shift) * tick_distance_shift
    max_tick = math.ceil(max(numbers_list) / tick_distance) * tick_distance
    plt.ylim(0, max_tick)
    plt.yticks(ticks=[i * tick_distance for i in range(round(max_tick / tick_distance) + 1)])
    
    plt.title(title)
    plt.xlabel("Listenindex")
    plt.ylabel("Wert")
    plt.show()

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
plot_list(my_list, "Ungeordnete Beispielliste")
mergeSort(my_list)
plot_list(my_list, "Geordnete Beispielliste")
