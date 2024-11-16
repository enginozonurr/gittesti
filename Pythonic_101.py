                                             ## print##


print("Hello World") # ekrana yazdırma
print("Onur\nEnginöz") # alt alta ekrana yazdırma
print("19","03","2001",sep="/") # print parametresi ile boşluk yerine / ekleme
print("{} + {} = {}".format(2,3,2+5)) # bu parametre ile fonksiyon içerisine değer gönderdim
""" çoklu yorum satırı """
# yorum satırı

                             ## Değişkenler ve Veri Tipleri ##
a=3 # tamsayı, int
b=3.24 # float, ondalık
c="Hello World" #string yazı
d=[1,2,3,4,"python"] # liste
e=(1,2,3,4,"python") # tuple
f={"elma":1,"armut":2,"kiraz":5} # sözlük; anahtara karşılık değer ilişkisi taşır
g=False, True
print(type(a)) # hangi veri tipinden olduğunu söyler diğer değişkenlerede uygulayabiliriz ama üşendim

                                ## Matematik Operatörleri##

print(3+4)   # toplama
print(2-1)   # çıkarma
print(2*3)   # çarpma
print(4/2)   # bölme
print(10//4) # tam sayı bölmesi sonucu float istemiyorsak kullanılır.
print(10%4)  # yüzde operatörü 10un 4e bölümünden kalanını bulur

#örnek sayısal toplama
a = 5
b = 10
c = a + 2 * b
#örnek metinsel toplama
a="python"
b="programlama"
c="dili"
d=a+b+c
print(d)
#örnek metinsel çarpım
a="Python"
print(a*5)

print("* " *1)
print("* " *2)
print("* " *3)
print("* " *4)
print("* " *5)
                  ## stringler ve listelerin indekslenmesi##

a="python"
b=[1,2,3,4,5,6,7]
print(a[0])   # sıfırıncı indeksindeki değeri almak istiyorum anlamına gelir
print(a[1])
print(len(a)) # kaç tane karakter olduğunu görmek istersek bunu
print(len(b)) # kaç tane eleman olduğunu görmek istersekte bu şekilde kullanıyoruz
print(a[-1])  # dizedeki son elemanı yazdırır daha uzun yazımıda mevcuttur ama gerek yok
print(a[0:2]) # dizenin sıfırıncı indeksinden başla 2. indeksine kadar devam et ama ikinci indeksi almadan yazdır anlamına geliyor
print(a[2:])  # ikinci indeksten başla sonuna kadar git anlamına gelir bitiş değeri bu şekilde kullanmak istiyorsak koymamız gerekmiyor
print(a[:4])  # baştan başla 4. indekse git ve oraya kadar parçala demiş oluyoruz 4 dahil değil.
print(b[0:6:2]) #sıfırdan başlayarak altıya kadar iki atlayarak git anlamına gelir
print(b[::2]) # yukarıdaki örneğin başka versiyonu başlangıç bitiş değeri vermeden de bu işlem yapılabiliyor

#sözlükler
a={"elma":3,"armut":4,"kiraz":5} # sözlük tanımlandı
print(a["elma"])                 # anahar verip değer yazdırdık
print(a["armut"])
print(a["kiraz"])

## önemli##  sözlükte olmayan bir anahtarı verirsek KeyError hatası ile karşılaşırız
# örneğin
# print(a["çilek"])

                               ## Kullanıcıdan İnput Alma ##

yas=input("Yaşınızı girin: ") # kullanıcıdan değer aldık ancak öncesinde bunu bir değişkene atadık
print("yaşınız",yas)

a= int(input("a: "))
b= int(input("b: "))
c= int(input("c: "))
print("toplam: ",a+b+c)   # inputtan alınan her bir değer python tarafından string değer olarak görünüyor ben burda toplama işlemini yan yana yazdırmak değil de değerleri toplamak amacıyla yapmak istiyorum bu yüzden tür dönüşümü işlemi yaptım ve inputtan aldığım değeri integere dönüştürdüm

                                    ## koşul durumları ##
                                    #333333333333