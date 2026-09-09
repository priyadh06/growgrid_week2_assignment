num_str = input("Enter a positive number: ")
if num_str.startswith('0'):
    print(f"{num_str} is NOT a Duck number (it starts with zero).")
elif '0' in num_str:
    print(f"{num_str} IS a Duck number.")
else:
    print(f"{num_str} is NOT a Duck number (contains no zero).")
