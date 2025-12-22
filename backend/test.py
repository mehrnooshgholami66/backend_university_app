import requests

username = "admin2"
password = "456"

resp = requests.post(
    "http://127.0.0.1:8000/api/auth/login/",
    json={
        "username": username,
        "password": password
    }
)

if resp.status_code == 200:
    data = resp.json()
    token = data["token"]
    # role نداریم، پس چاپش نکنیم یا مقدار پیش‌فرض بدیم
    role = data.get("role", "unknown")
    user_id = data["user_id"]

    print(f"Logged in as {username} with role {role} and is {user_id}. Token: {token}")
    print (data)
else:
    print("Login failed:", resp.status_code, resp.text)

