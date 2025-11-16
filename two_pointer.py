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