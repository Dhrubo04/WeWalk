# Smart Walking Stick for Elderly 👨‍🦯 
A life-saving assistive device that detects falls, monitors vital signs like unconsciousness , and sends real-time alerts with GPS location to caregivers — all powered by ESP32 and smart sensors.

---

## 🔍 Overview

The **Smart Walking Stick** is a compact, affordable, and real-time health monitoring system designed especially for elderly individuals. It continuously monitors **unconsciousness** , **movement**, **falls**, **pulse rate**, **SpO₂**, and **location**, triggering alerts and sharing coordinates if abnormalities are detected.

---

🚀 Tech Stack
<p align="center"> <img src="https://upload.wikimedia.org/wikipedia/commons/1/18/ISO_C%2B%2B_Logo.svg" alt="Embedded C++" height="50"/> &nbsp;&nbsp;&nbsp; <img src="https://www.vectorlogo.zone/logos/python/python-horizontal.svg" alt="Python" height="50"/> &nbsp;&nbsp;&nbsp; <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Micropython-logo.svg/1200px-Micropython-logo.svg.png" alt="MicroPython" height="65"/> &nbsp;&nbsp;&nbsp; <img src="https://cdn.prod.website-files.com/657fc5d7afa77574fc1a1f61/663d9a02aa09856cc50d2040_tinyML.png" alt="Edge AI" height="65"/> &nbsp;&nbsp;&nbsp; <img src="https://www.vectorlogo.zone/logos/tensorflow/tensorflow-icon.svg" alt="TensorFlow" height="50"/> &nbsp;&nbsp;&nbsp; <img src="https://upload.wikimedia.org/wikipedia/commons/a/ae/Keras_logo.svg" alt="Keras" height="50"/> </p> 

---

## 📦 Features

✅ **Fall Detection** using MPU6050  
✅ **No-Movement Monitoring** to detect unconsciousness  
✅ **Pulse & SpO₂ Sensing** via MAX30102  
✅ **GPS Location Tracking** with Neo-6M  
✅ **Alert System** using buzzer and LED  
✅ **Emergency Notification** with live coordinates  
✅ **Low Power & Compact Design**

---

## 🧠 How It Works

- **MPU6050**: Detects falls or unusual motion
- **MAX30102**: Monitors pulse rate and SpO₂  
- **Neo-6M GPS**: Tracks live location  
- **ESP8266**: Controls the logic and communication  
- **LED + Buzzer**: Provides instant alerts locally

---

🛠️ Hardware Used

**Component	Description**
- ESP32 microcontroller
- MPU6050	3-axis Accelerometer + Gyroscope
- MAX30102	Pulse & SpO₂ sensor
- Neo-6M GPS Module for real-time tracking
- Laser Module	Laser emitter for obstacle awareness / direction indicator
- Buzzer + LED	Local alert and status indication
- Rechargeable Battery	Power source for portability and reuse

---

## 📁 Folder Structure

```
📂 SmartWalkingStick
├── 📄 README.md
├── 📁 DOCS/
│   ├── Circuit_Diagram.png      
│   └── Flowchart
│   └── .pdf   
├── 📁 DataSets/
│   └── Dhrubo.csv
│   └── Arya.csv
└── 📁 Data_Colection/
|    └── MPU.py
├── 📁 Model_Training/
│   └── ML.ipynb
├── 📁 Models/
│   └── .h5
│   └── .tflite
│   └── .h
├── 📁 Deployment/
│   └── .esp32_model.ino
```

---

## 🧪 Status

- ✅ Fall & No-Movement Detection  
- ✅ Pulse/SpO₂ alert trigger  
- ✅ LED/Buzzer functional  
- 🔄 GPS coordinate transmission in progress  
- 🔜 Integration with IoT dashboard / SMS / email alert

---

## 🤝 Contributors

- **Dhrubo Ghosh** — Embedded Systems, Machine Learning, Firmware, and System Logic  
- **Arya Das** — Machine Learning, Algorithms , Model Training

---
