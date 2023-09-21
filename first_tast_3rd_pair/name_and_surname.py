

list = []
for i in range(1,11):
    name = input("{}. ismi giriniz: ".format(i))
    surname = input("{}. soyismi giriniz: ".format(i))
    fullname = name + " " + surname
    list.append(fullname)
print(list)