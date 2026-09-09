num=int(input("enter an integer under 120 :"))
if num<0:
    print("Invalid. Negative number entered.")
elif num in (2,3,5,7,11,13):
    print("It is a prime number")
elif (num==1 or num%2==0 or num%3==0 or num%5==0 or num%7==0 or num%11==0 or num%13==0):
    print("It is not a prime number")
else:
    print("It is a prime number")
