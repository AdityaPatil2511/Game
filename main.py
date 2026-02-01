import random

n = random.randint(1,100)
a = -1
guesses = 1

while(a!=n):
    a = int(input("Guess The Number :"))

    if(a>n):
        print("Little CLose to the Number \nTry Again...Guess Lower Number Please")
        guesses +=1
    elif(a<n):
        print("Little CLose to the Number \nTry Again...Guess Higher Number Please")
        guesses +=1
    
print(f"Congrats Right Guess...\nAttempts :{guesses} ")