n = int(input("Enter number of terms: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    a, b = 0, 1
    sum = 0
    print("Fibonacci Sequence:", end=" ")
    
    for _ in range(n):
        print(a, end=" ")
        sum += a
        a, b = b, a + b
        
    print(f"\nSum of first {n} terms: {sum}")
