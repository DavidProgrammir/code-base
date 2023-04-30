from register import register
from login import login

print('Hello, enter your login')
login_string = input()

if login_string == '0':
    register()
else:
    result = login(login_string)
    if type(result) == list:
        print("Welcome")
    else:
        print('User not found')

