number = 7
guess = 0
count = 0
print("Let's play Guessing game!")
while guess != number:
    guess = int(input("Enter the number:"))
    count += 1
    if guess == number:
        print("You are right!")
    elif guess < number:
        print("It's bigger!")
    elif guess > number:
        print("It's not so big!")
    if count > 3:
        print("Your session expired! Try again later")
    else:
        print("Good Job!")


