import cv2
from tensorflow import keras 
from keras.preprocessing.image import img_to_array
import imutils
import cv2
from keras.models import load_model
import numpy as np
detection_model_path = 'haarcascade_files/haarcascade_frontalface_default.xml'
emotion_model_path = 'models/_mini_XCEPTION.102-0.66.hdf5'
face_detection = cv2.CascadeClassifier(detection_model_path)
emotion_classifier = load_model(emotion_model_path, compile=False)
EMOTIONS = ["angry" ,"disgust","scared", "happy", "sad", "surprised",
 "neutral"]
class VideoCamera(object):
    def __init__(self):
      self.video = cv2.VideoCapture(0)

    def __del__(self):
      self.video.release()

    def get_frame(self):
      ret, frame = self.video.read()
      frame = imutils.resize(frame,width=300)
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      faces = face_detection.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE) 
      frame = frame.copy()
      if len(faces) > 0:
          faces = sorted(faces, reverse=True,
          key=lambda x: (x[2] - x[0]) * (x[3] - x[1]))[0]
          (fX, fY, fW, fH) = faces
          roi = gray[fY:fY + fH, fX:fX + fW]
          roi = cv2.resize(roi, (64, 64))
          roi = roi.astype("float") / 255.0
          roi = img_to_array(roi)
          roi = np.expand_dims(roi, axis=0)
          preds = emotion_classifier.predict(roi)[0]
          emotion_probability = np.max(preds)
          label = EMOTIONS[preds.argmax()]

          for (i, (emotion, prob)) in enumerate(zip(EMOTIONS, preds)):
                    text = "{}: {:.2f}%".format(emotion, prob * 100)
                    w = int(prob * 300)
                    cv2.putText(frame, label, (fX, fY - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
                    cv2.rectangle(frame, (fX, fY), (fX + fW, fY + fH),
                                  (0, 0, 255), 2)

      ret, jpeg = cv2.imencode('.jpg', frame)
      return jpeg.tobytes()
