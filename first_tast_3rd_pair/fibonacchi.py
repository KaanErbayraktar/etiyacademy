
# 1 1 2 3 5 8 13 21 34 .....
while True:
    eleman_sayisi = int(input("En az 20 elemanlı olacak şekilde kaç elemanlı Fibonacchi serisi oluşturulsun?:  "))
    if eleman_sayisi <=19:
        print("Lütfen 20'den büyük sayı giriniz.")
    else:
        liste = [1,1]
        for i in range(eleman_sayisi-2):
            sayi = liste[i] + liste[i+1]
            liste.append(sayi)
        print(liste)
        print(len(liste))
        break



    