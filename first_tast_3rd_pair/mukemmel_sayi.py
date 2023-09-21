

x = int(input("Lütfen bir sayı giriniz: "))
sayi = 0
for i in range(1,x):
    if x % i == 0:
        print(i)
        sayi = sayi + i
if x == sayi:
    print(f"{sayi} mükemmel bir sayıdır.")
else:
    print(f"{x} sayısının kendinden küçük tam bölenlerinin toplamı {sayi}'dır. Bu sayı mükemmel bir sayı değildir.")




