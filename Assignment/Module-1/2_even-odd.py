
n = int(input("Enter a number: "))
if (n > 0 and n%2 == 0):
    print("The number is Positive and Even")
elif (n > 0 and n%2 != 0):
    print("The number is Positive and Odd")
elif (n < 0 and n%2 == 0):
    print("The Number is Negative and Even")
elif (n < 0 and n%2 != 0):
    print("The Number is Negative and Odd")
else:
    print("The Number is Zero")
