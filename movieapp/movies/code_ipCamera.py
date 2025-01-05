import cv2
import numpy as np
import requests

# YOLOv4 konfigürasyonu ve ağırlık dosyasının yolu
config_path = 'path_to_your_config_file.cfg'
weights_path = 'path_to_your_weights_file.weights'

# Sınıf etiketlerinin olduğu dosyanın yolu
classes_file = 'path_to_your_classes_file.names'

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

# Kameradan görüntü almak için url'leri listesi
urls = ["http://10.101.154.200:8080//shot.jpg", "http://another_camera_ip:8080//shot.jpg"]

# Çoklu pencereler için pencere adlarını oluşturma
windows = ["Camera 1", "Camera 2"]  # Kamera adlarına göre güncelleyin

# Pencerelerin sayısı kadar YOLOv4 modeli oluşturma
nets = [cv2.dnn.readNetFromDarknet(config_path, weights_path) for _ in windows]

while True:
    for idx, url in enumerate(urls):
        # Kameradan görüntüyü al
        img_resp = requests.get(url)
        img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
        img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
        img = cv2.resize(img, (640, 480))

        height, width = img.shape[:2]

        # Görüntüyü YOLOv4 için uygun boyuta getirme
        blob = cv2.dnn.blobFromImage(img, 1 / 255.0, (input_width, input_height), swapRB=True, crop=False)

        # YOLOv4 ile tespit yapma
        nets[idx].setInput(blob)
        outs = nets[idx].forward(output_layers)

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

            # Çerçeve kutusunun altına çerçeve renginde bir alan çizme
            cv2.rectangle(img, (x, y + h - 25), (x + w, y + h), color, -1)
            # Benzerlik skorunu çerçeve renginden farklı bir renkte yazdırma
            cv2.putText(img, score_text, (x, y + h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        # Tespit edilen nesneleri içeren görüntüyü gösterme
        cv2.imshow(windows[idx], img)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
