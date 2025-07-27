print("Step Counter")

daily_goal = int(input("What is your daily steps target?\n"))
current_progress = int(input("How Many steps have you taken today?\n"))

remaining = daily_goal - current_progress

if remaining > 0:
    print(f"You still have {remaining} steps left\n")
elif remaining < 0:
    print(f"You have completed {-remaining} more steps today\n")
else:
    print("Congratulations! You have completed your daily goals")