#Program that calculates greater of two numbers entered by the user
n1 = input("Enter first number: ")
n2 = input("Enter second number: ")
if (n1>n2):
    print (n1, "is greater than",n2,".")
elif (n2>n1):
    print (n2, "is greater than",n1,".")
else:
    print ("Both numbers are equal.")