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


def plot_list(to_plot_list):
    x = range(len(to_plot_list))
    plt.plot(x, to_plot_list)
    plt.show()

    
my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
plot_list(my_list)

merge_sort(my_list)
plot_list(my_list)