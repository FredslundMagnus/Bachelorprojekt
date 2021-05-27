from os import listdir
from os.path import join


def getFiles(folder: str):
    for d in listdir(folder):
        if d == 'empty.txt' or "Markdown" not in list(listdir(join(folder, d))):
            continue
        for name in listdir(join(folder, d, "Markdown")):
            with open(join(folder, d, "Markdown", name)) as file:
                for line in file:
                    if "Minutes used" in line and "minutes." in line:
                        yield int(line.split(' ')[-2])


def getTime(folder: str):
    print(folder.split("\\")[-1])
    minutes = sum(getFiles(folder))
    hours = minutes/60
    days = hours/24
    print(f"{minutes=}")
    print(f"{hours=}")
    print(f"{days=}\n")


print("")
getTime("C:\\Users\magnu\Desktop\old_outputs")
getTime("outputs")
