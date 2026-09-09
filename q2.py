usn="abc"
psw="def"
username=input("Enter username :")
password=input("Enter password :")
while username!=usn or password!=psw:
    print("Incorrect username or password. try again")
    username=input("Enter username :")
    password=input("Enter password :")
if username==usn or password==psw:
    print("Login successful")
