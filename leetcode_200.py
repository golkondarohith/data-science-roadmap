arr = [["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]]

# count = 0
# for row in arr:
#     for val in row:
#         if val == "1":
#             count += 1
# print(count)


count = sum(val == "1" for row in arr for val in row)
print(count)