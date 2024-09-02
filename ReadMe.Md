# Django ile web sitesi hazırlanması

İlk olarak ptyhon  websitesinden python yükle

Versiyon kontrol et. Ardından django kurulumu yap.
```
python3 --version
pip3 install django
```

Aşağıdaki komut ile yüklenen paketleri kontrol edebilirsin.
```
pip3 freeze
```
Aşağıdaki komut ile web geliştirme yapmak için gerekli komutları görebilirsin.
```
django-admin 
```
Bu komut ile bir django projesi oluşturabilirsin.

```
django-admin startproject WebsiteName
cd WebsiteName
python manage.py runserver
```
## Sanalaştırma
Python tüm paketleri global olarak tutuyor. Ve biz her projenin ayrı ayrı paket kullanmasını isteyebiliriz.
Bundan dolayı sanallaştırma kullanılabilir.

```
python3 -m venv myproject-env

```

sanal ortamda çalışmak için activate.bat çalıştırmak gerekiyor.

..\Scripts\activate.bat

## Yeni uygulama oluşturma
Bir proje içerisinde birden fazla uygulama olabilir. Bu sebeple bir proje altına bir uygulama açmamız gerekiyor.

```

```