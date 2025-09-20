from collections import deque
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
dq.pop()
dq.popleft()
print(dq)
