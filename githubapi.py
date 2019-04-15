import requests

username = input("github username :")

class GetUser:
    def __init__(self, url = "https://api.github.com/users/" + username + "/repos"):
        self.url = url

    def get(self):
        S = requests.Session()
        R = S.get(self.url)
        DATA = R.json()
        return DATA

list_repo = GetUser().get()
repo = []

for i in list_repo:
    repo.append(i["name"])
print(repo)