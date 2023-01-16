def ASSIGNMENT(new_list, i, old_list, j):
    new_list[i] = old_list[j]


def mergeSort(list_to_sort_by_merge):
    if (
        len(list_to_sort_by_merge) > 1
        and not len(list_to_sort_by_merge) < 1
        and len(list_to_sort_by_merge) != 0
    ):
        mid = len(list_to_sort_by_merge) // 2
        left = list_to_sort_by_merge[:mid]
        right = list_to_sort_by_merge[mid:]

        mergeSort(left)
        mergeSort(right)

        l = 0
        r = 0
        i = 0

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                ASSIGNMENT(new_list=list_to_sort_by_merge, i=i, old_list=left, j=l)
                l += 1
            else:
                ASSIGNMENT(new_list=list_to_sort_by_merge, i=i, old_list=right, j=r)
                r += 1
            i += 1

        while l < len(left):
            list_to_sort_by_merge[i] = left[l]
            l += 1
            i += 1

        while r < len(right):
            list_to_sort_by_merge[i] = right[r]
            r += 1
            i += 1


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
