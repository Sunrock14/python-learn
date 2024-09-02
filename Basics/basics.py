def basic():
    print(5 + 50)
    print(5 ** 5)

    print(type(10))
    print(type(3.14))

    number = 10
    print(number)
def variables():

    name = 'faruk'
    age = 29
    isMarried = False
    skills = ['ismail','faruk','kocademir']

    detail = {
        'name' : 'İsmail Faruk',
        'surname': 'Kocademir',
        'state': 'Istanbul',
        'age': 20,
        'isMarried' : False,        
        }
    
    print(detail)
    name, age = 'faruk', 20
def arithmetic_operations():
    print('Toplama: ', 1 + 2)
    print('Çıkarma: ', 2 - 1)
    print('Çarpma: ', 2 * 3)
    print ('Bölme: ', 4 / 2)                         
    print('Bölme: ', 6 / 2)
    print('Bölme: ', 7 / 2)
    print('Bölme : ', 7 // 2)   
    print('Mod Alma: ', 101 % 2)                           
    print ('Kalansız bölme: ', 7 // 3)
    print('Üs hesaplama: ', 7 ** 2)                     
def string_operations():
    letter = 'p'
    selectChar = 'Faruk'
    first  = selectChar[0]
    first  = selectChar[2]
    first  = selectChar[0:3]
    first  = selectChar[-1]
    multi_line = '''Lorem ipsum dolor sit amet, 
    consectetur adipiscing elit. Nulla finibus elit ut lectus vehicula, et fermentum urna sagittis. Morbi et sapien at tellus ..'''

    # capitalize() - Metnin ilk harfini büyük yapar, geri kalanını küçük yapar
    print(multi_line.capitalize())

    # count('y') - Metin içinde belirtilen karakterin ('y') kaç kez geçtiğini sayar
    print(multi_line.count('y'))

    # endswith('e') - Metnin belirtilen karakterle ('e') bitip bitmediğini kontrol eder
    print(multi_line.endswith('e'))

    # startswith('Nu') - Metnin belirtilen karakterle ('Nu') başlayıp başlamadığını kontrol eder
    print(multi_line.startswith('Nu'))

    # expandtabs(10) - Metin içinde sekme karakterlerini (\t) 10 boşlukla değiştirir (sekme yoksa etkisizdir)
    print(multi_line.expandtabs(10))

    # find('th') - Belirtilen substring'in ('th') metin içinde ilk bulunduğu indeksi döndürür. Bulamazsa -1 döner.
    print(multi_line.find('th'))

    # format() - Metin içindeki süslü parantezler ile belirtilen yerleri formatlar (Bu metinde kullanılmamış, ama hatalı değil)
    print(multi_line.format())

    # index('a') - Belirtilen karakterin ('a') metin içinde ilk bulunduğu indeksi döndürür. Bulamazsa hata verir.
    print(multi_line.index('a'))

    # isalnum() - Metnin yalnızca harf ve rakamlardan oluşup oluşmadığını kontrol eder (Boşluk, noktalama işaretleri vs. varsa False döner)
    print(multi_line.isalnum())

    # isalpha() - Metnin yalnızca harflerden oluşup oluşmadığını kontrol eder (Boşluk, noktalama işaretleri vs. varsa False döner)
    print(multi_line.isalpha())

    # isdecimal() - Metnin yalnızca ondalık rakamlardan oluşup oluşmadığını kontrol eder (Bu metin harf içerdiği için False döner)
    print(multi_line.isdecimal())

    # isdigit() - Metnin yalnızca rakamlardan oluşup oluşmadığını kontrol eder (Bu metin harf içerdiği için False döner)
    print(multi_line.isdigit())

    # isidentifier() - Metnin geçerli bir Python tanımlayıcısı olup olmadığını kontrol eder (Değişken ismi olarak kullanılabilir mi?)
    print(multi_line.isidentifier())

    # islower() - Metnin tüm karakterlerinin küçük harf olup olmadığını kontrol eder
    print(multi_line.islower())

    # isupper() - Metnin tüm karakterlerinin büyük harf olup olmadığını kontrol eder
    print(multi_line.isupper())

    # isnumeric() - Metnin yalnızca sayısal karakterlerden oluşup oluşmadığını kontrol eder
    print(multi_line.isnumeric())

    # join() - Bu fonksiyon normalde bir iterable'ın (list, tuple vs.) elemanlarını birleştirir. Yanlış kullanılmış.
    # Düzeltilmesi gerek.
    # Örnek doğru kullanım: ','.join(['a', 'b', 'c'])
    # print(multi_line.join())  # Hatalı, bu satır kaldırılmalıdır.

    # strip() - Metnin başındaki ve sonundaki boşlukları (veya belirtilen karakterleri) kaldırır
    print(multi_line.strip())

    # replace() - Bu fonksiyon iki parametre alır: değiştirilmesi istenen eski substring ve yeni substring.
    # Örnek doğru kullanım: multi_line.replace('elit', 'XXXX')
    # print(multi_line.replace())  # Hatalı, bu satır kaldırılmalıdır.

    # split() - Metni, belirtilen ayraç karakteriyle (varsayılan olarak boşluk) böler ve bir liste döndürür
    print(multi_line.split())

    # title() - Metindeki her kelimenin ilk harfini büyük yapar
    print(multi_line.title())

    # swapcase() - Metindeki büyük harfleri küçük yapar ve küçük harfleri büyük yapar
    print(multi_line.swapcase())
def list_operations():
    fruits = ['banana', 'orange', 'mango', 'lemon']                 
    vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      
    countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

    print('Meyveler:', fruits)
    print('Meyve Sayisi:', len(fruits))
    print('Sebzeler:', vegetables)
    print('Sebze sayisi:', len(vegetables))
    
    fruits.append('lime') 
    fruits.insert(2, 'apple')
    fruits.remove('banana')
    fruits.pop()  
    del fruits[0] 
    fruits.clear()     
    fruits_copy = fruits.copy()     
def dictionary():
    person = {
    'first_name':'Faruk',
    'last_name':'Kocademir',
    'age':29,
    'country':'Türkiye',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
        }
    }
    print(person['first_name'])
    person['skills'].append('HTML')
def confitions():

    a = 5
    b = 10
    if a > b:
        print('a büyük')  
    elif b > a:
        print('b büyük')
    else:
        print('eşit')
    
    #tek satırlık if
    print('A is positive') if a > 0 else print('A is negative')

    #Logic opreation
    if a > 0 and a % 2 == 0:
            print('A is an even and positive integer')
    elif a > 0 and a % 2 !=  0:
        print('A is a positive integer')
    elif a == 0:
        print('A is zero')
    else:
        print('A is negative')

    user = 'James'
    access_level = 3
    if user == 'admin' or access_level >= 4:
            print('Access granted!')
    else:
        print('Access denied!')
def while_loops():
    counter = 1
    while counter < 10:
          print('doğruu')
          counter + 1
    
    while counter <10:
         print(True)
         counter+1
    else:
         print(false)
         counter+1
    
    while counter <10:
         print('oke')
         break
    
    while counter <10:
         print('oke')
         continue
def for_loops():
     numbers = [0, 1, 2, 3, 4, 5]
     
     for number in numbers:
          print(number)






































