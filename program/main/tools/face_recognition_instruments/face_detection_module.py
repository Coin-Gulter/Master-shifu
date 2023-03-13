import mediapipe as mp
import cv2 as cv
import time
import numpy as np



def recognition(Draw=True):                                                                          
    cap = cv.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)
    pTime = 0
    Fc_recog = face_recognition()
    while True:
        success, img = cap.read()
        img = cv.flip(img, 1)
        img, detection = Fc_recog.faceDetector(img)
        img_mesh, face_mesh = Fc_recog.faceMeshDetect(img)
        if len(detection) != 0:
            face = detection[0][1]
            start_point_w = abs(face[0])
            start_point_h = abs(face[1])
            end_point_w = start_point_w + face[2]
            end_point_h = start_point_h + face[3]
            img = img[start_point_h:end_point_h, start_point_w:end_point_w]
            dsize = (400, 400)
            img = cv.resize(img, dsize, interpolation = cv.INTER_AREA)
            print(detection)
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        if Draw:
            cv.putText(img, f'fps: {int(fps)}', (20, 70), cv.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2)
        cv.imshow('Image',img)
        cv.imshow('Image',img_mesh)
        cv.waitKey(1)

def cut_face(img, bbox, out_size=(400, 400)):
        if type(img) != np.ndarray:
            return 0
        if len(bbox) != 0:
            face = bbox[0][1]
            start_point_w = abs(face[0])
            start_point_h = abs(face[1])
            end_point_w = start_point_w + face[2]
            end_point_h = start_point_h + face[3]
            img = img[start_point_h:end_point_h, start_point_w:end_point_w]
            dsize = out_size
            img = cv.resize(img, dsize, interpolation = cv.INTER_AREA)
            return img
        else:
            return 0


class face_recognition():

    def __init__(self, model_selection=0, min_detect_con=0.9):
        self.model_selection = model_selection
        self.min_detect_con = min_detect_con

        self.mpFaceDetection = mp.solutions.face_detection
        self.mpFaceMesh = mp.solutions.face_mesh
        self.mpDrawStyle = mp.solutions.drawing_styles
        self.mpDraw = mp.solutions.drawing_utils
        self.faceDetect = self.mpFaceDetection.FaceDetection(model_selection=self.model_selection, min_detection_confidence=self.min_detect_con)

    def faceDetector(self, img, rectangle_color:tuple=(173, 181, 1)):
        try:
            imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        except:
            return 0, 0
        self.results = self.faceDetect.process(imgRGB)
        bboxs = []
        detection_score = 0
        if self.results.detections:
            for id, detection in enumerate(self.results.detections):
                bboxc = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape
                bbox = int(bboxc.xmin * iw), int(bboxc.ymin * ih), int(bboxc.width * iw), int(bboxc.height * ih)
                bboxs.append([id, bbox, detection.score])
                cv.rectangle(img, bbox, rectangle_color, 3)
                detection_score = detection.score[0]
                # cv.putText(img, f'{int(detection.score[0]*100)}%', (bbox[0], bbox[1]-20),
                #         cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)
        return img, bboxs, detection_score

    def faceMeshDetect(self, img):
        try:
            imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        except:
            return 0, 0
        drawing_spec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=1)
        with self.mpFaceMesh.FaceMesh(static_image_mode=True, max_num_faces=1, refine_landmarks=True, min_detection_confidence=0.5) as face_mesh:
            result = face_mesh.process(imgRGB)
            result_multi_face = result.multi_face_landmarks
            if result_multi_face:
                face_mesh = np.array([])
                for face in result_multi_face:
                    for landmark in face.landmark:
                        face_mesh = np.append(face_mesh, int(landmark.x * imgRGB.shape[1]))
                        face_mesh = np.append(face_mesh, int(landmark.y * imgRGB.shape[0]))
                    self.mpDraw.draw_landmarks(image=imgRGB, landmark_list=face,
                    connections=self.mpFaceMesh.FACEMESH_TESSELATION, landmark_drawing_spec=None, 
                    connection_drawing_spec=self.mpDrawStyle.get_default_face_mesh_tesselation_style())
                return imgRGB, face_mesh
            else:
                return False, False
                




if __name__ == "__main__":
    recognition()
