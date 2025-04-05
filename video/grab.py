import requests

stduent_id = input("Please input your stduent id")
password = input("Please input your password")

url = "https://classroom.zju.edu.cn"

response = requests.get(url)

print(response.history)