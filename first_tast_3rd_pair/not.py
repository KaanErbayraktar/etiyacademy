

vize = int(input("Vize notunu giriniz: "))
final = int(input("Final notunu giriniz: "))

if vize<=100 and vize>=0: 
    if final <=100 and final>=0:
        vize = vize*0.4
        final = final*0.6
        total = vize + final
        if total >= 80:
            harf = "AA"
            print("Notunuz:{}, Harf Notunuz:{}".format(total, harf))
        elif total >= 70:
            harf = "BB"
            print("Notunuz:{}, Harf Notunuz:{}".format(total, harf))
        elif total >= 60:
            harf = "CC"
            print("Notunuz:{}, Harf Notunuz:{}".format(total, harf))
        elif total >= 50:
            harf = "DD"
            print("Notunuz:{}, Harf Notunuz:{}".format(total, harf))
        else:
            harf = "FF"
            print("Notunuz:{}, Harf Notunuz:{}".format(total, harf))
    else:
        print("Lütfen geçerli sayı giriniz.")
else:
    print("Lütfen geçerli sayı giriniz.")

