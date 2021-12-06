for i in range(3):
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == 'jyff' and password == 'vinsmoke':
        print("Logged in Successfully")
        break
    else:
        print("Invalid credentials!!")
    print("Try again!")
else:
    print("Attempts finished!!")

