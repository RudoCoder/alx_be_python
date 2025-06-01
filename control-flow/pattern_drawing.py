square_side = int(input("Enter the size of the pattern: "))
size = 0
while size < square_side:
    for pattern in range(square_side):
        print("*", end=" ")

    print()
    size += 1
