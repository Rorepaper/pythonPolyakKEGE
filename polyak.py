from os import mkdir, listdir, mknod
from requests import get
import bs4

with open("tasks.txt", "r") as f:
    tasks = f.readlines()

if len(tasks[0].strip()) <= 2:
    a = get(f"https://kpolyakov.spb.ru/school/ege/gen.php?action=viewVar&answers=on&varId={tasks[0]}")
    tasks = tasks[1:]

    soup = bs4.BeautifulSoup(a.text, 'html.parser')
    f = soup.find(class_="vartopic")
    rows = f.find_all('tr')
    n = 0
    data = {}
    for i in rows:
        n += 1
        data[n] = str(i).split("'")[1].split(";")[1][:-2]
        if n == 19:
            n += 2
    tasks2 = []
    for task in tasks:
        tasks2.append(data[int(task)])
    tasks = tasks2

for task in tasks:
    a = get(f"https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId={task}")
    soup = bs4.BeautifulSoup(a.text, 'html.parser')
    numb = soup.text.split("№")[2].split()[0][:-1]
    ans = soup.find(class_="hidedata")
    ans = str(ans).split("'")[1]
    a = str(soup.find(class_="topicview")).split("\n")

    if numb not in ["1", "4", "6", "11"]:
        if numb not in listdir():
            mkdir(numb)

    b = a[2].split("'")[1].split("href")
    if len(b) > 1:
        b = b[1].split("\"")[1]
        ur = "https://kpolyakov.spb.ru/cms/files/" + b
        nam = b.split("/")[-1]
        get_response = get(ur, stream=True)
        mknod(f"{numb}/{task}pol.{nam.split('.')[-1]}")
        with open(f"{numb}/{task}pol.{nam.split('.')[-1]}", 'wb') as f:
            for chunk in get_response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
    if numb not in ["1", "3", "4", "6", "7", "10", "11", "18", "22"]:
        mknod(f"{numb}/{task}pol.py")

    text = a[2].split("'")[1]
    pic = text.split("src")[1].split("\"")[1]
    text = text.replace(pic, "https://kpolyakov.spb.ru/cms/images/" + pic)
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(f"<h1>Задание:{numb}</h1><h2>Номер:{task}</h2>" + text + f"<h2>Ответ:\n{ans}</h2>")
    input("Нажмите Enter, чтобы включить следующее")
