import httpx

data = {
    "username": "test_user",
    "password": "12345"
}

with httpx.Client(trust_env=False) as client:
    response = client.post(
        "https://httpbun.com/post",
        data=data
    )

print(response.json())
print(response.status_code)