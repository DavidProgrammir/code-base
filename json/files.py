'''Dumps позволяет создать JSON-строку из переданного в нее объекта. Loads — преобразовать строку назад в объекты языка.
Dump и load используют, чтобы сохранить результат в файл или воссоздать объект.
 Работают они схожим образом, но требуют передачи специального объекта для работы с файлом — filehandler.'''
import json

with open("/home/nubuk/Папка/programist/data.json", "r") as fh:
    e = json.load(fh)
print(e)
e["d"] = 3
print(e)


with open("/home/nubuk/Папка/programist/data.json", "w") as fh:
    json.dump(e, fh)


