num=int(input("Enter a number: "))
temp=abs(num)
digits_count=0
counter=temp
if temp==0:
    digits_count=1
else:
    while counter>0:
        digits_count+=1
        counter//=10

total=0
counter=temp
while counter>0:
    digit=counter%10
    total+=digit ** digits_count
    counter//=10

if total==abs(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
