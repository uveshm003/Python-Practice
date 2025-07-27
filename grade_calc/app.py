print("Grade Calculator")

scores = []

while True:
    new_score = float(input("Enter Your Score & when you are done enter -1."))
    if new_score == -1:
        break
    elif new_score > 100 | new_score < 0 & new_score != -1:
        print("Enter Valid Score.")
    else:
        scores.append(new_score)        

average = sum(scores) /len(scores)
print(f"Average Score => {average:.1f}")

if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")    
elif average >= 40:
    print("Grade: D")
else:
    print("Grade: F")    