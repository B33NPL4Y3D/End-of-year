'''Below is an example'''
user_name = "Dilynisking" #create a username here
password = "BBB123" #create a password here

def login():
    if input("Username: ") == user_name and input("Password: ") == password:
        print("------Access Granted------")
    elif input("Username: ") == password and input("Password: ") == user_name:
        print("------Not Quite Buddy------")
    else:
        print("------Access Denied------")

login()

'''
Practice:

1. Create an if-else statement that prints "Greater Than" if num1 > num2 and "Less Than"
if num1 < num2

2. Use elif to add a third case that prints "Equal" if num1 is equal to num2

3. BONUS CHALLENGE ($5): Modify the above function to return the number of login attempts
(Hint: use the return statement)
'''

num1 = 6
num2 = 5
# Write if-else statement below
if num1 > num2:
    print("greater than")
elif num1 < num2:
        print("Less Than")
else:
        print("Equal")  

