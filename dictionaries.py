dic={"name":"ajay","age":"24"}
print(dic["name"])

roll={111:"andi",112:"arun"}
print(roll[111])
print(dic)

#shows error if error
print(dic["age"])

#do not shows error
print(dic.get("name2"))

print(dic.keys())
print(dic.values())
print(dic.items())

for key in dic.keys():
    print(dic[key])

    print(f"for value of key {key} is equal to {dic[key]}")


for key,value in dic.items():
    print(f"{key}={value}")