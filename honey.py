from collections import deque

bees = deque([int(x) for x in input().split()])
fruits = [int(y) for y in input().split()]
symbols = deque(input().split())

operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b
}

honey = 0

while bees and fruits:
    bee = bees.popleft()
    nectar = fruits.pop()
    if nectar < bee:
        bees.appendleft(bee)
        continue

    if nectar == 0:
        continue

    operator_1 = symbols.popleft()
    honey += abs(operations[operator_1](bee, nectar))

print(f"Total honey made: {honey}")

if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")

if fruits:
    print(f"Nectar left: {', '.join(map(str, fruits))}")
