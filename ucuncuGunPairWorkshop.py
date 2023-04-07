# Kullanıcıdan 10 adet sayı alalım ve bu sayılar arasından
#  en büyük olanı kullanıcıya gösterelim.

sayilar=[]
for i in range(3):
    i=int(input("Sayı giriniz: "))
    sayilar.append(i)

print(sayilar)
enBuyukDegisken= max(sayilar)
print(" En büyük sayı " , enBuyukDegisken)


# Kullanıcının vereceği üst limit ile 0'dan bu üst limite kadar
#  olan tüm 'çift' sayıları ekrana yazdıralım.

# 2. geliştirdiğimiz programa kullanıcının alt limiti 
# belirlemesi için gerekli desteği ekleyelim.

ustLimit=int(input("Üst Limit Sayıyı Belirle: "))
for ciftsayi in range(0, ustLimit, 2):
    print(ciftsayi)

altLimit=int(input("Alt Limiti Belirleyiniz: "))

for ciftsayi in range(altLimit, ustLimit):
    if ciftsayi%2==0:
        print(ciftsayi)