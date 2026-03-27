n=int(input("Enter n: "))
a, b=0, 1
for I in range(1, n):
    a, b =b, a + b
 print("Nth Fibonacci term:", a)