import requests

username = input("github username :")

class GetRepos:
    def __init__(self, url = "https://api.github.com/users/" + username + "/repos"):
        self.url = url

    def getrep(self):
        S = requests.Session()
        R = S.get(self.url)
        DATA = R.json()
        return DATA

list_repo = GetRepos().getrep()
repo = []

for i in list_repo:
    repo.append(i["name"])
print(repo)

class GetCommit:
    def __init__(self, url = "https://api.github.com/users/" + username + "/ex_03_jsonload/commits"):
        self.url = url

    def getcom(self):
    	S = requests.Session()
    	R = S.get(self.url)
    	DATA = R.json()
    	return DATA

list_commit = GetCommit().getcom()
com = []

for c in list_commit:
	com.append(c["commit"])
print(com)