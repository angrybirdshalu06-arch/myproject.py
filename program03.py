n = int(input("Enter a number:"))
if n<=1:
print("Neither Prime nor Composite")
else:
    for i in range(2, n):
        if n%i==0:
           print("composite number")
           break
    else:
        print("Prime number")