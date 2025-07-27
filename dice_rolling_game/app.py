import random



dice_count = int(input("How many dice you want to roll?: "))
while dice_count < 1:
    dice_count = int(input("Enter a valid count: "))
counter = 0

while True:
    dice_list = []
    output = "("
    choice = input("\nRoll the dice? (y/n): ").lower()
    if choice == 'y':
        for dice in range(0,dice_count):
            dice_roll = random.randint(1,6)
            dice_list.append(dice_roll)
            output = f"{output}{str(dice_roll)},"
        output = f"{output}) "
        counter += 1
        print(output)
    elif choice == 'n':
        print(f"Thanks for playing! You rolled the dice {counter} times.")
        break
    else:
        print("Invalid Choice!")
        

        
    