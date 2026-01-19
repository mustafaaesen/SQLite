import sqlite3

con=sqlite3.connect("kutuphane.db")# veritabani dosyasi olusturup baglanti saglar
#baglantiyi con adli degiskenle saglariz

#<----Islemler--->
#veritabaninda yapilacak islemler icin imlec lazim(cursor)
#bunu cursor ile saglariz

cursor=con.cursor()

#<-----Tablo Oluşturma -------->


def tabloOlustur():# veritabanında tablo oluşturan fonksiyon

    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik(İsim TEXT,Yazar TEXT , Yayınevi TEXT, Sayfa_Sayısı INT)")
    # imlecin(cursor) execute komutu ile  veritabanında tablo oluşturan kodu yazabiliriz

    con.commit()# veritabnında ilgili değişikliklerin yapılabilmesi için yazılan komut


#<------- Tablolara Veri Ekleme--------->

#INSERT INTO tablo_adi VALUES(" değerler") syntaxı ile tabloya veri eklemesi yapılabilir
#fonkisyon ile yapılan metodu

def veriEkle(isim,yazar,yayinevi,sayfa_sayisi):
    #kullanıcıdan alınan bilgileri parametre olarak alan  ve tabloya ekleyen veriEkle fonksiyonu
    cursor.execute("INSERT INTO kitaplik VALUES(?,?,?,?)",(isim,yazar,yayinevi,sayfa_sayisi))
    #insert into ile veriler eklenirken ? ile parametre eşeleşecek şekilde ekleme yapılır

    con.commit()#veritabanında ilgili değişikikleri yapılması için


def verileriAl():

    cursor.execute("SELECT * FROM kitaplik")#tüm verileri çeken sorgu
    liste=cursor.fetchall()#sorgunun çalıştığı sırada verileri listeye atayan fonksiyon
    print("Kitaplık Tablosunun Bilgileri...")
    for i in liste:
        print(i)
    #veritabanında değişiklik yapılmadığı için con.commit'e ihtiyaç duyulmaz
    


def verileriAl2():

    cursor.execute("SELECT İsim,Yazar FROM kitaplik")#kitapların ismi ve yazarını geitren sorgu
    liste=cursor.fetchall()

    print("Kitapların Adları ve Yazarları")
    for i in liste:
        print(i)

def verileriAl3(yayinevi):
    cursor.execute("SELECT * FROM kitaplik where Yayınevi = ?",(yayinevi,))
    #yayinevi olarak aranan kelimeyi parametre olarak alır ve ilgili yainevi ile 
    #yayınlanmış kitapları listeler
    liste=cursor.fetchall()
    print("Aradığınız Yayınevinin Kitapları...",yayinevi)
    for i in liste:
        print(i)


def verileriGuncelle(eski_yayinevi,yeni_yayinevi):

    cursor.execute("UPDATE kitaplik SET Yayınevi=? WHERE Yayınevi=?",(yeni_yayinevi,eski_yayinevi))
    #eski ve yeni yayınevlerini parametre olarak alıp güncelleme yapan kısım
    con.commit()#değişiklikleri yapan kısım

def veriSil(yazar):

    cursor.execute("DELETE FROM kitaplik WHERE Yayınevi=?",(yazar,))
    #yazarı parametre olarak alıp  tablodan silen kısım
    con.commit()#değişiklikleri uygulayan taraf

verileriAl()
verileriAl2()
verileriAl3("İnkılap")

verileriGuncelle("Everest Yayıncılık","Doğan Kitapevi")
verileriAl()

veriSil("Ahmet Ümit")

"""isim=input("Kitap İsmi:")
yazar=input("Yazar:")
yayinevi=input("Yayınevi")
sayfa_sayisi=int(input("Sayfa Sayısı:"))

veriEkle(isim,yazar,yayinevi,sayfa_sayisi)"""







con.close()#veritabanini kapatmak icin