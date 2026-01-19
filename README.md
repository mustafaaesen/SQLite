# SQLite ile SQL Pratikleri

Bu repository, proje geliştirmeye geçmeden önce SQL mantığını pekiştirmek için yapılan
SQLite tabanlı çalışmaları içerir.

Amaç; framework veya ORM kullanmadan, doğrudan SQL yazarak veritabanı işlemlerini
terminal ve Python ortamında denemek ve temel veritabanı düşünme alışkanlığı kazanmaktır.

---

## Çalışma Amacı

Flask, Django veya PostgreSQL gibi daha büyük yapılara geçmeden önce;

- SQL sorgularının nasıl çalıştığını görmek
- cursor mantığını öğrenmek
- CRUD işlemlerini elle yazmak
- veritabanı işlemlerini kod tarafında kontrol etmek

için SQLite kullanılarak pratik yapılmıştır.


---

## Çalışma Yaklaşımı


Veritabanı işlemleri:
- Python’un `sqlite3` modülü kullanılarak
- cursor üzerinden SQL sorguları çalıştırılarak
- terminalde çıktı alınarak

simüle edilmiştir.

Önce SQL öğrenilmiş, sonra bu SQL kodları küçük senaryolarla bir araya getirilmiştir.

---

## Dosya İçeriği

### `ders1-veritabani.py`

Bu dosyada SQLite ile temel veritabanı işlemleri yapılmıştır.

- Veritabanı bağlantısı kurulmuştur
- Tablo oluşturulmuştur
- Parametreli sorgular kullanılarak:
  - veri ekleme
  - veri listeleme
  - veri güncelleme
  - veri silme

işlemleri fonksiyonlar hâlinde yazılmıştır.

Bu dosya SQL’e ve SQLite’a ilk alışma aşamasını temsil eder.

---

### `ders2kutuphane.py`

Bu dosyada veritabanı işlemleri nesne tabanlı yapıya taşınmıştır.

- Kitapları temsil eden bir `Kitap` sınıfı oluşturulmuştur
- Veritabanı işlemlerini yöneten `Kutuphane` sınıfı yazılmıştır
- SQL sorguları sınıf metotları içinde toplanmıştır

Veritabanından gelen kayıtlar doğrudan nesnelere dönüştürülerek kullanılmıştır.
Bu yapı, daha sonra ORM ' de işimize yarayacak altyapıyı oluşturmaktadır.

---

### `ders2kutuphaneproje.py`

Bu dosyada önceki iki aşamada yazılan kodlar birleştirilerek
komut satırı üzerinden çalışan basit bir kütüphane otomasyonu oluşturulmuştur.

- Menü yapısı ile kullanıcıdan input alınmıştır
- Kitap ekleme, silme, sorgulama ve güncelleme işlemleri yapılmıştır
- Veritabanı işlemleri ayrı bir modül olarak kullanılmıştır

Amaç, SQL ve Python ile yazılan kodların küçük bir senaryo içinde nasıl çalıştığını görmektir.

---

### `kutuphane.db`

Bu dosya eğitim sırasında oluşturulmuş örnek SQLite veritabanıdır.
Gerçek veya hassas veri içermez, yalnızca deneme amaçlı kullanılmıştır.

---



## Sonrasında Ne Yapıldı?

Bu çalışmalardan sonra:
- PostgreSQL kullanılarak daha gelişmiş veritabanı konularına geçilmiştir
- Flask ve Django projelerinde bu temel bilgiler kullanılmıştır

Bu repo, o aşamalara geçmeden önce yapılan hazırlık çalışmasıdır.
