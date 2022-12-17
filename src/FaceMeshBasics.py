import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture('resources/videos/video1.mp4')
pTime = 0

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=3)
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=1)

while(True):
  success, img = cap.read()
  imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  results = faceMesh.process(imgRGB)

  if results.multi_face_landmarks:
    for faceLandmarks in results.multi_face_landmarks:
      mpDraw.draw_landmarks(img, faceLandmarks, mpFaceMesh.FACEMESH_CONTOURS, drawSpec, drawSpec)
      
      for id,landmark in enumerate(faceLandmarks.landmark):
        imageHeight, imageWidth, imageChannels = img.shape
        x, y = int(landmark.x * imageWidth), int(landmark.y * imageHeight)
        print(id, x,y)

  cTime = time.time()
  fps = 1/(cTime-pTime)
  pTime = cTime

  cv2.putText(img, f'FPS: {int(fps)}', (20,70), cv2.FONT_HERSHEY_PLAIN,
              3, (0,255,0), 3 )

  cv2.imshow("Video", img)
  
  cv2.waitKey(1)