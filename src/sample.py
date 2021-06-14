import os

a = []
for file in os.listdir("src/cogs"):
    if file.endswith(".py"):
        a.append(file.replace(".py",""))

print(a)