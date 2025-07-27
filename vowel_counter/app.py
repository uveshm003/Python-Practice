print("Vowel Counter")

while True:
    text = input("\nEnter Some Text (or quit): ")
    if text.lower() == "quit":
        break

    vowel_count = 0
    for letter in text.lower():
        if letter in ["a","e","i","o","u"]:
            vowel_count += 1

    print(f"This text had {vowel_count} vowels.")