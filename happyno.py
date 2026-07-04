
# happy number:if repeatedly replacing it by the sum of the 
# squares of its digits eventually reaches

num = int(input("enter any number"))

seen = set()

while num != 1 and num not in seen:
  seen.add(num)
  total = 0

  while num > 0:
    digit = num % 10
    total += digit * digit
    num //= 10

    num = total

if(num == 1):
    print("HAPPY NUMBERS")
else:
     print("NOT happy")







