
## Proje Hakkında  

## Proje Hakkında  

Günümüzde güvenlik sorunlarının artması, kamera güvenlik sistemlerinin gerekliliğini ve kullanımını artırmaktadır. Güvenlik sistemlerini ve kameralarını takip etmek için çeşitli programlar ve güvenlik personeli kullanılmaktadır. Çoğu yerde, kamera takibi için sürekli olarak video kaydı yapılmakta ya da sadece kameradan gelen görüntünün aktarıldığı monitörlerden izlenebilmekte ve yalnızca güvenlik sorunu oluştuğunda müdahale edilebilmektedir. Sürekli insan denetimi ihtiyacı, kamera tabanlı güvenlik izleme sistemlerinin en büyük dezavantajlarından biridir. Çünkü insanlar, sınırlı sayıda saat ekran akışına odaklanarak dikkati dağılmadan çalışabilirler.  

Bu nedenle, canlı video analiz yöntemi aracılığıyla çeşitli güvenlik olaylarının takip edilmesi ve tespit edilerek otomatik olarak uyarı verilmesi önemlidir. Günümüzde şehirlerin hemen hemen her tarafında güvenlik kameraları bulunmaktadır. Önerilen proje kapsamında, bu kameralar aracılığıyla alınan görüntüleri bilgisayarlı görü tabanlı analiz ederek hırsızlık olaylarının tespit ve takibi üzerine bir çalışma yapılacaktır.   

Plakalar açık halde ise, açık plakaların tespiti yapılarak veritabanımıza kaydedilecektir. Bu sayede, şüpheli bir durumda içeride kimlerin bulunduğu ve hangi plakalı araçların içeride olduğu tespit edilebilecektir. Eğer plaka tespit edilemiyorsa veya kapalıysa, bu durum şüpheli olarak algılanacaktır. Projede özellikle, plakası kapalı araçlar ve at arabası ile yapılan hırsızlık olaylarının tespit edilmesine odaklanılacaktır. Alınan kamera görüntülerinde at arabası veya motorlu araçların şantiyeler veya fabrikalar etrafında dolaşması, şüphe uyandıran durumların tespit edilmesi sağlanacaktır. Bu tarz durumlar tespit edildikten sonra kayıt altına alınacak ve yetkili kişilere e-posta yoluyla uyarı verilecektir.

## Kullanılan Teknolojiler 

- Derin Öğrenme Modelleri: YOLOv4, YOLOv5, YOLOv8  
- Web Çerçevesi: Django
- Görüntü İşleme: OpenCV 
- Veritabanı: SQLite
- İletişim: SMTP protokolü ile e-posta gönderimi

## Özellikler  

- Görüntü işleme algoritmaları  
- Nesne tanıma ve sınıflandırma  
- Makine öğrenimi entegrasyonu  
- Kullanıcı dostu arayüz
- Plaka Tanıma
- Canlı Video Analizi
- Otomatik Uyarı Sistemi

## Gereksinimler  

- Python 3.x  
- Gerekli kütüphaneler:  
  - OpenCV  
  - NumPy  
  - Matplotlib  
  - scikit-learn

    
## Algoritmalar  

Bu projede kullanılan bazı temel algoritmalar şunlardır:  

1. **Görüntü Filtreleme**: Görüntülerin gürültüsünü azaltmak için çeşitli filtreleme teknikleri (örneğin, Gauss filtresi) kullanılır.  
2. **Nesne Tanıma**: Görüntülerdeki nesneleri tanımak için derin öğrenme tabanlı modeller (örneğin, YOLO, SSD) kullanılır.  
3. **Öznitelik Çıkartma**: Görüntülerden özniteliklerin çıkartılması için SIFT veya ORB gibi algoritmalar kullanılır.
4.  **Plaka Tanıma**: Araç plakalarının otomatik olarak tanınması için özel algoritmalar geliştirilmiştir. Bu algoritmalar, görüntülerdeki plakaları tespit eder ve veritabanına kaydeder.  
5. **Olay Tespiti**: Canlı video akışında şüpheli durumların tespiti için makine öğrenimi teknikleri kullanılmaktadır. Bu sayede, güvenlik ihlalleri anında algılanarak gerekli önlemler alınabilir.  

## Deneysel Sonuçlar  

- YOLOv4: %95 kapalı plaka, %98 açık plaka, %96 at arabası doğruluğu 
- YOLOv5: %100 kapalı plaka, %99 açık plaka, %98 at arabası doğruluğu
- YOLOv8: %98 kapalı plaka, %99 açık plaka, %97 at arabası doğruluğu
- Sonuç: YOLOv8, doğruluk ve hız açısından en dengeli performansı sergilemiştir.

## Kullanım Senaryoları 

- Fabrika ve Şantiyeler: Şüpheli araçların tespiti ve giriş-çıkış takibi
- Şehir Güvenliği: Hırsızlık girişimlerinin gerçek zamanlı analizi
- E-posta Bildirimi: Tespit edilen şüpheli durumların yetkililere anında iletilmesi

## Kurulum  

1. **Depoyu Klonlayın:**  

git clone https://github.com/Buse-cetin/ComputerVisionn.git  
cd ComputerVisionn

2.**Gerekli Kütüphaneleri Yükleyin:**
pip install -r requirements.txt

## Kullanım
cd movieapp
activate.bat
python manage.py runserver

## İletişim
Herhangi bir sorunuz veya geri bildiriminiz varsa, lütfen benimle iletişime geçin:

E-posta: buseetinn@gmail.com
