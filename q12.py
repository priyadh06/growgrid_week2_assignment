num = int(input("Enter a number: "))
temp = abs(num)
largest = -1
second_largest = -1
if temp < 10:
    print("The number does not have a second largest digit.")
else:
    while temp > 0:
        digit = temp % 10
        if digit > largest:
            second_largest = largest
            largest = digit
        elif digit > second_largest and digit != largest:
            second_largest = digit
        temp //= 10
    if second_largest == -1:
        print("All digits are equal")
    else:
        print(f"Second largest digit: {second_largest}")
        
