from wsgiref import headers

import httpx
#from gevent.testing import params
#
# response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
#
# print(response.json())
# print(response.status_code)
#
# data = {
#     "title": "Новая задача",
#     "comleted": False,
#     "userId": 1
# }
# response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)
#
# print(response.json())
# print(response.request.headers)
# print(response.status_code)
#
# data = {
#     "username": "test_user",
#     "password": "12345"
# }
#
# with httpx.Client(trust_env=False) as client:
#     response = client.post(
#         "https://httpbun.com/post",
#         data=data
#     )
#
# print(response.json())
# print(response.status_code)
#
# headers = {"Authorization": f"Bearer access_token"}
# response = httpx.get("https://httpbun.com/get", headers=headers)
#
# print(response.json())
# print(response.request.headers)
#
# params = {"userId": 1}
# response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
# print(response.json())
# print(response.url)
#
#
# files = {"file": ("exemple.txt", open("exemple.txt", "rb"))}
# response = httpx.post("https://httpbun.com/post", files=files)
#
# print(response.json())
#
# with httpx.Client() as client:
#     response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
#     response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")
#
#
# print(response1.json())
# print(response2.json())
#
# client = httpx.Client(headers={"Authorization": "Bearer access_token"})
# response = client.get("https://httpbun.com/get")
# print(response.json())

try:
    response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")

try:
    response = httpx.get("https://httpbun.com/delay/5")
except httpx.ReadTimeout:
    print("Запрос привысил лимит времени")