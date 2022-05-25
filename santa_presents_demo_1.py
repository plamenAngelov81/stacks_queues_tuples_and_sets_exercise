from collections import deque


def negative_result(current_material, current_magic):
    new_material = current_material + current_magic
    toy_materials.pop()
    magic_level.popleft()
    toy_materials.append(new_material)


def positive_result(current_result):
    if current_result in presents_list:
        if current_result == 150:
            item_dict["Doll"] += 1
            toy_materials.pop()
            magic_level.popleft()
        elif current_result == 250:
            item_dict["Wooden train"] += 1
            toy_materials.pop()
            magic_level.popleft()
        elif current_result == 300:
            item_dict["Teddy bear"] += 1
            toy_materials.pop()
            magic_level.popleft()
        elif current_result == 400:
            item_dict["Bicycle"] += 1
            toy_materials.pop()
            magic_level.popleft()
    else:
        magic_level.popleft()
        toy_materials[-1] += 15


# take the last box with materials
toy_materials = [int(x) for x in input().split()]

# take first magic_level element
magic_level = deque([int(y) for y in input().split()])

item_dict = {"Doll": 0,
             "Wooden train": 0,
             "Teddy bear": 0,
             "Bicycle": 0
             }

presents_list = [150, 250, 300, 400]

while toy_materials and magic_level:
    material = toy_materials[-1]
    magic = magic_level[0]
    result = material * magic
    if result < 0:
        negative_result(material, magic)
    elif result > 0:
        positive_result(result)
    elif magic == 0 and material == 0:
        toy_materials.pop()
        magic_level.popleft()
    elif magic == 0:
        magic_level.popleft()
    elif material == 0:
        toy_materials.pop()

if item_dict["Doll"] >= 1 and item_dict["Wooden train"] >= 1 or item_dict["Teddy bear"] >= 1 \
        and item_dict["Bicycle"] >= 1:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

toy_materials.reverse()
if toy_materials:
    print(f"Materials left: {', '.join(map(str, toy_materials))}")

if magic_level:
    print(f"Magic left: {', '.join(map(str, magic_level))}")

sorted_presents = sorted(item_dict.items())
for item, numer in sorted_presents:
    if numer > 0:
        print(f"{item}: {numer}")
