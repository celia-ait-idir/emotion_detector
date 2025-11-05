import cv2
from fer import FER
import numpy as np

cam = cv2.VideoCapture(0)
detector = FER(mtcnn=True)

emojis = {
    "angry": "😠",
    "disgust": "🤢",
    "fear": "😨",
    "happy": "😄",
    "sad": "😢",
    "surprise": "😲",
    "neutral": "😐"
}

while True:
    ret, frame = cam.read()
    if not ret:
        break

    results = detector.detect_emotions(frame)

    for result in results:
        (x, y, w, h) = result["box"]
        emotions = result["emotions"]
        top_emotion = max(emotions, key=emotions.get)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, f"{top_emotion.upper()} {emojis.get(top_emotion, '')}",
                    (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow('Emotion Detector', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
