numbers = [4, 7, 2, 4, 9, 7, 3]
found = False

for x in range(len(numbers)):
    for y in range(len(numbers)):
        if numbers[x] == numbers[y] and x != y:
            found = True
            break

if found:
    print("duplicate found")
else: print("duplicate not found")