from os import mkdir, listdir, mknod
from json import load
from io import StringIO
from requests import get

with open("tasks.txt", "r") as f:
    tasks = f.readlines()

for task in tasks:
    a = load(StringIO(get(f"https://kompege.ru/api/v1/task/{task}").text))
    numb = str(a["number"])
    ans = "\n".join(str(a["key"]).split('\\n'))

    if numb not in listdir():
        mkdir(numb)

    if "files" in dict(a).keys():
        ff = a["files"]
        for i in ff:
            ur, nam = i["url"], i["name"]
            get_response = get(f"https://kompege.ru{ur}", stream=True)
            mknod(f"{numb}/{task}{nam.split('.')[-1]}")
            with open(f"{numb}/{task}{nam.split('.')[-1]}", 'wb') as f:
                for chunk in get_response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)

    mknod(f"{numb}/{task}.py")

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(f"<h1>Задание:{numb}</h1><h2>Номер:{task}</h2>" + a["text"] + f"<h2>Ответ:{ans}</h2>")
    input("Нажмите Enter, чтобы включить следующее")
