import requests

with open("dataset_3378_2.txt") as file:
    url=file.readline()
print(url)

f=requests.get(url.strip())
tex=f.text
print(tex)
tex.splitlines()
#tex.strip()
print(len(tex.splitlines()))

