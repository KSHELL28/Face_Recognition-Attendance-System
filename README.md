# Face Recognition Attendance System

A Python-based real-time attendance system using face recognition powered by OpenCV and the `face_recognition` library.
This project detects and recognizes faces from a webcam feed and marks attendance by storing the names and timestamps in a CSV file.

---

## 📌 Features

- 📷 Real-time face detection via webcam
- 📁 Stores attendance logs in `Attendance.csv`
- 🖼 Automatically labels and draws bounding boxes

---

## 🛠 Requirements

Install the required packages using:

1. Download C environment and essential tools by Downloading Visual Studio:
  https://visualstudio.microsoft.com/downloads/ the community version
  After installing Visual Studio in the PC you need to install the following :
    ![Screenshot 2025-07-02 145628](https://github.com/user-attachments/assets/ca1702f3-58e1-4d8e-9c10-eeb520065003)

  
2. ```bash
    pip install -r requirements.txt
    ```


## 📁 Folder Structure

Face_Recognition-Attendance-System

- ImagesAttendance/        (Images of all people in the database)
- Attendance.csv           ( Generated attendance log)
- main.py     ( Main face recognition + attendance logic)
- requirements.txt
- README.md

## 🚀 How to Run

```bash
python main.py
```
To Quit the system press Q . 

## 🔧 Future Improvements

- Face mask detection for pandemic settings
- Add GUI interface (Tkinter / PyQT)

## 📽️ Reference
  This project is based on the YouTube tutorial by Murtuza's Workshop - Robotics and AI:
    https://www.youtube.com/watch?v=sz25xxF_AVE 

##  📜 License
  Feel free to modify and extend this project .
  

