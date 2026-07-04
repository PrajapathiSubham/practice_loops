
# check a number it is palindrome or not

a = (input("enter a string:"))

'''original = a
reverse = 0

while a > 0:
    digit = a % 10
    reverse = reverse * 10 + digit
    a = a // 10
    
if(original == reverse):
    print("It is palindrome")
else:
    print("It is not an palindrome")'''



# chk the stng value
reverse = ""

for ch in a:
    reverse = ch + reverse
if(a == reverse):
    print("palindrome")
else:
    print("not a palindrome")
