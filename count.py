num = int(input("enter a number:"))

count = 0

while num > 1:
    num = num // 10
    count += 1
print("count digit",count)