num = int(input("Enter a 3-digit positive number: "))

if 100 <= num <= 999:
    m = (num // 10) % 10
    print(f"Middle Digit: {m}")

    if m % 2 == 0:
        print(f"{m} is divisible by 2.")
    else:
        print(f"{m} is not divisible by 2.")

    if m % 3 == 0:
        print(f"{m} is divisible by 3.")
    else:
        print(f"{m} is not divisible by 3.")

    if m % 5 == 0:
        print(f"{m} is divisible by 5.")
    else:
        print(f"{m} is not divisible by 5.")
else:
    print("Error: The entered number is not a 3-digit number.")
