## **Real-Time Theft Detection in Urban Surveillance: A YOLO-Based Deep Learning Approach**

## Abstract
The escalating concerns over urban security have led to the widespread deployment of camera surveillance systems. However, the reliance on human intervention limits their effectiveness and makes them vulnerable to security threats. To address this, we present an automated system for real-time theft detection using advanced YOLO (You Only Look Once) deep learning algorithms. Our study evaluates YOLOv4, YOLOv5, and
YOLOv8 for detecting suspicious activities in surveillance footage. Notably, YOLOv8 achieves high detection accuracies of 98% for vehicles with obscured license plates, 99% for those with visible plates, and 97%
for horse-drawn carriages. Through comparative analysis, we demonstrate the superiority of YOLO-based models in enhancing object detection capabilities for security applications. The proposed system facilitates
timely intervention in theft-related incidents and strengthens overall security protocols by generating detailed data logs. This research not only advances the application of deep learning in surveillance systems
but also provides a robust framework for enhancing the autonomy and operational efficiency of urban security infrastructure.

## Description
The code and datasets related to the paper "Real-Time Theft Detection in Urban Surveillance: A YOLO-Based Deep Learning Approach" have been made publicly available here. This work has been submitted for publication to The Signal, Image and Video Processing journal. You can find more details and track the paper's progress through the journal.


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
 **Clone the Repository:**

git clone https://github.com/Buse-cetin/urban-security-YOLO.git  
cd urban-security-YOLO



## Usage
- cd movieapp
- activate.bat
- python manage.py runserver

## 
This repository includes all the necessary resources to reproduce the results presented in the paper. Feel free to explore, contribute, and provide feedback.

## Contact
If you have any questions or feedback, please contact me:
E-posta: buseetinn@gmail.com

## Publication Info
The journal

