n=int(input("Enter a number:"))
temp = n 
s = 0
digits = len(str(n))
while n>0:
    d = n%10
    s+=d ** digits
    n//=10
if s==temp:
    print("Armstrong number")
else: 
    print("Not an Armstrong number")