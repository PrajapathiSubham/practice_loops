num = int(input("Enter a digits:"))

reverse = 0
while num >= 0:
    digit = num % 10
    reverse = reverse * 10 + num
    num = num//10
print("reverse numbere",reverse)
