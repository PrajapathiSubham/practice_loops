n = int(input("enter any number:"))

for i in range(1,n+1):

    if(i%3==0 and i%5==0):
        print("Fizzbuz")

    elif(i%10==0):
        print("fizz")

    elif(i%5==0):
        print("buzz")
        
    else:
        print(i)