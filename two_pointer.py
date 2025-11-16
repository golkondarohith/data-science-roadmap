# arr = [1, 2, 4, 7, 11, 15]

def targetSum(arr):
    left = 0
    right = len(arr) - 1

    target = 15
    while left < right:
        if arr[left] + arr[right] == target:
            return left, right
        elif arr[left] + arr[right] > target:
            right -= 1
        else:
            left += 1

print(targetSum([1, 2, 4, 7, 11, 15]))


def maxSubArr(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(window_sum, max_sum)
    return max_sum

print(maxSubArr([2, 1, 5, 1, 3, 2], 3))
    