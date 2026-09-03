import httpx

response = httpx.get('https://jsonplaceholder.typicode.com/todos/1')
print(response.json())
print(response.status_code)

data = {
    "title": "Новая задача",
    "completed": False,
    "userId": 1
}

response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)
print(response.json())
print(response.status_code)

data = {
    "username": "test_user",
    "password": "qwerty123"
}
response = httpx.post('https://httpbin.org/post', data=data)
print(response.json())
print(response.status_code)

headers = {
    "Authorization": "Bearer MY_SECRET_TOKEN"
}
response = httpx.get('https://httpbin.org/get', headers=headers)
print(response.json())
print(response.status_code)

params = {
    "userId": 1
}
response = httpx.get('https://jsonplaceholder.typicode.com/todos', params=params)
print(response.json())
print(response.url)

files = {
    "file": ("example.txt", open("example.txt", "rb"))
}
response = httpx.post('https://httpbin.org/post', files=files)
print(response.json())
print(response.status_code)

with httpx.Client() as client:
    response1 = client.get('https://jsonplaceholder.typicode.com/todos/1')
    response2 = client.get('https://jsonplaceholder.typicode.com/todos/2')

print(response1.json())
print(response2.json())

client= httpx.Client(headers={"Authorization": "Bearer MY_SECRET_TOKEN"})
response = client.get('https://httpbin.org/get')
print(response.json())
print(response.status_code)

try:
    response = client.get('https://jsonplaceholder.typicode.com/todos/invalid')
    response.raise_for_status()
except httpx.HTTPError as e:
    print(f'Ошибка запроса: {e}')


try:
    response = client.get("https://httpbin.org/delay/5", timeout=2)
except httpx.ReadTimeout:
    print("Запрос превысил лимит времени")