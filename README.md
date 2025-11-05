#  Real-Time Emotion Detector with Emojis (FER + OpenCV)

This project uses the **[FER library](https://github.com/justinshenk/fer)** and **OpenCV** to detect human emotions in real time through your webcam and display corresponding emojis for each detected emotion.



##  Features

- Real-time emotion recognition  
- Supports multiple emotions:  
  😠 Angry, 🤢 Disgust, 😨 Fear, 😄 Happy, 😢 Sad, 😲 Surprise, 😐 Neutral  

---

##  How It Works

1. The webcam feed is captured using **OpenCV**.  
2. The **FER** model analyzes each frame to detect faces and classify emotions.  
3. The most dominant emotion is extracted for each face.  
4. An emoji representing that emotion is drawn above the face in real time.  

---

## 🛠️ Requirements

Install dependencies:
```bash
pip install fer opencv-python numpy

