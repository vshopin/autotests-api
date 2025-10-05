import httpx

payload = {
    "email": "jdoe@example.com",
    "password": "test",
}

login_response = httpx.post(url="http://localhost:8000/api/v1/authentication/login", json=payload)
login_response_data = login_response.json()

print("Login Status Code:", login_response.status_code)
print("Login response:", login_response_data)

access_headers = {"Authorization": f"Bearer {login_response_data["token"]["accessToken"]}"}

me_response = httpx.get(url="http://localhost:8000/api/v1/users/me", headers=access_headers)
me_response_data = me_response.json()

print("Users Me Status Code:", me_response.status_code)
print("Users Me response:", me_response_data)
