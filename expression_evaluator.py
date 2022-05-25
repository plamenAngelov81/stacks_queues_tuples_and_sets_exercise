from collections import deque

some_symbols = input().split()

operators = {
             "+": lambda a, b: a + b,
             "-": lambda a, b: a - b,
             "*": lambda a, b: a * b,
             "/": lambda a, b: a // b,
}
numbers = deque()

for i in some_symbols:

    if i in "+-*/":
        while len(numbers) > 1:
            num_1 = numbers.popleft()
            num_2 = numbers.popleft()
            result = operators[i](num_1, num_2)
            numbers.appendleft(result)
    else:
        numbers.append(int(i))

print(numbers.pop())
