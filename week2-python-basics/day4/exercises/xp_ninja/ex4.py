def insertion_sort(alist):
    """
    code implements the insertion sort algorithm to sort a list of numbers in ascending order.
    It iterates through the list, moving elements to their correct positions within the sorted portion of the list.
    """
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = currentvalue


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(alist)
print(alist)
