from flask import Flask, Response, render_template
import cv2
import numpy as np
import requests

app = Flask(__name__)

# Kamerayı başlat
camera = cv2.VideoCapture("http://10.152.228.76:8080//shot.jpg")

# YOLOv4 konfigürasyon dosyasının ve ağırlık dosyasının yolu
config_path = 'C:/Users/BUSE/Desktop/TUBITAK_horse/Custom_yolo_model/YOLOV4/darknet/spot_yolov4.cfg'
weights_path = 'C:/Users/BUSE/Desktop/backup-20230810T100028Z-001/backup/spot_yolov4_best.weights'

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

def generate_frames():
    while True:
        ret, frame = camera.read()

        if not ret:
            break

        # Görüntüyü YOLOv4 için uygun boyuta getirme
        blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (input_width, input_height), swapRB=True, crop=False)

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
                    center_x = int(detection[0] * frame.shape[1])
                    center_y = int(detection[1] * frame.shape[0])
                    w = int(detection[2] * frame.shape[1])
                    h = int(detection[3] * frame.shape[0])

                    # Dikdörtgen kutuyu tespitler listesine ekleme
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        # Nesneleri tespit edilen kutuları çizme ve nesne adı ile benzerlik skorlarını yazdırma
        colors = np.random.uniform(0, 255, size=(len(classes), 3))
        for i in range(len(boxes)):
            x, y, w, h = boxes[i]
            class_id = class_ids[i]
            class_name = classes[class_id]
            confidence = confidences[i]

            color = colors[class_id]
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            label = f"{class_name} {confidence:.2f}"
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('camera.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
