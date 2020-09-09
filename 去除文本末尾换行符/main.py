txt = ""
with open("get.txt",encoding="utf-8") as f:
    while True:
        line = f.readline().strip("'\n")
        if not line:
            break
        txt += line + " "


print(txt)
with open("res.txt","w") as file:
    file.write(txt)
