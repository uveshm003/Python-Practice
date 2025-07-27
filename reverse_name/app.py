print("Reverse Name Project")

while True:
    name = input("Enter a name:-")

    if not name:
        break
    reversed_name = name[::-1]
    print(f"Your reversed name is {reversed_name.title()}")

    choice = input("\nWant to try another name? y/n: ")
    if choice != "y":
        break

