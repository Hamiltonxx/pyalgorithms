def select_non_adjacent_max_sum(array):
    n = len(array) // 3

    dp1 = array[:n]
    for i in range(n, 2 * n):
        dp1.append(max(dp1[i-2] + array[i], dp1[i-1]))

    maxIndex1 = dp1.index(max(dp1))

    dp1[maxIndex1] = 0

    dp2 = array[:n]
    dp2[maxIndex1] = 0
    for i in range(n, 2 * n):
        dp2.append(max(dp2[i-2] + array[i], dp2[i-1]))

    maxIndex2 = dp2.index(max(dp2))

    dp2[maxIndex2] = 0

    selected = [array[maxIndex1], array[maxIndex2]]
    remaining = n - 2

    for i in range(2 * n):
        if i != maxIndex1 and i != maxIndex2:
            if remaining == 0:
                break
            if len(selected) == 2:
                selected.append(array[i])
                remaining -= 1
            elif selected[-2] != array[i-1]:
                selected.append(array[i])
                remaining -= 1

    return selected

array = [1,2,3,4,5,6]

print(select_non_adjacent_max_sum(array))