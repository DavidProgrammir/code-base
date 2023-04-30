import pathlib

path = pathlib.Path('../', 'user.json')

f = open(str(path))

print(f.readline())