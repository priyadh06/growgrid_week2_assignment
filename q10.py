a = int(input("Enter first positive integer: "))
b = int(input("Enter second positive integer: "))
x, y = abs(a), abs(b)
while y > 0:
    x, y = y, x % y

gcd = x
if a == 0 or b == 0:
    lcm = 0
else:
    lcm = abs(a * b) // gcd

print(f"GCD: {gcd}")
print(f"LCM: {lcm}")
