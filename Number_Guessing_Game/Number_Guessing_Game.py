import random


print("---------------------------------------------")
print("Hello! Welcome to the Number Guessing Game")
print("---------------------------------------------")
secret_number =random.randint(1,50)

print("I'm thinking of a number between 1 and 50,so let's hope you can guess!")
print()
guess =0

count = 0
end_the_count = False
while guess!= secret_number and not(end_the_count):
    guess = int(input("you have 3 chances ,Enter your guess: "))
    if guess< secret_number:
        count += 1
        print(f"Hint: guess is too low try again!,you have {3-count} chances ")



    elif guess>secret_number:
        print(f"Hint: guess is too high ,try one more time!,you have {3-count} chances ")
        count += 1

    if count == 3:
        end_the_count = True
        break

if count == 3:
    print("chances are over , you loose!")
    print(f"Correct number is {secret_number}")

else:
    print("You won!,Congratulations!")



