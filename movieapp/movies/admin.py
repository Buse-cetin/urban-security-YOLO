from django.contrib import admin
from .models import  About_Information, Example, Other, Gallery, Communication, Testimonial, Team_Members, Information, Information_two, Services, User, Message, Ip, Plate, PlateDetection, Detection 

class BlogAdmin(admin.ModelAdmin):
    search_fields = ("title",) #Admin paneline filtreleme özelliği getirdi

class PlateAdmin(admin.ModelAdmin):
    list_display = ("plaka_numarasi","tarih","saat") #Admin panelinde bu tablonun girişine bu verileri çektim.
    #readonly_fields = ("plaka_numarasi") sadece okunabilir özellik ekler
    search_fields = ("plaka_numarasi","tarih","saat") #Admin paneline filtreleme özelliği getirdi
    list_filter = ("plaka_numarasi","tarih","saat") #filtreleme işlemi

class HorseDAdmin(admin.ModelAdmin):
    list_display = ("benzerlik_orani","tarih","saat") #Admin panelinde bu tablonun girişine bu verileri çektim.
    #readonly_fields = ("plaka_numarasi") sadece okunabilir özellik ekler
    search_fields = ("benzerlik_orani","tarih","saat") #Admin paneline filtreleme özelliği getirdi
    list_filter = ("benzerlik_orani","tarih","saat") #filtreleme işlemi

class PlateDAdmin(admin.ModelAdmin):
    list_display = ("isim","benzerlik_orani","tarih","saat") #Admin panelinde bu tablonun girişine bu verileri çektim.
    search_fields = ("isim","benzerlik_orani","tarih","saat") #Admin paneline filtreleme özelliği getirdi
    list_filter = ("isim","benzerlik_orani","tarih","saat") #filtreleme işlemi

# Register your models here.
admin.site.register(About_Information),
admin.site.register(Example),
admin.site.register(Other),
admin.site.register(Communication, BlogAdmin),
admin.site.register(Gallery),
admin.site.register(Testimonial),
admin.site.register(Team_Members),
admin.site.register(Information),
admin.site.register(Information_two),
admin.site.register(User),
admin.site.register(Message),
admin.site.register(Ip),
admin.site.register(Services),
admin.site.register(PlateDetection, PlateDAdmin),
admin.site.register(Detection, HorseDAdmin),
admin.site.register(Plate, PlateAdmin),