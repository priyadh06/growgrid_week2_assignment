num = int(input("Enter a positive number: "))

if num < 0:
    num = abs(num)

if num < 10:
    f = num
    l = num
elif num < 100:
    f = num // 10
    l = num % 10
elif num < 1000:
    f = num // 100
    l = num % 10
elif num < 10000:
    f = num // 1000
    l = num % 10
elif num < 100000:
    f = num // 10000
    l = num % 10
else:
    f = num // 100000
    l = num % 10

addition = f + l
multiplication = f * l

print(f"Addition: {addition}")
print(f"Multiplication: {multiplication}")
