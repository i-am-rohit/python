import random
winning_number = random.randint(1,100)
guess = 1
while True:
    n=int(input("guess your number between 0 to 100 :  ")) 
    if n == winning_number: 
        print(f"you win!!!, guessing time : {guess}")
        break
    else:
        if n < winning_number:
            print("too low ")
            
        else:
            print("too high")
            
        guess += 1
        continue 

