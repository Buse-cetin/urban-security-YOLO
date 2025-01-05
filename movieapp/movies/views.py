from django.shortcuts import render
from .models import About_Information, Communication, Gallery, Information, Team_Members, Testimonial, Information_two, Services, Message, Ip, Plate
import cv2
import numpy as np
import requests
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
import tkinter as tk    
from PIL import Image, ImageTk
import requests
from smtplib import SMTP
from django.shortcuts import render
from smtplib import SMTP
from django.http import StreamingHttpResponse
import time
import cv2
import numpy as np
import requests
from django.http import StreamingHttpResponse
import datetime
import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image
from io import BytesIO
import os
import base64
from email.mime.text import MIMEText
import uuid  
from django.http.response import HttpResponseRedirect
from itertools import chain
import sqlite3 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule

def veritabanina_kaydet(benzerlik_orani, tarih, saat, gorsel):
    # Veritabanı bağlantısını oluştur
    database_path = "C:\\Users\\BUSE\\Documents\\GitHub\\TUBITAK\\GÖBK_django\\movieapp\\db.sqlite3"
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    #conn = sqlite3.connect('veritabani.db')
    #cursor = conn.cursor()

    # Veritabanı tablosu kontrolü veya oluşturulması
    cursor.execute('''CREATE TABLE IF NOT EXISTS movies_Detection
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       benzerlik_orani TEXT,
                       tarih TEXT,
                       saat TEXT,
                       gorsel BLOB)''')

    # Plakayı veritabanına ekle
    cursor.execute("INSERT INTO movies_Detection (benzerlik_orani, tarih, saat, gorsel) VALUES (?, ?, ?, ?)",
                   (benzerlik_orani, tarih, saat, gorsel))

    # Değişiklikleri kaydet ve bağlantıyı kapat
    conn.commit()
    conn.close()

def veritabani_kayit(isim, benzerlik_orani, tarih, saat, gorsel):
    # Veritabanı bağlantısını oluştur
    database_path = "C:\\Users\\BUSE\\Documents\\GitHub\\TUBITAK\\GÖBK_django\\movieapp\\db.sqlite3"
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    #conn = sqlite3.connect('veritabani.db')
    #cursor = conn.cursor()

    # Veritabanı tablosu kontrolü veya oluşturulması
    cursor.execute('''CREATE TABLE IF NOT EXISTS movies_PlateDetection
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       isim TEXT,
                       benzerlik_orani TEXT,
                       tarih TEXT,
                       saat TEXT,
                       gorsel BLOB)''')

    # Plakayı veritabanına ekle
    cursor.execute("INSERT INTO movies_PlateDetection (isim, benzerlik_orani, tarih, saat, gorsel) VALUES (?, ?, ?, ?, ?)",
                   (isim, benzerlik_orani, tarih, saat, gorsel))

    # Değişiklikleri kaydet ve bağlantıyı kapat
    conn.commit()
    conn.close()
    
def send_email(subject, message, sendTo, sayac_kapali_plaka, sayac_acik_plaka,sayac_at_arabasi):
    try:
        kapali_plaka="Tespit edilen kapalı plaka sayısı: "+str(sayac_kapali_plaka)
        acik_plaka="Tespit edilen açık plakalı araç sayısı :"+str(sayac_acik_plaka)
        at_tespit="Tespit edilen at arabası sayısı: "+str(sayac_at_arabasi)
        # E-posta içeriği oluşturma
        content = f"Subject: {subject}\n\n{kapali_plaka}\n\n{acik_plaka}\n\n{at_tespit}"
        

        # Hesap bilgileri
        my_mail_address = "buseetinn@gmail.com"
        password = "zwgmhpyrfbtqnhlr"

        # SMTP sunucusuna bağlanma
        with SMTP("smtp.gmail.com", 587) as mail:
            mail.ehlo()
            mail.starttls()
            mail.login(my_mail_address, password)
            mail.sendmail(my_mail_address, sendTo, content.encode("utf-8"))

        print(f"E-posta '{subject}' başlıklı mesaj, {sendTo} adresine gönderildi.")
    except Exception as e:
        print(f"Hata oluştu! {e}")

