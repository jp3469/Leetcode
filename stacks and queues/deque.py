import collections 

queue = collections.deque([6,1,2,3,4])
print(queue)

queue.pop()
queue.popleft()

print(queue)

queue.append(3)
print(queue)

queue.appendleft(4)
print(queue)