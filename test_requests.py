import requests

# Register User
url = 'http://127.0.0.1:5000/register'
data = {
    "username": "testuser",
    "password": "securepassword"
}
response = requests.post(url, json=data)
print("Registration Response:", response.json())

# Grant Superuser
url = 'http://127.0.0.1:5000/grant_super_user'
data = {
    "username": "testuser"
}
response = requests.post(url, json=data)
print("Grant Superuser Response:", response.json())
