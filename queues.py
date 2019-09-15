from collections import deque

numbers = deque()

numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5)
numbers.append(6)
numbers.append(7)
numbers.append(8)
numbers.append(9)
numbers.append(10)

def insertAndRotate(a,array = deque):
    array.appendleft(a)
    array.rotate()
    array.popleft()
    print(array)
insertAndRotate(69,numbers)
print(numbers)