from ders2kutuphane import *

# kutuphane kodlarının yazıldığı dosyayı import edip modul olarak kullanma

#Yapılacaklar
#modul olarak import ettiğimiz kutuğhane sınıfından nesne türeterek veritabanı oluşturulur
#daha sonra işlemler yapılabilir




print(""" <----------------------KÜTÜPHANE OTOMASYONUNA HOŞGELDİNİZ------------------------->
      

    İşlemler
      1--->Kitapları Göster
      2--->Kitap Sorgula
      3--->Kitap Ekle
      4--->Kitap Sil
      5--->Baskı Yükselt

      Çıkış İçin 'q'ya Basin

<--------------------------------------------------------------------------------->""")


kutuphane=Kutuphane()
while True:

    islem=input("Yapacağınız İşlemi Seçiniz")

    if(islem=='q'):

        print("Program Sonlandırılıyor...")

        print("Yine Bekleriz:)")

    
    elif(islem=='1'):

        kutuphane.kitaplariGoster()
    
    elif(islem=='2'):

        isim=input("Sorgulamak İstediğiniz Kitabı Giriniz\n")
        print("Kitap Sorgulanıyor...")
        time.sleep(2)

        kutuphane.kitapSorgula(isim)

    elif(islem=='3'):
        isim=input("Kitap Adı Giriniz:\n")
        yazar=input("Yazar Adı Giriniz:\n")
        yayinevi=input("Yayınevi Giriniz:\n")
        tur=input("Türüni Giriniz:\n")
        baski=int(input("Baski Girniz:\n"))

        yeni_kitap=Kitap(isim,yazar,yayinevi,tur,baski)#yeni girilen bilgilerden nesne turetme
        print("Kitap Ekleniyor...")
        time.sleep(2)

        kutuphane.kitapEkle(yeni_kitap)#turetilen nesnenin eklenmesi
        print("Kitap Eklendi !!!")


        
    elif(islem=='4'):

        isim=input("Silmek İstediğiniz Kitap Adını  Giriniz:\n")
        cevap=input("Emin misiniz?  (E/H)")

        if(cevap=='E'):
            print("Kitap Siliniyor...\n")
            time.sleep(2)

            kutuphane.kitapSil(isim)
            print("Kitap Silindi!!!")
    elif(islem=='5'):

        isim=input("Hangi Kitabın Baskisini Yükseltmek İstiyorusunuz:\n")
        print("Baski Yükseltiliyor...")
        time.sleep(2)

        kutuphane.baskiYukselt(isim)
        print("Baskı Yükseltildi")

        
    
    else:
        print("Geçersiz Seçim Yaptınız!!!\nLütfen Tekrar Deneyiniz")