nums = [1, 2, 3, 4, 5]

squares = [i*i for i in nums]
print(squares)

even = [i for i in nums if i%2 == 0]
print(even)

only_even = [i if i%2 == 0 else 0 for i in nums]
print(only_even)


# Nested loop comprehensions
a = [1, 2]
b = [11, 22]

pairs = [(i, j) for i in a for j in b]
print(pairs)

#Enumerates
enum = [4, 5, 6, 7, 8]
print("before enumeration", enum)
enum = [(i, v) for i, v in enumerate(enum)]
print(enum)


# leetcode problem
nums = [8, 1, 2, 2, 3]

res_nums = [sum(1 for j in nums if j < i) for i in nums]
res_nums2 = [sum(2 for j in nums if j < i) for i in nums]
print(res_nums)
print(res_nums2)