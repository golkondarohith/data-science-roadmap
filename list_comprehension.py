nums = [1, 2, 3, 4, 5]

squares = [i*i for i in nums]
print(squares)

even = [i for i in nums if i%2 == 0]
print(even)

only_even = [i if i%2 == 0 else 0 for i in nums]
print(only_even)


