

x = int(input("İlk sayıyı giriniz: "))
y = int(input("İkinci sayıyı giriniz: "))
islem = input("İşlem'i seçiniz: ")

while True:

    if islem == "+":
        sonuc = x+y
        print(sonuc)
        break
    elif islem == "-":
        sonuc = x-y
        print(sonuc)
        break
    elif islem == "*":
        sonuc = x*y
        print(sonuc)
        break
    elif islem == "/":
        sonuc = x/y
        print(sonuc)
        break
    else: 
        islem = input("Lütfen geçerli bir işlem giriniz: ")