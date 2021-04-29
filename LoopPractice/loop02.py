# using looping system to get user generated multiplications table

print("please, enter the number:")
number = int(input())
count = 1
while count <= 10:
    print(number, "x", count, "=", number*count)
    count += 1
