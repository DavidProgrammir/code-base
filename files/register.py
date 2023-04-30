def register():
    print('enter your login:')
    login = input()
    print('enter your password:')
    password = input()
    f = open('db.txt', '+r')
    allUsers = f.readlines()
    last = allUsers[len(allUsers)-1]
    last_params = last.split()
    last_id = int(last_params[0])
    current_id = last_id + 1
    row = f'\n{current_id} {login} {password}'
    f.write(row)
    f.close()