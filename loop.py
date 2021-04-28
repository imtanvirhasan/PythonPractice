x = int(input("How many candies you need?"))
av = 10
i = 1 
while i <= x:
    if i > av:
        print("Out of stock")
        break
    print("Candy")
    i += 1

print("Have a good day!")
