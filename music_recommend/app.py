import random

print("Music Recommender.")

genres ={
    "rock":["AC/DC","Queen","Led Zeppelin","Nirvana"],
    "pop":["Taylor Swift","Ed Sheeran","Bruno Mars","Ariana Grande"],
    "hip-hop":["Kendrick Lamar","J. Cole", "Drake","The Weeknd"],
}

choice = input("Enter Genre Type:- (rock, pop, hip-hop):-\n")

if choice not in genres:
    print("Sorry, I don't know about this genre.")
else: 
    print(f"Check Out {random.choice(genres[choice])}")