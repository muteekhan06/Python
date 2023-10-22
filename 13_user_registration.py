# User Registration: When creating a user registration system, input() can be used to prompt users to enter their information, such as name, email, and password.
name = input ("Enter your name: ")
email = input("Enter your email address: ")
password = input("Create a password for your account: ")
confirm_password = input("Confirm your password: ")                       
if password == confirm_password:
    print("Account created successfully! Welcome", name)
    print ("Please check your mail",email ,"for verification code.")
else:
    print("Passwords do not match.")
