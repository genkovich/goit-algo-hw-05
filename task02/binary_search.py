def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    iterations = 0
    res = -1

    if target < arr[left] or target > arr[right]:
        return iterations, res

    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        print(f"left: {left},\t "
              f"right: {right},\t "
              f"mid: {mid},\t "
              f"target: {target},\t "
              f"arr_mid: {arr[mid]},\t"
              f"arr: {arr[left:right]}")

        sub_array = arr[left:right]
        if len(sub_array) <= 2:
            if target > sub_array[0]:
                res = mid
            else:
                res = left
            break

        if arr[mid] == target:
            res = mid
            break

        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid + 1

    return iterations, res


array = [2, 5, 8.4, 12.12, 16.83, 23.21, 38.66, 56, 72, 91]
target = 23.20
result = binary_search(array, target)

if result[1] != -1:
    print(f"Елемент {target} знайдено на індексі {result}")
else:
    print(f"Елемент {target} не знайдено в масиві")