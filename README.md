# Hepsiburada Fiyat Kontrolü ve Mail Bildirim Uygulaması
Bu uygulama, belirli bir Hepsiburada ürününün fiyatını takip eder ve istenilen bir fiyata düştüğünde kullanıcıya e-posta ile bildirim gönderir.

## Nasıl Çalışır?
smtplib, time, requests ve BeautifulSoup kütüphaneleri projeye dahil edilir.
Kullanıcıdan Hepsiburada ürününün URL'si alınır.
HTTP isteği göndermek için gerekli olan kullanıcı ajanı (user agent) belirtilen headers tanımlanır.
fiyatkontrol() fonksiyonu, verilen URL üzerindeki sayfayı çeker ve fiyatı kontrol eder.
mail() fonksiyonu, e-posta gönderme işlemini gerçekleştirir. Gerekli SMTP ayarları yapılır ve e-posta içeriği oluşturulur.
Sonsuz bir döngü başlatılır. Her döngüde fiyatkontrol() fonksiyonu çalıştırılır ve belirli bir süre (3600*24 saniye) beklenir.
## Kurulum
Bu uygulamayı çalıştırabilmek için Python 3'ün yüklü olması gerekmektedir.
smtplib, time, requests ve beautifulsoup4 kütüphanelerini yükleyin:
"pip install smtplib time requests beautifulsoup4"
## Kullanım
Program çalıştırıldığında, Hepsiburada üzerinde izlemek istediğiniz ürünün URL'sini girin.
Ardından, bir fiyat belirleyin. Eğer ürünün fiyatı bu değeri geçerse size e-posta ile bildirim gönderilecektir.
Yönlendirmek istediğiniz e-posta adresini girin.
Artık program her 24 saatte bir fiyatı kontrol edecek ve istenilen fiyata düştüğünde size bildirim gönderecektir.
Bu uygulama, belirli bir ürünün fiyatını takip etmek ve istenilen bir fiyata düştüğünde size bildirim göndermek için basit bir örnektir. Kendi ihtiyaçlarınıza göre uyarlayabilir ve geliştirebilirsiniz.

Uyarı: Bu uygulama, yalnızca öğrenme amaçlıdır. Gerçek projelerde e-posta ve web sitesi scraping gibi işlemleri yaparken, ilgili hizmet sağlayıcının kullanım şartlarına ve izinlerine uygun hareket etmeniz önemlidir.
