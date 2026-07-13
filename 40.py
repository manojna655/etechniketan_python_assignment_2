print("Welcome to Grade Checker")

while True:

    marks = float(input("Enter marks: "))

    if marks >= 90:
        print("Grade: A+")
    elif marks >= 80:
        print("Grade: A")
    elif marks >= 70:
        print("Grade: B")
    elif marks >= 60:
        print("Grade: C")
    elif marks >= 50:
        print("Grade: D")
    else:
        print("Fail")

    choice = input("Do you want to continue? (yes/no): ")

    if choice.lower() == "no":
        print("Thank you")
        break
