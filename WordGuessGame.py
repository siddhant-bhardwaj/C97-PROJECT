import random
print("Welcome to number guessing game! You must guess the number between 1-20 to win")
num=random.randint(1,20)
chance=5
while(chance>0):
    print("Number of lives ",chance)
    guess=int(input("Enter the number"))
    if(guess==num):
        print("Congratulations! You won!")
        break
    elif(guess<num):
        print("Your guess is less than the number")
    else:
        print("Your guess is more than the number")
        
    chance=chance-1

if(chance==0):
    print("You lose! The number was ",num)