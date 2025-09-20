from collections import deque
from collections import Counter

dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
dq.pop()
dq.popleft()
print(dq)


words = ["apple", "banana", "apple", "orange", "banana", "apple"]
count = Counter(words)
print(count)
print(count.most_common(1))
