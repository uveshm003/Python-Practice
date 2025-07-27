import random
print("Coin Flip Game")


while True:
   user_choice = input("\nEnter Your Guess (heads/tails)") 
   tossed_coin = random.choice(["heads","tails"])
   if tossed_coin == user_choice:
       print("You Guessed Correctly: You Win")
   else:
       print("Sorry Wrong Guess Try Again!")
       
   choice = input("Want to play again (y/n)")
   if choice == "n":
      break 