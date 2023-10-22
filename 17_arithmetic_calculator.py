# This program performs basic arithmetic operations like addition, subtraction, multiplication, and division.
number1=input("Enter first number: ")
number2=input("Enter second number: ")
n1=int(number1)
n2=int(number2)
operation=input("Enter operation you want to perform: ")
if(operation=="+"):
    print ("The sum is",n1+n2,".")
if(operation=="-"):
    print ("The difference is",n1-n2,".")
if(operation=="*"):
    print ("The product is",n1*n2,".")
if(operation=="/"):
    print ("The quotient is",n1/n2,".")
if(operation=="%"):
    print ("The quotient is",n1%n2,".")
if(operation=="//"):
    print ("The floor division is",n1//n2,".")
if(operation=="**"):
    print ("The exponent is",n1**n2,".")
