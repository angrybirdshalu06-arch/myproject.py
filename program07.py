user_input= int (input("Enter a number:"))
rev = 0
while user_input > 0:
    rev = rev * 10 + user_input % 10
    user_input//=10
print("Reverse:", rev)