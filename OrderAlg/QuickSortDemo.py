def QuickSort(a):
    if len(a) <= 1:
        return a
    pivot = a[len(a) // 2]
    left = [x for x in a if x < pivot]
    middle = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]
    print(f"left is {left}")
    print(f"right is {right}")
    print(f"middle is {middle}")
    return QuickSort(left) + middle + QuickSort(right)


a = [10, 234, 6234, 23, 1234, 2134]
a = QuickSort(a)
print(a)
