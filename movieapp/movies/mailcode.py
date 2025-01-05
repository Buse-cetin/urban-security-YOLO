from django.shortcuts import render
from .models import About_Information, Communication, Gallery, Information, Team_Members, Testimonial, Information_two, Services, Message, Ip
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
# Create your views here.

def index(request):
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

def statistics(request):
    return render(request, 'statistics.html')

def choose(request):
    return render(request, 'choose.html')

def plate(request):
    return render(request, 'plate.html')

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
    output_layers = [layers[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    # Sınıf etiketlerini yükleme
    with open(classes_file, 'r') as f:
        classes = f.read().strip().split('\n')

    # Giriş görüntü boyutları
    input_width, input_height = 608, 608

    # Kameradan görüntü almak için url
    url = "http://10.152.228.76:8080//shot.jpg"

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

            label_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)[0]
            cv2.rectangle(img, (x, y - label_size[1]), (x + label_size[0], y), color, -1)
            cv2.putText(img, label, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

            if(confidence_percent >50 ):
           # smtpx = Smmtp.objects.all()
            #for s in smtpx :
             messagex = Message.objects.all()
             for m in messagex :

                # usera = User.objects.all()
            # for s in usera :
                
                try:
                # Mail Mesaj Bilgisi 
                    subcjet = m.subject
                    message = m.text
                    sendTo = "busecetin587@gmail.com"
                    #sendTo = m.users.email
                
                
                # userd = User.objects.get()
                    #sendTo = [val for val in Message.objects.all() if val in userd.objects.all()]
                    content = "Subject: {0}\n\n{1}".format(subcjet,message)
                    

                    # Hesap Bilgileri 
                    myMailAdress = "buseetinn@gmail.com"
                    password = "zwgmhpyrfbtqnhlr"

                    # Kime Gönderilecek Bilgisi
                    #sendTo = m.users
                    #host, port
                    mail = SMTP("smtp.gmail.com", 587)
                    
                # mail = SMTP("smtp.gmail.com", 587)
                    #sunucuya bağlanma
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

             # Eğer at tespiti yapılırsa alt kısma metin yazdırma
            if at_detected:
              cv2.putText(img, "At tespit edildi!", (10, 470), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

        # Tespit edilen nesneleri içeren görüntüyü gösterme
        cv2.imshow('YOLOv4 Object Detection', img)
        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()

    return render(request, 'camera.html')


def movie_details(request, slug):
    return render(request, 'movie-details.html', {
        "slug": slug
    })