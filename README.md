## **Improving Urban Security through YOLO-Based Object Detection in Surveillance Systems**
In response to increasing security concerns, the use of camera surveillance systems has grown significantly. However, the reliance on human intervention within these systems limits their effectiveness and resilience to security threats. As a result, there is a growing need for automated mechanisms capable of detecting security anomalies, particularly through real-time video analytics. This study focuses on the detection and monitoring of theft by analyzing urban surveillance camera feeds using computer vision. Advanced deep learning architectures such as YOLOv4, YOLOv5 and YOLOv8 enable high levels of detection accuracy. For example, YOLOv8 achieves 98% detection accuracy for vehicles with hidden number plates, 99% for vehicles with visible number plates, and 97% for horse identification. By providing a comparative analysis of YOLO algorithms, this study contributes to the field of object detection in security applications. In addition, the system is designed to facilitate timely intervention in theft-related incidents and strengthen security protocols. This research advances the application of deep learning in surveillance and provides a robust framework for improving the efficiency and autonomy of urban security systems.

## Technologies Used

- Deep Learning Models: YOLOv4, YOLOv5, YOLOv8
- Web Framework: Django
- Image Processing: OpenCV
- Database: SQLite
- Communication: Email sending via SMTP protocol

## Features

- Image processing algorithms
- Object recognition and classification
- Machine learning integration
- User-friendly interface
- License Plate Recognition
- Live Video Analysis
- Automatic Warning System

## Requirements

- Python 3.x
- Required libraries:
- OpenCV
- NumPy
- Matplotlib
- scikit-learn
    
## Algorithms

Some of the basic algorithms used in this project are:

1. **Image Filtering**: Various filtering techniques (e.g. Gaussian filter) are used to reduce the noise of images.

2. **Object Recognition**: Deep learning-based models (e.g. YOLO, SSD) are used to recognize objects in images.

3. **Feature Extraction**: Algorithms such as SIFT or ORB are used to extract features from images.

4. **License Plate Recognition**: Special algorithms have been developed for automatic recognition of vehicle license plates. These algorithms detect license plates in images and save them to the database.

5. **Incident Detection**: Machine learning techniques are used to detect suspicious situations in live video streams. In this way, security breaches can be detected immediately and necessary precautions can be taken.  

## Experimental Results
- YOLOv4: 95% closed plate, 98% open plate, 96% horse carriages accuracy 
- YOLOv5: 100% closed plate, 99% open plate, 98% horse carriages accuracy 
- YOLOv8: 98% closed plate, 99% open plate, 97% horse carriages accuracy
- Result: YOLOv8 demonstrated the most balanced performance in terms of accuracy and speed.

## Usage Scenarios

- Factories and Construction Sites: Detection of suspicious vehicles and tracking of entry and exit
- City Security: Real-time analysis of theft attempts
- Email Notification: Instant notification of suspicious situations detected to authorities

## Installation

1. **Clone the Repository:**

git clone https://github.com/Buse-cetin/ComputerVisionn.git  
cd ComputerVisionn

2.**Install Required Libraries:**
pip install -r requirements.txt

## Usage
cd movieapp
activate.bat
python manage.py runserver

## Contact
If you have any questions or feedback, please contact me:
E-posta: buseetinn@gmail.com

##Publication Info
Posted in The Visual Computer journal

