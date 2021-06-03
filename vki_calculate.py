"""
VKİ 18 ile < 25 aralığındaysa normal,
VKİ 25 ile <30 aralığındaysa kilolu,
VKİ 30 ve daha yüksekse obez,
VKİ 35 ve daha fazlaysa ciddi obez olarak kabul edilir.
VKİ’ni hesaplayarak kişinin durumunu yazdırınız
(VKİ=ağırlık/(boy*boy), boymetre cinsinden verilmeli)

try:
    hata oluşabilecek satıralr
except:
    hata oluşursa burası çalışacak

"""
while True:
    try :
        agr=float(input("Lütfen kilonuzu giriniz : "))
        boy=float(input("Lütfen boyunuzu metre cinsinden giriniz : "))
    except:
        print("Lütfen geçerli bir sayı giriniz.")
        continue
    vki=agr/boy**2
    print(vki)
    if 18<=vki<25:
        print("Kilonuz Gayet Normal Afferim..")
    elif 25<=vki<30:
        print("Fazla kilo Almışsın azıcık şu boğazını kıs...")
    elif 30<=vki<35:
        print("Abooo kız sana nolmuş??")
    else:
        print("Allah affetsin...")
    break

