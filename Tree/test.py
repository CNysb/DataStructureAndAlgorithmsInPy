from collections import deque

stack = deque()

for i in range(10):
    print(f"insert {i}")
    stack.append(i)


for i in range(10):
    print(stack.popleft())
