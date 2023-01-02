import cv2
import mediapipe as mp
import time

class FaceMeshDetector():
  
  def __init__(self, staticMode=False, maxFaces=2,refineLandmarks=True, minDetectionConfidence=0.5, minTrackConfidence=0.5):
    self.staticMode = staticMode
    self.maxFaces = maxFaces
    self.refineLandmarks = refineLandmarks
    self.minDetectionConfidence = minDetectionConfidence
    self.minTrackConfidence = minTrackConfidence

    self.mpDraw = mp.solutions.drawing_utils
    self.mpFaceMesh = mp.solutions.face_mesh
    self.faceMesh = self.mpFaceMesh.FaceMesh(self.staticMode, self.maxFaces, self.refineLandmarks,
                                        self.minDetectionConfidence, self.minTrackConfidence)
    self.drawSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=1)

  
  def findFaceMesh(self, img, draw= True ):
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = self.faceMesh.process(imgRGB)
    faces = []


    if results.multi_face_landmarks:
      for faceLandmarks in results.multi_face_landmarks:
        if draw:
          self.mpDraw.draw_landmarks(
            img, faceLandmarks, self.mpFaceMesh.FACEMESH_CONTOURS, self.drawSpec, self.drawSpec
          ) 

        face = []
        for id,landmark in enumerate(faceLandmarks.landmark):
          imageHeight, imageWidth, imageChannels = img.shape
          x, y = int(landmark.x * imageWidth), int(landmark.y * imageHeight)
          cv2.putText(img, str(id), (x,y), cv2.FONT_HERSHEY_PLAIN,
                  1, (0,255,0), 1 )
          face.append([x,y])

        faces.append(face)

    return img, faces

  

def main():
  cap = cv2.VideoCapture('resources/videos/video3.mp4')
  pTime = 0

  faceDetector = FaceMeshDetector(maxFaces=1)

  while(True):
    success, img = cap.read()
    img, faces = faceDetector.findFaceMesh(img)
    faceLandmarks = []

    if(faces):
      faceLandmarks = faces[0]
      
      noseCoordinates = faceLandmarks[1]
      chinCoordinates = faceLandmarks[152]

      cTime = time.time()
      fps = 1/(cTime-pTime)
      pTime = cTime

      cv2.putText(img, f'FPS: {int(fps)}', (20,70), cv2.FONT_HERSHEY_PLAIN,
                    3, (0,255,0), 3 )
      
      cv2.putText(img, f'NOS', (noseCoordinates[0], noseCoordinates[1]), cv2.FONT_HERSHEY_PLAIN,
                    2, (0,0,255), 3 )

      cv2.putText(img, f'BRODA', (chinCoordinates[0], chinCoordinates[1]) ,cv2.FONT_HERSHEY_PLAIN,
                    2, (0,0,255), 3 )

      cv2.line(img, noseCoordinates, chinCoordinates, (255, 0, 0), thickness=1)


    cv2.imshow("Video", img)
      
    cv2.waitKey(1)

if __name__ == "__main__":
  main()