"""# Düzgün çalışması için bir flag ekleyin
mail_sent_flag = False

# schedule fonksiyonunu düzgün kullanma
def schedule_email(subject, message, sendTo):
    global mail_sent_flag
    current_time = time.localtime()

    if (
        current_time.tm_hour == 16
        and current_time.tm_min == 10
        and not mail_sent_flag
    ):
        send_email(subject, message, sendTo)
        mail_sent_flag = True
    elif current_time.tm_hour != 16 or current_time.tm_min != 10:
        mail_sent_flag = False"""


def generate_frames(): 
##config_path = 'C:/Users/BUSE/Desktop/TUBITAK_Plate/custom_yolo_model/yolov4/darknet/plate_yolov4.cfg'
    #weights_path = "C:/Users/BUSE/Desktop/plate_weights/backup-20230815T071458Z-001/backup/plate_yolov4_best.weights"
    #classes_file = 'C:/Users/BUSE/Desktop/TUBITAK_Plate/custom_yolo_model/yolov4/darknet/plate_data/plate.names'

    config_path = 'C:/Users/BUSE/Desktop/yolov4/darknet/darknet/hp_yolov4.cfg'
    #weights_path = "C:/Users/BUSE/Downloads/backup-20240110T194404Z-001/backup/hp_yolov4_best.weights"
    weights_path = "C:/Users/BUSE/Downloads/hp_yolov4_4000.weights"
    classes_file = 'C:/Users/BUSE/Desktop/yolov4/darknet/darknet/HP_data/plate.names'

    #config_path = 'C:/Users/BUSE/Desktop/PH/darknet/HP_yolov4.cfg'
    #weights_path = "C:/Users/BUSE/Downloads/weights2-20231224T205148Z-001/weights2/backup/hp_yolov4_last.weights"
    #classes_file = 'C:/Users/BUSE/Desktop/PH/darknet/HP_data/plate.names'

    # YOLOv4 modelini yükleme
    net = cv2.dnn.readNetFromDarknet(config_path, weights_path)

    # Modelin yapılandırmasını al
    layers = net.getLayerNames()
    #output_layers = [layers[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    output_layers = [layers[i-1] for i in net.getUnconnectedOutLayers()]

    # Sınıf etiketlerini yükleme
    with open(classes_file, 'r') as f:
        classes = f.read().strip().split('\n')

    # Giriş görüntü boyutları
    input_width, input_height = 608, 608

    # Kameradan görüntü almak için url
    #url = "http://10.129.249.102:8080//shot.jpg"
    # Tespit edilen plakaları ve at arabalarını sayan değişkenler
    sayac_kapali_plaka = 0
    sayac_acik_plaka = 0
    sayac_at_arabasi = 0
    at_detected = False  # At tespiti yapıldığını takip eden değişken
    send_interval = 60  # Mail gönderme aralığı (saniye)
    last_email_sent_time = 0  # Son mail gönderme zamanı
    send_email_hour = 9  # Saat 15:16 olarak ayarlandı
    send_email_minute = 53  # Dakika 16 olarak ayarlandı
    mail_sent_flag = False  # mail_sent_flag değişkenini tanımlayın

    url = "http://10.251.29.198:8080//shot.jpg"
    while True:
        messages = Message.objects.all()
        for m in messages:
            subject = m.subject
            message = m.text
            send_to = m.user.email

        current_time = datetime.datetime.now().time()

        # Belirli bir saat ve dakikaya gelindiğinde ve daha önce mail gönderilmediyse mail gönderme işlemi yap
        if current_time.hour == send_email_hour and current_time.minute == send_email_minute \
            and not mail_sent_flag and time.time() - last_email_sent_time > send_interval:
            # Kontrol etmek için bitiş saat, dakika ve saniyeyi ayarla
            end_hour = 22
            end_minute = 46
            end_second = 5

            # Şu anki saat, dakika ve saniye, bitiş saatinden önce mi kontrol et
            if current_time.hour < end_hour or (current_time.hour == end_hour and current_time.minute < end_minute) \
                    or (current_time.hour == end_hour and current_time.minute == end_minute and current_time.second < end_second):
                send_email(subject, message, send_to, sayac_kapali_plaka, sayac_acik_plaka,sayac_at_arabasi)
                last_email_sent_time = time.time()
                mail_sent_flag = True

        

        # Kameradan görüntüyü al
        img_resp = requests.get(url)
        img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
        img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
        img = cv2.resize(img, (640, 480))

        height, width = img.shape[:2]

        # Görüntüyü YOLOv4 için uygun boyuta getirme
        blob = cv2.dnn.blobFromImage(img, 1 / 255.0, (input_width, input_height), swapRB=True, crop=False)

        # YOLOv4 ile tespit yapma
        net.setInput(blob)
        outs = net.forward(output_layers)

        # Tespit sonuçlarını işleme
        class_ids = []
        confidences = []
        boxes = []
        confidence_percent = 0  # confidence_percent değişkenini başlangıç değeriyle tanımla

        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                if confidence > 0.5:  # Minimum güvenilirlik eşiği
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    # Dikdörtgen kutuyu tespitler listesine ekleme
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)       

        # NMS (Non-Maximum Suppression) uygulama
        indices = cv2.dnn.NMSBoxes(boxes, confidences, score_threshold=0.5, nms_threshold=0.4)
        
        # Nesneleri tespit edilen kutuları çizme ve nesne adı ile benzerlik skorlarını yazdırma
        colors = np.random.uniform(0, 255, size=(len(classes), 3))
        for i in indices:
            #i = i[i]  # İndex'i düzeltilmiş haliyle kullan
            box = boxes[i]
            x, y, w, h = box
            class_id = class_ids[i]
            class_name = classes[class_id]
            confidence = confidences[i]

            color = colors[class_id]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)

            # Benzerlik skorunu yüzde olarak hesaplama ve çerçeve içine yazdırma
            confidence_percent = confidence * 100
            score_text = f"Score: {confidence_percent:.2f}%"
            label = f"{class_name} {score_text}"

            label_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 1)[0]
            cv2.rectangle(img, (x, y - label_size[1]), (x + label_size[0], y), color, -1)
            cv2.putText(img, label, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

            # Tespit edilen plakaları ve at arabalarını sayan değişkenler

            

            close_plate_detected = False
            open_plate_detected = False
            horse_detected = False
            if confidence_percent > 65:
                if class_name == "Close Plate" and not close_plate_detected:
                    sayac_kapali_plaka += 1
                    close_plate_detected = True
                    #time.sleep(3)  # 3 saniyelik gecikme ekle
                elif class_name == "Open Plate" and not open_plate_detected:
                    sayac_acik_plaka += 1
                    open_plate_detected = True
    
                    #send_email(subject=subject, message=message, sendTo=sendTo)
                    #time.sleep(3)  # 3 saniyelik gecikme ekle
                elif class_name == "Horse" and not horse_detected:
                    sayac_at_arabasi += 1
                    horse_detected = True  # Mark that a horse has been detected

            # Reset the flags if a detection has occurred
            if close_plate_detected:
                close_plate_detected = False
            if open_plate_detected:
                open_plate_detected = False
            if horse_detected:
                horse_detected = False


        #if class_name == "Open Plate":
            #plaka tespit kodu
        #if classes[class_id] == "Open Plate": 
            #process_and_save_plate_image(url,counter)


            if confidence_percent>50:
                 # veritabanına ve klasöre kaydet
                current_date = datetime.datetime.now().strftime("%Y-%m-%d")
                current_time = datetime.datetime.now().strftime("%H:%M")

                #  veritabanına kaydet
                _, img_encoded = cv2.imencode('.jpg', combined_img)
                plaka_gorseli = img_encoded.tobytes()
                veritabanina_kaydet (label, current_date, current_time, plaka_gorseli)

            """if classes[class_id] == "Horse" or classes[class_id] == "Closed Plate": 
                at_detected = True  # At tespiti yapıldığını işaretle
                if at_detected:
                                    # E-posta mesajları ve kullanıcı bilgilerini alın
                            messages = Message.objects.all()

                            # E-posta gönderme işlemi
                            for m in messages:
                                try:
                                    # E-posta mesajı bilgileri
                                    subject = m.subject
                                    message = m.text
                                    sendTo = m.user.email  # Gönderen e-posta adresi
                                    #recipient_email = "busecetin587@gmail.com"  # Alıcı e-posta adresi

                                    # E-posta içeriği oluşturma
                                    content = "Subject: {0}\n\n{1}".format(subject,message)
                

                                    # Hesap bilgileri
                                    myMailAdress = "buseetinn@gmail.com"  # E-posta hesabınızın adresi
                                    password = "zwgmhpyrfbtqnhlr"  # E-posta hesabınızın şifresi

                                    # SMTP sunucusuna bağlanma
                                    mail = SMTP("smtp.gmail.com", 587)# E-posta sunucusunun adresi ve portu

                                    mail.ehlo()
                                    #verileri şifreleme
                                    mail.starttls()
                                    #mail sunucusunda oturum açma
                                    mail.login(myMailAdress,password)
                                    #maili gönderme
                                    mail.sendmail(myMailAdress, sendTo, content.encode("utf-8"))
                                    print("Mail Gönderme İşlemi Başarılı!")
                                except Exception as e:
                                    print("Hata Oluştu!\n {0}".format(e))

                            #time.sleep(10) #10 saniye aralıklar ile mail gönderir
                            #time.sleep(10) #10 saniye aralıklar ile mail gönderir

                                    #root = tk.Tk()
                                   # root.withdraw()  # Pencereyi gizler
                                   # messagebox.showinfo("Dikkat", "At Arabası tespit edildi, dikkatli olmanızı öneririz!!!")
                                    #time.sleep(10) #10 saniye aralıklar ile mail gönderir"""
        
        # Görüntüyü yatay olarak ikiye bölme
        quarter_width = int(img.shape[1] / 2)
        left_half = img[:, :quarter_width]
        right_half = img[:, quarter_width:]

        # İki çıktıyı yanyana birleştirme
        combined_img = cv2.hconcat([left_half, right_half])

        # Video akışı işlemi
        ret, buffer = cv2.imencode('.jpg', combined_img)
        frame_bytes = buffer.tobytes()

        for frame in range(10):
         yield f"Frame from part 1: {frame}"


        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
        
        # İşlem tamamlandıktan sonra bayrağı sıfırla
        #if current_time.hour != send_email_hour or current_time.minute != send_email_minute:
            #mail_sent_flag = False
            
        print(f"Kapalı Plaka Sayısı: {sayac_kapali_plaka}")
        print(f"Açık Plaka Sayısı: {sayac_acik_plaka}")
        print(f"At Arabası Sayısı: {sayac_at_arabasi}")
    
        
    

#def video_feed(request):
 #  return StreamingHttpResponse(generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame')



def video_feed(request):
    # İki farklı fonksiyonu sırayla çağırarak generator'ları oluştur
    frames_part1 = generate_frames()
    frames_part2 = generate_framestwo()
    
    # İki generator'ı birleştirerek StreamingHttpResponse oluştur
    combined_frames = chain(frames_part1, frames_part2)
    return StreamingHttpResponse(combined_frames, content_type='multipart/x-mixed-replace; boundary=frame')

def generate_framestwo(): 
        # YOLOv4 konfigürasyon dosyasının ve ağırlık dosyasının yolu
    config_path = 'C:/Users/BUSE/Desktop/TUBITAK_Plate/custom_yolo_model/yolov4/darknet/plate_yolov4.cfg'
    weights_path = "C:/Users/BUSE/Desktop/plate_weights/backup-20230815T071458Z-001/backup/plate_yolov4_best.weights"
    classes_file = 'C:/Users/BUSE/Desktop/TUBITAK_Plate/custom_yolo_model/yolov4/darknet/plate_data/plate.names'

    # YOLOv4 modelini yükleme
    net = cv2.dnn.readNetFromDarknet(config_path, weights_path)

    # Modelin yapılandırmasını al
    layers = net.getLayerNames()
    #output_layers = [layers[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    output_layers = [layers[i-1] for i in net.getUnconnectedOutLayers()]

    # Sınıf etiketlerini yükleme
    with open(classes_file, 'r') as f:
        classes = f.read().strip().split('\n')

    # Giriş görüntü boyutları
    input_width, input_height = 608, 608

    # Kameradan görüntü almak için url
    #url = "http://10.129.249.102:8080//shot.jpg"

    send_interval = 60  # Mail gönderme aralığı (saniye)
    last_email_sent_time = 0  # Son mail gönderme zamanı
    url = "http://10.251.29.198:8080//shot.jpg"
    while True:
        # Kameradan görüntüyü al
        img_resp = requests.get(url)
        img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
        img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
        img = cv2.resize(img, (640, 480))

        height, width = img.shape[:2]

        # Görüntüyü YOLOv4 için uygun boyuta getirme
        blob = cv2.dnn.blobFromImage(img, 1 / 255.0, (input_width, input_height), swapRB=True, crop=False)

        # YOLOv4 ile tespit yapma
        net.setInput(blob)
        outs = net.forward(output_layers)

        # Tespit sonuçlarını işleme
        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                if confidence > 0.5:  # Minimum güvenilirlik eşiği
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    # Dikdörtgen kutuyu tespitler listesine ekleme
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)                    

        # NMS (Non-Maximum Suppression) uygulama
        indices = cv2.dnn.NMSBoxes(boxes, confidences, score_threshold=0.5, nms_threshold=0.4)
        
        # Nesneleri tespit edilen kutuları çizme ve nesne adı ile benzerlik skorlarını yazdırma
        colors = np.random.uniform(0, 255, size=(len(classes), 3))
        for i in indices:
            #i = i[i]  # İndex'i düzeltilmiş haliyle kullan
            box = boxes[i]
            x, y, w, h = box
            class_id = class_ids[i]
            class_name = classes[class_id]
            confidence = confidences[i]

            color = colors[class_id]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)

            # Benzerlik skorunu yüzde olarak hesaplama ve çerçeve içine yazdırma
            confidence_percent = confidence * 100
            score_text = f"Score: {confidence_percent:.2f}%"
            label = f"{class_name} {score_text}"

            label_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 1)[0]
            cv2.rectangle(img, (x, y - label_size[1]), (x + label_size[0], y), color, -1)
            cv2.putText(img, label, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

            if confidence_percent>50:
                 # Plakayı veritabanına ve klasöre kaydet
                current_date = datetime.datetime.now().strftime("%Y-%m-%d")
                current_time = datetime.datetime.now().strftime("%H:%M")

                # Plakayı veritabanına kaydet
                _, img_encoded = cv2.imencode('.jpg', combined_img)
                plaka_gorseli = img_encoded.tobytes()
                veritabani_kayit (class_name, score_text, current_date, current_time, plaka_gorseli)

            if classes[class_id] == "Horse":
                at_detected = True  # At tespiti yapıldığını işaretle
                if at_detected:
                                    # E-posta mesajları ve kullanıcı bilgilerini alın
                            messages = Message.objects.all()

                            # E-posta gönderme işlemi
                            for m in messages:
                                try:
                                    # E-posta mesajı bilgileri
                                    subject = m.subject
                                    message = m.text
                                    sendTo = m.user.email  # Gönderen e-posta adresi
                                    #recipient_email = "busecetin587@gmail.com"  # Alıcı e-posta adresi

                                    # E-posta içeriği oluşturma
                                    content = "Subject: {0}\n\n{1}".format(subject,message)
                

                                    # Hesap bilgileri
                                    myMailAdress = "buseetinn@gmail.com"  # E-posta hesabınızın adresi
                                    password = "zwgmhpyrfbtqnhlr"  # E-posta hesabınızın şifresi

                                    # SMTP sunucusuna bağlanma
                                    mail = SMTP("smtp.gmail.com", 587)# E-posta sunucusunun adresi ve portu

                                    mail.ehlo()
                                    #verileri şifreleme
                                    mail.starttls()
                                    #mail sunucusunda oturum açma
                                    mail.login(myMailAdress,password)
                                    #maili gönderme
                                    mail.sendmail(myMailAdress, sendTo, content.encode("utf-8"))
                                    print("Mail Gönderme İşlemi Başarılı!")
                                except Exception as e:
                                    print("Hata Oluştu!\n {0}".format(e)) 

                            #time.sleep(10) #10 saniye aralıklar ile mail gönderir
                            #time.sleep(10) #10 saniye aralıklar ile mail gönderir

                                    #root = tk.Tk()
                                   # root.withdraw()  # Pencereyi gizler
                                   # messagebox.showinfo("Dikkat", "At Arabası tespit edildi, dikkatli olmanızı öneririz!!!")
                                    #time.sleep(10) #10 saniye aralıklar ile mail gönderir
        # Görüntüyü yatay olarak ikiye bölme
        quarter_width = int(img.shape[1] / 2)
        left_half = img[:, :quarter_width]
        right_half = img[:, quarter_width:]

        # İki çıktıyı yanyana birleştirme
        combined_img = cv2.hconcat([left_half, right_half])

        # Video akışı işlemi
        ret, buffer = cv2.imencode('.jpg', combined_img)
        frame_bytes = buffer.tobytes()

        for frame in range(10, 20):
            yield f"Frame from part 2: {frame}"

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
        
#def video_feed(request):
    #frames_one = generate_frames()
    #frames_two = generate_framestwo()

    #combined_frames = chain(frames_one, frames_two)
    #return StreamingHttpResponse(combined_frames, content_type='multipart/x-mixed-replace; boundary=frame')


def index(request):
    # Kodunuzun içindeki değişkenleri tanımlayın
    send_interval = 60  # Mail gönderme aralığı (saniye)
    last_email_sent_time = 0  # Son mail gönderme zamanı
    send_email_hour = 21  # Saat 15:16 olarak ayarlandı
    send_email_minute = 56  # Dakika 16 olarak ayarlandı
    mail_sent_flag = False  # mail_sent_flag değişkenini tanımlayın

    messages = Message.objects.all()
    for m in messages:
        subject = m.subject
        message = m.text
        send_to = m.user.email

    current_time = datetime.datetime.now().time()

    # Belirli bir saat ve dakikaya gelindiğinde ve daha önce mail gönderilmediyse mail gönderme işlemi yap
    if current_time.hour == send_email_hour and current_time.minute == send_email_minute \
        and not mail_sent_flag and time.time() - last_email_sent_time > send_interval:
        # Kontrol etmek için bitiş saat, dakika ve saniyeyi ayarla
        end_hour = 21
        end_minute = 58
        end_second = 5

        # Şu anki saat, dakika ve saniye, bitiş saatinden önce mi kontrol et
        if current_time.hour < end_hour or (current_time.hour == end_hour and current_time.minute < end_minute) \
                or (current_time.hour == end_hour and current_time.minute == end_minute and current_time.second < end_second):
            send_email(subject, message, send_to)
            last_email_sent_time = time.time()
            mail_sent_flag = True

        
            
    info = About_Information.objects.all()
    tes = Testimonial.objects.all()
    inftwo = Information_two.objects.all()
    gal = Gallery.objects.all()
    ser = Services.objects.all()

    content = {
        "info": info,
        "tes": tes ,
        "inftwo": inftwo ,
        "gal": gal,
        "ser": ser
    }

    return render(request, 'index.html', content)


def login_request(request):

    if request.user.is_authenticated:  # Kullanıcı daha önceden giriş yaptıysa tekrar oturum açtıemak yerine direkt anasayfaya yönlendiriyor.
        return redirect("/")
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")  # HttpResponse döndürülmeli
        else:
            return render(request, "login.html", {
                "error": "Kullanıcı adı ya da parola yanlış"
            })
    else:
        return render(request, "login.html")
    
def logout_request(request):
    logout(request)
    return redirect("products")

def movies(request):
    return render(request, 'movies.html')

def exx(request):
    return render(request, 'exx.html')

def statistics(request):
    return render(request, 'statistics.html')

def platedenemeA(request):
    return render(request, 'ex.html')

def camera_birlestirme(video_feed):

    return render(video_feed, 'camera_birlestirme.html')

def choose(request):
    return render(request, 'choose.html')

def plate(request):
    pla=Plate.objects.all()

    content = {
        "pla": pla ,
    }
    return render(request, 'plate.html', content)

def list(request):
    if request.GET['q'] and request.GET['q'] is not None:
        q=request.GET['q']
        pla=Plate.objects.filter(plaka_numarasi__contains=q).order_by("-tarih")
        #pla=Plate.objects.filter(tarih__contains=q)
        #pla=Plate.objects.filter(saat__contains=q)
    else:
        return HttpResponseRedirect("/plate")
    content = {
        "pla": pla ,
    }
    
    return render(request, 'plate.html', content)


def blogs_by_category(request):
    context = {
        "plate": Plate.objects.filter(tarih="2023-11-25"),
    }
    return render(request, "plate.html", context)

def adminindex(request):
    return render(request, 'adminindex.html')

def about(request):
    info = Information.objects.all()
    tes = Testimonial.objects.all()
    team = Team_Members.objects.all()

    content = {
        "info": info ,
        "tes": tes ,
        "team": team
    }
    return render(request, 'about.html', content)

def gallery(request):
    gal = Gallery.objects.all()

    content = {
        "gal": gal
    }

    return render(request, 'gallery.html', content)

def communication(request):
    com = Communication.objects.all()

    content = {
        "com": com
    }

    return render(request, 'communication.html', content)

def camera(request):

    # YOLOv4 konfigürasyon dosyasının ve ağırlık dosyasının yolu
    config_path = 'C:/Users/BUSE/Desktop/TUBITAK_horse/Custom_yolo_model/YOLOV4/darknet/spot_yolov4.cfg'
    weights_path = "C:/Users/BUSE/Desktop/backup-20230810T100028Z-001/backup/spot_yolov4_best.weights"

    # Sınıf etiketlerinin olduğu dosyanın yolu
    classes_file = 'C:/Users/BUSE/Desktop/TUBITAK_horse/Custom_yolo_model/YOLOV4/darknet/horse_data/horse.names'
    # YOLOv4 modelini yükleme
    net = cv2.dnn.readNetFromDarknet(config_path, weights_path)

    # Modelin yapılandırmasını al
    layers = net.getLayerNames()
    output_layers = [layers[i-1] for i in net.getUnconnectedOutLayers()]

    # Sınıf etiketlerini yükleme
    with open(classes_file, 'r') as f:
        classes = f.read().strip().split('\n')

    # Giriş görüntü boyutları
    input_width, input_height = 608, 608

    # Kameradan görüntü almak için url
    url = "http://10.195.248.233:8080//shot.jpg"

    while True:
        # Kameradan görüntüyü al
        img_resp = requests.get(url)
        img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
        img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
        img = cv2.resize(img, (640, 480))

        height, width = img.shape[:2]

        # Görüntüyü YOLOv4 için uygun boyuta getirme
        blob = cv2.dnn.blobFromImage(img, 1 / 255.0, (input_width, input_height), swapRB=True, crop=False)

        # YOLOv4 ile tespit yapma
        net.setInput(blob)
        outs = net.forward(output_layers)

        # Tespit sonuçlarını işleme
        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                if confidence > 0.5:  # Minimum güvenilirlik eşiği
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    # Dikdörtgen kutuyu tespitler listesine ekleme
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

                    if classes[class_id] == "horse":
                     at_detected = True  # At tespiti yapıldığını işaretle
                     messages = Message.objects.all()

    # E-posta gönderme işlemi
                     for message in messages:
                         try:
                            # E-posta mesajı bilgileri
                             subject = "deneme"
                             email_text = "denem123"
                             sender_email = "buseetinn@gmail.com"  # Gönderen e-posta adresi
                             recipient_email = "busecetin587@gmail.com"  # Alıcı e-posta adresi

                            # E-posta içeriği oluşturma
                             content = "Subject: {0}\n\n{1}".format(subject, email_text)

                            # Hesap bilgileri
                             my_mail_address = "buseetinn@gmail.com"  # E-posta hesabınızın adresi
                             password = "zwgmhpyrfbtqnhlr"  # E-posta hesabınızın şifresi

                            # SMTP sunucusuna bağlanma
                             server = SMTP("smtp.example.com", 587)  # E-posta sunucusunun adresi ve portu

                             server.starttls()  # Verileri şifreleme
                             server.login(my_mail_address, password)  # E-posta sunucusunda oturum açma

                            # E-postayı gönderme
                             server.sendmail(my_mail_address, recipient_email, content.encode("utf-8"))
                             print("Mail Gönderme İşlemi Başarılı!")

                            # E-posta sunucusuyla bağlantıyı kapatma
                             server.quit()
                         except Exception as e:
                             print("Hata Oluştu!\n {0}".format(e))
                    else:
                     print("At algılanmadı, e-posta gönderilmedi.")
                                    
                    

        # NMS (Non-Maximum Suppression) uygulama
        indices = cv2.dnn.NMSBoxes(boxes, confidences, score_threshold=0.5, nms_threshold=0.4)

        at_detected = False  # At tespiti yapılıp yapılmadığını takip eden değişken

        # Nesneleri tespit edilen kutuları çizme ve nesne adı ile benzerlik skorlarını yazdırma
        colors = np.random.uniform(0, 255, size=(len(classes), 3))
        for i in indices:
            i = i[0]
            box = boxes[i]
            x, y, w, h = box
            class_id = class_ids[i]
            class_name = classes[class_id]
            confidence = confidences[i]

            color = colors[class_id]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)

            # Benzerlik skorunu yüzde olarak hesaplama ve çerçeve içine yazdırma
            confidence_percent = confidence * 100
            score_text = f"Score: {confidence_percent:.2f}%"
            label = f"{class_name} {score_text}"

            # Eğer at tespiti yapılırsa alt kısma metin yazdırma
            if(confidence_percent >50 ):
                cv2.putText(img, "At tespit edildi!", (10, 470), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)


            label_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 1)[0]
            cv2.rectangle(img, (x, y - label_size[1]), (x + label_size[0], y), color, -1)
            cv2.putText(img, label, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

            

        # Tespit edilen nesneleri içeren görüntüyü gösterme
        
        cv2.imshow('YOLOv4 Object Detection', img)
        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()

    return render(request, 'camera.html')

#from .models import Plaka

#def plaka_tespit_view(request):
    # Plaka tanıma işlemini gerçekleştirin ve sonucu muh_plaka değişkeninde saklayın
 #   muh_plaka = plakaKarakter()
#
 #   if muh_plaka:
  #      plaka_karakter = muh_plaka
   #     tespit_zamani = timezone.now()
    #    Plaka.objects.create(plaka_karakter=plaka_karakter, tespit_zamani=tespit_zamani)
     #   return HttpResponse("Plaka başarıyla kaydedildi.")
    #else:
    #    return HttpResponse("Plaka tespit edilemedi.")



def movie_details(request, slug):
    return render(request, 'movie-details.html', {
        "slug": slug
    })