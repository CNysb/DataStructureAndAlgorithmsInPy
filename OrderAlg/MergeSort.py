def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # 分解：将数组分成两半
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # 合并：合并两个有序数组
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 处理剩余元素
    result.extend(left[i:])
    result.extend(right[j:])
    return result


a = [10, 1, 4, 6, 2, 9, 3]
res = merge_sort(a)
print(res)
