import random
n=random.randint(1,100)
def intro():
    print("Welcome to the guessing game")
    print("May i know your name:")
    global name 
    name=input()
    print("Hello",name,"! I am thinking about a number between 1 to 100.")
    if(n%2==0):
        print("It is an even number")
    else:
        print("It is an odd number")
    print("Go ahead and guess the number!") 

    
def guessnum():
        if guess<=100 and guess>=1:
            if guess< n:
                print("Your guess is too low")
                print("Try again!")
            if guess>n:
                print("Your guess is too high")
                print("Try again")
intro()
guess=int(input("Enter your guess:"))
guessnum()
if guess==n:
    print("Congratulations!",name,"! You guessed the number correctly!")
else:
    print("Sorry",name," The number was",n,".")



