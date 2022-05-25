from collections import deque

# take last chocolate element
chocolate = list(map(int, input().split(", ")))
# tak first cup of milk
milk = deque(map(int, input().split(", ")))

milkshakes = 0

while chocolate and milk:
    if milkshakes == 5:
        break

    current_chocolate = chocolate[-1]
    cup_milk = milk[0]
    if current_chocolate > 0 and cup_milk > 0:
        if current_chocolate == cup_milk:
            milkshakes += 1
            chocolate.pop()
            milk.popleft()
        if current_chocolate != cup_milk:
            chocolate[-1] -= 5
            milk.popleft()
            milk.append(cup_milk)
    else:
        if current_chocolate <= 0 and cup_milk <= 0:
            chocolate.pop()
            milk.popleft()
        elif current_chocolate <= 0:
            chocolate.pop()
        elif cup_milk <= 0:
            milk.popleft()

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate:
    print(f"Chocolate: {', '.join(map(str, chocolate))}")
else:
    print("Chocolate: empty")

if milk:
    print(f"Milk: {', '.join(map(str, milk))}")
else:
    print("Milk: empty")
