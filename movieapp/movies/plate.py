import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils
import easyocr
import datetime
import os
import sqlite3  
# Plakayi tespit ettiginizde bu fonksiyonu calistir
def plakayi_veritabanina_kaydet(plaka_numarasi, tarih, saat, plaka_gorseli):
    # Veritabanı bağlantısını oluştur
    database_path = "C:\\Users\\BUSE\\Documents\\GitHub\\TUBITAK\\GÖBK_django\\movieapp\\db.sqlite3"
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    #conn = sqlite3.connect('veritabani.db')
    #cursor = conn.cursor()

    # Veritabanı tablosu kontrolü veya oluşturulması
    cursor.execute('''CREATE TABLE IF NOT EXISTS movies_plate
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       plaka_numarasi TEXT,
                       tarih TEXT,
                       saat TEXT,
                       plaka_gorseli BLOB)''')

    # Plakayı veritabanına ekle
    cursor.execute("INSERT INTO movies_plate (plaka_numarasi, tarih, saat, plaka_gorseli) VALUES (?, ?, ?, ?)",
                   (plaka_numarasi, tarih, saat, plaka_gorseli))

    # Değişiklikleri kaydet ve bağlantıyı kapat
    conn.commit()
    conn.close()

    
video_url = "http://10.251.29.198:8080//shot.jpg"
counter=0
while (counter<1):
    counter=counter+1
    cap = cv2.VideoCapture(video_url)
    # Kameradan bir kare al
    ret, frame = cap.read()
    # G�r�nt�y� boyutland�r
    frame = cv2.resize(frame, (500, 500))

    #img = cv2.imread('image1.jpg')
    plt.title("Gorselin siyah beyaz formata getirilmesi")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
    plt.show()

    #islem resmi (ir_img)
        #G�r�lt�lerden daha fazla kurtulmak i�in medianBlur i�lemini iki kez yap�yoruz.
    plt.title("Blurlama islemi")
    ir_img = cv2.medianBlur(gray,5) #5x5
    ir_img = cv2.medianBlur(ir_img,5) #5x5
    plt.imshow(ir_img,cmap="gray")
    plt.show()

    plt.title("Kenarlik Olusturma islemi")
    bfilter = cv2.bilateralFilter(gray, 11, 17, 17) #Noise reduction
    edged = cv2.Canny(bfilter, 30, 200) #Edge detection
    plt.imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))
    plt.show()

        # np.ones((3,3),np.uint8) -->
    kenarlik = cv2.dilate(edged,np.ones((3,3),np.uint8),iterations=1) #geni�letme i�leminin ka� defa yap�laca��n� iterations parametresi ile belirtiriz.

    plt.imshow(kenarlik,cmap="gray")
    plt.title("Goruntununn Kenarlarini Genisletme")
    plt.show()

    th_img = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,2)

    plt.title("esiklenmis")
    plt.imshow(th_img,cmap="gray")
    plt.show()

    kernel = np.ones((3,3),np.uint8)
    th_img = cv2.morphologyEx(th_img,cv2.MORPH_OPEN,kernel,iterations=1)
    plt.title("Gurultu yok edilmis")
    plt.imshow(th_img,cmap="gray")
    plt.show()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
    bfilter = cv2.bilateralFilter(gray, 11, 17, 17) #Noise reduction
    edged = cv2.Canny(bfilter, 30, 200) #Edge detection
    plt.imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))


    keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(keypoints)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

    location = None
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 10, True)
        if len(approx) == 4:
            location = approx
            break

    location
    mask = np.zeros(gray.shape, np.uint8)
    new_image = cv2.drawContours(mask, [location], 0,255, -1)
    new_image = cv2.bitwise_and(frame, frame, mask=mask)
    plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
    plt.show()

    (x,y) = np.where(mask==255)
    (x1, y1) = (np.min(x), np.min(y))
    (x2, y2) = (np.max(x), np.max(y))
    cropped_image = gray[x1:x2+1, y1:y2+1]

    plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
    plt.show()
    

    reader = easyocr.Reader(['tr'])
    result = reader.readtext(cropped_image)
    result

    text = result[0][-2]
    font = cv2.FONT_HERSHEY_SIMPLEX
    res = cv2.putText(frame, text=text, org=(approx[0][0][0], approx[1][0][1]+60), fontFace=font, fontScale=1, color=(0,255,0), thickness=2, lineType=cv2.LINE_AA)
    res = cv2.rectangle(frame, tuple(approx[0][0]), tuple(approx[2][0]), (0,255,0),3)
    plt.imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))
    plt.show()
    

     # Plakayı veritabanına ve klasöre kaydet
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.datetime.now().strftime("%H:%M")

    # Görseli kaydet
    #kayit_klasoru = "C:\\Users\\BUSE\\Desktop\\deneme"
    kayit_klasoru = "C:\\Users\\BUSE\\Documents\\GitHub\\TUBITAK\\plate_image"
   
    # Görseli kaydedin
    image_filename = os.path.join(kayit_klasoru, f"plaka_{counter}.jpg")
    cv2.imwrite(image_filename, frame)

    print(f"Plaka görseli başarıyla kaydedildi: {image_filename}")

    # Plakayı veritabanına kaydet
    _, img_encoded = cv2.imencode('.jpg', frame)
    plaka_gorseli = img_encoded.tobytes()
    plakayi_veritabanina_kaydet(text, current_date, current_time, plaka_gorseli)

# Döngü bittiğinde kamera bağlantısını serbest bırak
cap.release()