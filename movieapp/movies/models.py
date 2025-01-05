from django.db import models

# Create your models here.
class About_Information(models.Model):
    informate = models.CharField("Bilgi",max_length=200, null=True)
    title = models.CharField("Başlık",max_length=200, null=True)  
    imageUrl = models.ImageField("Resim Url",blank=True, null=True)
    #button = models.CharField("Buton",max_length=200, null=True)

    def __str__(self):
        return f"{self.title}"


    class Meta:
        verbose_name = "Bilgi"
        verbose_name_plural = "Bilgiler"

class Other(models.Model):
    see = models.CharField(max_length=200, null=True)

class Example(models.Model):
    see = models.CharField(max_length=200, null=True)

class Communication(models.Model):
    title = models.CharField("Başlık",max_length=200, null=True)
    informate = models.CharField("Bilgi",max_length=200, null=True)
    email = models.EmailField("E-Mail", null=True)
    telephone=models.IntegerField()
    addresss = models.CharField("Adres",max_length=200, null=True)

    def __str__(self):
        return f"{self.title} {self.email} {self.telephone}"

    class Meta:
        verbose_name = "İletişim"
        verbose_name_plural = "İletişim Bilgileri"

class Gallery(models.Model):
    informate = models.CharField("Bilgi",max_length=200, null=True)
    title = models.CharField("Başlık",max_length=200, null=True)
    subtitle_one = models.CharField("AltBaşlık",max_length=200, null=True)
    subtitle_two = models.CharField("AltBaşlık",max_length=200, null=True)
    subtitle_three = models.CharField("AltBaşlık",max_length=200, null=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Galeri"
        verbose_name_plural = "Galeri"

class Testimonial(models.Model):
    title_one = models.CharField("Başlık 1",max_length=200, null=True)
    informate_one = models.CharField("Bilgi 1",max_length=200, null=True)
    imageUrl_one = models.ImageField("Resim Url 1",blank=True, null=True)
    title_two = models.CharField("Başlık 2",max_length=200, null=True)
    informate_two = models.CharField("Bilgi 2",max_length=200, null=True)
    imageUrl_two = models.ImageField("Resim Url 2",blank=True, null=True)
    title_three = models.CharField("Başlık 3",max_length=200, null=True)
    informate_three = models.CharField("Bilgi 3",max_length=200, null=True)
    imageUrl_three = models.ImageField("Resim Url 3",blank=True, null=True)
    title_four = models.CharField("Başlık 4",max_length=200, null=True)
    informate_four = models.CharField("Bilgi 4",max_length=200, null=True)
    imageUrl_four = models.ImageField("Resim Url 4",blank=True, null=True)
    title_five = models.CharField("Başlık 5",max_length=200, null=True)
    informate_five = models.CharField("Bilgi 5",max_length=200, null=True)
    imageUrl_five = models.ImageField("Resim Url 5",blank=True, null=True)

    def __str__(self):
        return f"{self.title_one}"
    

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonial"

class Team_Members(models.Model):
    name= models.CharField("Ad", max_length=200, null=True)
    imageUrl = models.ImageField("Resim Url",blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Ekip Üyeleri"
        verbose_name_plural = "Ekip Üyeleri"

class Information(models.Model):
    informate = models.CharField("Bilgi",max_length=20000, null=True)
    title = models.CharField("Başlık",max_length=200, null=True)
    button = models.CharField("Alt Başlık",max_length=200, null=True)
    
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = "Hakkımızda Bilgi"
        verbose_name_plural = "Hakkımızda Bilgi Sayfası"

class Information_two(models.Model):
    info = models.CharField("Kısa Bilgi",max_length=200, null=True)
    title = models.CharField("Başlık",max_length=200, null=True)
    subtitle = models.CharField("Alt Başlık",max_length=200, null=True)
    informate = models.CharField("Bilgi",max_length=20000, null=True)
    button = models.CharField("Buton",max_length=200, null=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Bilgi 2"
        verbose_name_plural = "Bilgi Sayfası 2"

class User(models.Model):
    name = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200, null=True)
    email = models.EmailField()
    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = "Kişi"
        verbose_name_plural = "Kişiler"

class Ip(models.Model):
    ip = models.GenericIPAddressField(null=True)

class Plate(models.Model):
    plaka_numarasi = models.CharField(max_length=10)
    tarih = models.DateField(auto_now_add=True)
    saat = models.TimeField(auto_now_add=True)
    plaka_gorseli = models.ImageField(blank=True, null=True)
    #plaka_gorseli = models.ImageField(upload_to='plaka_gorselleri/' , null=True)

    def __str__(self):
       return self.plaka_numarasi  

    class Meta:
        verbose_name = "Plaka"
        verbose_name_plural = "Plakalar"

class Detection(models.Model):
    benzerlik_orani = models.CharField(max_length=30)
    tarih = models.DateField(auto_now_add=True)
    saat = models.TimeField(auto_now_add=True)
    gorsel = models.ImageField(blank=True, null=True)
    #plaka_gorseli = models.ImageField(upload_to='plaka_gorselleri/' , null=True)

    def __str__(self):
       return self.benzerlik_orani  

    class Meta:
        verbose_name = "At Tespiti"
        verbose_name_plural = "At Tespiti"

class PlateDetection(models.Model):
    
    benzerlik_orani = models.CharField(max_length=30)
    isim = models.CharField(max_length=15)
    tarih = models.DateField(auto_now_add=True)
    saat = models.TimeField(auto_now_add=True)
    gorsel = models.ImageField(blank=True, null=True)
    #plaka_gorseli = models.ImageField(upload_to='plaka_gorselleri/' , null=True)

    def __str__(self):
       return self.isim  

    class Meta:
        verbose_name = "Plaka Tespiti"
        verbose_name_plural = "Plaka Tespiti"

class Message(models.Model):
    subject = models.CharField("Konu",max_length=200)
    text = models.CharField("İçerik",max_length=2500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField("Tarih",auto_now=True, null=True)

    def __str__(self):
       return self.subject  #admin sayfasında Mesajlar tablosunda konuyu göster dedim

    class Meta:
        verbose_name = "Mesaj"
        verbose_name_plural = "Mesajlar"

    
class Services(models.Model):
    title = models.CharField("Başlık",max_length=200, null=True)
    informate = models.CharField("Bilgi",max_length=200, null=True)
    title_one = models.CharField("Başlık 1",max_length=200, null=True)
    informate_one = models.CharField("Bilgi 1",max_length=2000, null=True)
    imageUrl_one = models.ImageField("Resim Url 1",blank=True, null=True)
    title_two = models.CharField("Başlık 2",max_length=200, null=True)
    informate_two = models.CharField("Bilgi 2",max_length=2000, null=True)
    imageUrl_two = models.ImageField("Resim Url 2",blank=True, null=True)
    title_three = models.CharField("Başlık 3",max_length=200, null=True)
    informate_three = models.CharField("Bilgi 3",max_length=2000, null=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Servisler"
        verbose_name_plural = "Servisler"