num = int(input("Enter a number: "))
temp = abs(num)
print(f"Process: {temp}")
while temp >= 10:
    current_sum = 0
    while temp > 0:
        current_sum += temp % 10
        temp //= 10
    temp = current_sum
    print(f" ->{temp}", end="")

print(f"\nSingle digit result: {temp}")
