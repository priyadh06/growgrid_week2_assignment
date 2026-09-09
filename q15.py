start_num = int(input("Enter starting number: "))
n = start_num + 1

while True:
    if n % 7 == 0 and n % 2 != 0 and n % 3 != 0:
        
        temp = n
        rev_num = 0
        while temp > 0:
            rev_num = (rev_num * 10) + (temp % 10)
            temp //= 10
            
        if n == rev_num:
            print(f"The smallest matching number greater than {start_num} is: {n}")
            break
            
    n += 1
