password = "python123"

attempt = 1

while attempt <= 3:

    user = input("Enter password: ")

    if user == password:
        print("Access granted")
        break

    else:
        print("Wrong password")
        attempt += 1

if attempt > 3:
    print("Access denied")
