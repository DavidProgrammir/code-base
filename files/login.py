def login(login_string: str):
    f = open('db.txt', 'r')
    users = f.readlines()
    for user in users:
        user_params = user.split()
        if login_string == user_params[1]:
            return user_params
    return False
