# Из json-строки преобразовать в словарь
import json

json_data = """{
  "name": "Иван",
  "age": 30,
  "is_student": false,
  "courses": [
    "Python",
    "QA Automation",
    "API Testing"
  ],
  "address": {
    "city": "Москва",
    "zip": "10100"
  },
  "count": null
}"""  # строка
parsed_data = json.loads(json_data)  # из строки получить json

print(parsed_data["address"])

#наоборот есть словарь получить json-строку
data={ #словарь, могут быть одинарные кавычки
  "name": "Мария",
  "age": 25,
  "is_student": True
}

json_string=json.dumps(data,indent=4) #преобразование в json
print(json_string)

#чтение из json-файла и распарсить данные в виде python-словаря
with open("json_example.json","r", encoding="utf-8") as file:
    read_data=json.load(file)
    print(read_data, type(read_data))

#записать json в файл
with open("json_user.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)
