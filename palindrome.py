
# check a number it is palindrome or not

a = int(input("enter a number"))

original = a
reverse = 0

while a > 0:
    digit = a % 10
    reverse = reverse * 10 + a
    a = a // 10
    
    if(original == reverse):
        print("It is palindrome")
    else:
        print("It is not an palindrome")

print("")        