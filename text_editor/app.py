print("Text Editor")

text_to_edit = str(input("Enter some text: "))

print("1. UPPERCASE")
print("2. lowercase")
print("3. Title Case")
print("4. Sentence case")


edit_preference = int(input("Enter Preferred Format:- "))

if edit_preference == 1:
    print(text_to_edit.upper())
elif edit_preference == 2:
    print(text_to_edit.lower())
elif edit_preference == 3:
    print(text_to_edit.title())
else: 
    print(text_to_edit.capitalize())