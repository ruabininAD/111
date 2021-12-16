import requests
start_url="https://stepic.org/media/attachments/course67/3.6.3/"
with open("dataset_3378_3.txt") as file:
    url=file.readline()
url="https://stepic.org/media/attachments/course67/3.6.3/987573.txt"
#print(url)
first_word = ""
while first_word != "We":
    f=requests.get(url.strip())
    name=f.text

    if first_word == "We":

        break
    else:
        x = name
        url = "https://stepic.org/media/attachments/course67/3.6.3/"+x
        #print(url)
        print(str(name).strip())
        first_word = (name.strip()).split()[0]