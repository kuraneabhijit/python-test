try:
    number=int(input("Enter number to check even odd\n"))

    if number%2==0:
        print("The given number is even number")
    else:
        print("The given number is odd number")
except Exception as e:
        print("Exception caught",e)
finally:
        print("Finally printed")
     