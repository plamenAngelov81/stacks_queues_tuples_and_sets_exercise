first = set(map(int, input().split()))
second = set(map(int, input().split()))

n = int(input())

for i in range(n):
    data = input().split()
    if data[0] == "Add":
        if data[1] == "First":
            first = first.union([int(x) for x in data[2:]])
        elif data[1] == "Second":
            second = second.union([int(y) for y in data[2:]])
    elif data[0] == "Remove":
        if data[1] == "First":
            first = first.difference([int(z) for z in data[2:]])
        elif data[1] == "Second":
            second = second.difference([int(z) for z in data[2:]])
    elif data[0] == "Check":
        print(first.issubset(second) or second.issubset(first))

print(f"{', '.join(map(str, sorted(first)))}")
print(f"{', '.join(map(str, sorted(second)))}")
