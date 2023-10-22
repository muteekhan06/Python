# This program displays the Fibonacci sequence up to a specified number of terms.
limit=input("How many Fibonacci number you want to print? ")
l = int(limit)
first = 0
second = 1
for i in range(l):
    print(first,end=" ") #Here end is used to make the output in one line
    next = first + second
    first = second
    second = next

