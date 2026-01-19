#<------- Kütüphane Veritabanı Örneği--------->

import sqlite3

import time

class Kitap():

    def __init__(self,isim,yazar,yayinevi,tur,baski):
        self.isim=isim
        self.yazar=yazar
        self.yayinevi=yayinevi
        self.tur=tur
        self.baski=baski
        #kitap nesnesi türetebilmek için tanımlanan kitap sınıfı fonksiyonu

    
    def __str__(self):

        return "Kitap İsmi: {}\nYazarı: {}\nYayınevi: {}\nTür: {}\nBaskı: {}\n".format(self.isim,self.yazar,self.yayinevi,self.tur,self.baski)
        #kitap hakkında bilgileri döndürecek str fonksiyonu



class Kutuphane():

    def __init__(self):


        self.baglantiOlustur()

    def baglantiOlustur(self):
        self.baglanti=sqlite3.connect("kutuphane.db")#bağlantı oluşturacak fonksiyon

        self.cursor=self.baglanti.cursor()#gezebilmek için cursor

        sorgu="CREATE TABLE IF NOT EXISTS kitaplar(İsim TEXT, Yazar TEXT, Yayınevi TEXT, Tür TEXT, Baskı INT)"
        #veritabanında kitaplar adında tablo oluşturacak sorgu

        self.cursor.execute(sorgu) #sorgunun çalışması

        self.baglanti.commit()#değşiikliklerin  uygulanması iiçn commit 
    
    def baglantiKes(self):
        self.baglanti.close()
    

    def kitaplariGoster(self):

        sorgu="SELECT * FROM kitaplar" # kitapların döndürecek sorgu
        self.cursor.execute(sorgu)

        kitaplar=self.cursor.fetchall()#tüm itapları liste içinde tuple formatında kitaplar 
                                       #listesine atar

        if(len(kitaplar)==0):
            print("!!!Kütüphanede Kayıtlı Kitap Bulunmuyor... !!!")
        
        else:

            for i in kitaplar:
                kitap=Kitap(i[0],i[1],i[2],i[3],i[4])
                #listedeki her elemanı kitap nesnesine atayarak nesne oluşturur

                print(kitap)#kitap nesnesin str fonksiyonu ile yazdırır

    
    def kitapSorgula(self,isim):

        sorgu="SELECT * FROM kitaplar WHERE İsim=?"#isme göre kitap sorgulayan sorgu

        self.cursor.execute(sorgu,(isim,))

        kitaplar=self.cursor.fetchall()# dönen sonucu kitaplar listesine atar

        if(len(kitaplar)==0):
            print("!!! Kitap Kaydı Bulunamadı...!!!")

        else:

            kitap=Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4])
            # sorguda liste içinde tek tuple değeri döner varsa eğer kayıt
            #bu şekilde iki boyutlu listeymiş gibi değerlere ukaşılıp Kitap nesnesine paramtre
            #olarak gönderilir böylelikle nesne türetili

            print(kitap)

    def kitapEkle(self,kitap): #kitap objesi doğrudan paramtre olur

        sorgu="INSERT INTO kitaplar VALUES(?,?,?,?,?)"

        self.cursor.execute(sorgu,(kitap.isim,kitap.yazar,kitap.yayinevi,kitap.tur,kitap.baski))
        #nesnenin özelliklerini parametre olarak gönderiyoruz

        self.baglanti.commit()#db de değişikikliklerin yapılması için
    
    def kitapSil(self,isim):

        sorgu="DELETE FROM kitaplar WHERE İsim=?"

        self.cursor.execute(sorgu,(isim))#alınan ismi paramtre gönderip silen komut

        self.baglanti.commit()

    def baskiYukselt(self,isim):

        sorgu="SELECT * FROM kitaplar WHERE İsim=?"
        #güncellenecek kitabı arayan sorgu

        self.cursor.execute(sorgu,(isim,))


        kitaplar=self.cursor.fetchall()#sorguyu demet şeklinde kitaplar listesine atayan komut

        if(len(kitaplar)==0):

            print("!!!Kitap Kaydı Bulunamadı...!!!")

        else:
            #eleman vardı kitabın ilgili indexindeki baskı sayısı güncellenmeli

            baski=kitaplar[0][4]# 4. index baskı sayısıdır
            baski+=1

            #güncellenen değişekenin veritabnına da yazılması lazım 

            sorgu2="UPDATE kitaplar SET Baskı WHERE İsim=?"
            self.cursor.execute(sorgu2,(baski,isim))
            self.baglanti.commit()