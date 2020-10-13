n=28
guess=5
for i in range(1,6):
    print("You have only ",guess,"guesses left")
    num=int(input("Guess a no."))
    if num>n:
        print("It is greater , Reduce the no.")
    elif num<n:
        print("It is smaller , Increase the no.")
    elif num==n:
        print("You have the right no. at the ",i,"th guess")
        break
    guess=guess-1
if num!=28:
    print("Sorry! No chances left")
    
 


