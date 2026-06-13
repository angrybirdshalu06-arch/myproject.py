user_input= int (input("Enter a number:"))
reversed_number = 0
while user_input > 0:
    reversed_number = reversed_number * 10 + user_input % 10
    user_input//=10
print("reversed_number:", reversed_number)