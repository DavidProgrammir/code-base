from io import TextIOWrapper
import json
import pathlib
user_ = None


class Database:
    path: pathlib.Path
    f: TextIOWrapper

    def __init__(self):
        self.path = pathlib.Path('json_files', 'db.txt')

    def read_all(self):
        f = open(str(path))

        raw_data = f.readline()
        f.close()

        data = json.loads(raw_data)
        return data
    
    def update_user(self, user: dict):
        f = open(str(path))
        raw_data = f.readline()
        f.close()

        data = json.loads(raw_data)

        id_user = user["id"]
        for users in data:
            id_users = user["id"]
            if id_users == id_user:
                user_ = users
                break
        data[user_] = user
        raw_data = json.dumps(data)
        f = open(str(path), 'w')
        f.write(raw_data)
        f.close()


        # find in data user where id == user['id']
        # replace this user to income user
        # rewrite to file
    
    def add_user(user: dict):
        f = open(str(path))

        raw_data = f.readline()
        f.close()

        data = json.loads(raw_data)
        data.append(user)
        json_data = json.dumps(data)

        f = open(str(path), 'w')
        f.write(json_data)
        f.close()





path = pathlib.Path('json_files', 'db.txt')

# unique id +
# add data +
# edit data +
# read data +
# delete data +

db = Database()

data = db.read_all()


user = {
    "id": 3,
    "name": 'Natasha'
}

#db.update_user(user)
user1 = {'id': 1, 'name': 'Id_dev', 'password': '12345', 'roles': ['Admin', 'Manager'], 'address': {'street': 'Smith', 'home': 101}}

path.update_user(user1)


print(data)

