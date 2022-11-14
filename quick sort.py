# Quick Sort
# is a sorting algorithm which is based on a divide-and-conquer principles
# The easiest this problem could be is if list contains less then 2 elements. This is the base case. return given list
# In case the given list contains more then 2 elements. We choose an element from the list - neo.
# Then we make 2 lists: greater and less then neo. return quick_sort(less) + [neo] +quick_sort(greater)
#
# The complexity of the algorithm would depend on the element you choose as neo
# In the worst case the  complexity of the algorithm would be o(n^2)
# In average it would take o(n*log(n))

numbers = [1, 3, 4, 7, 14, -3, 6, 8, -4, -13, -24]


def quick_sort(elements):
    if len(elements) < 2:
        return elements
    else:
        neo = elements[len(elements)//2]  # chosen elemenet
        less = [i for i in elements[1:] if i <= neo]
        greater = [i for i in elements[1:] if i > neo]
        return quick_sort(less) + [neo] + quick_sort(greater)


print(quick_sort(numbers))
