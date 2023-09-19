

def find_median(arr):
    if arr == []:
        return None
    arr.sort()
    n = len(arr)
    if n % 2 == 0:
        median = (arr[n // 2] + arr[n // 2 - 1]) / 2
    else:
        median = arr[n // 2]
    return median


print(find_median(arr = [1, 5, 2, 3, 6]))

