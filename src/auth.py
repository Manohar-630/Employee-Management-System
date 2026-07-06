def login():
    
    USERNAME = "admin"
    PASSWORD = "admin123"

    print("\n========== Employee Management System Login ==========\n")

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == USERNAME and password == PASSWORD:
        print("\nLogin Successful!\n")
        return True

    print("\nInvalid Username or Password!\n")
    return False