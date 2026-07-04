n = int(input("enter a number: "))

original = n
sum = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit 
    sum += digit

if(n == original):
    print("Armstrong number")
else:
    print("not a armstrong number")