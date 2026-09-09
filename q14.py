n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
sum1 = 0
for i in range(1, n1):
    if n1 % i == 0:
        sum1 += i
sum2 = 0
for i in range(1, n2):
    if n2 % i == 0:
        sum2 += i
if sum1 == n2 and sum2 == n1 and n1 != n2:
    print(f"{n1} and {n2} are amicable numbers.")
else:
    print(f"{n1} and {n2} are not amicable numbers.")
