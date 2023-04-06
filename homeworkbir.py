#değişkenler start
baslik = "HABERİNİZ OLSUN" 
vade = 12
faizOrani=1.47
faizOrani1=1.44

print(baslik)
print(type(baslik))
print(type(vade))
print(type(faizOrani))

mesaj= "Hoşgeldin"
musteriAdi="Rümeysa"
musteriSoyadi="Doğan"
sonucMesaj=mesaj+ " "+ musteriAdi+ " " +musteriSoyadi
print(sonucMesaj)
sayi1=10
sayi2=20
print(sayi1+sayi2)
print(sonucMesaj)

#değişkenler end

#ŞartBlokları start
dolarDun=7.65
dolarBugun=7.75

if dolarDun>dolarBugun:
    print("Azalış oku")
    print("Bitti")
elif dolarDun<dolarBugun:
    print("Artış oku")
else:
    print("Eşittir oku")
    
print("Bitti")

#ŞartBlokları End

#Diziler start
krediler=["Hızlı Kredi","Maaşını Halkbank'tan alanlara özel","Mutlu emekli ihtiyaç kredisi"]

print(krediler)
print(krediler[0])
print(krediler[1])
print(krediler[2])
print(len(krediler))

krediler[0]="Çabuk kredi"
print(krediler)

# print(krediler[3])

#Diziler end

#Döngüler start
krediler=["Hızlı Kredi","Maaşını Halkbank'tan alanlara özel","Mutlu emekli ihtiyaç kredisi"]
#alias
for kredi in krediler:
    print("<option>"+kredi+"<option>")

for i in range(len(krediler)):
    print(krediler[i])

for i in range(3,10):
    print(i)

for i in range(0,11,2):
    print(i)

#Döngüler end

#Fonksiyonlar start

def kredileriListeleri():
    krediler=["Hızlı Kredi","Maaşını Halkbank'tan alanlara özel","Mutlu emekli ihtiyaç kredisi"]
    for kredi in krediler:
        print("<option>"+kredi+"<option>")

kredileriListeleri()

#Fonksiyonlar end