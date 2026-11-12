from src.camera import Camera
import cv2

WEBCAM_ID = 0
WEBCAM_NAME = "webcam"
WEBCAM_BACKEND = cv2.CAP_DSHOW

IPHONE_ID = 1
IPHONE_NAME = "iphone"
IPHONE_BACKEND = cv2.CAP_DSHOW

def main():
    webcam = Camera(WEBCAM_ID, WEBCAM_NAME, WEBCAM_BACKEND)
    iphone = Camera(IPHONE_ID, IPHONE_NAME, IPHONE_BACKEND)

    try:
        webcam.open()
        iphone.open()

        while True:
            ret_webcam, frame_webcam = webcam.read()
            ret_iphone, frame_iphone = iphone.read()

            if not ret_webcam:
                print("Erreur : Échec de la lecture de l'image de la webcam.")
                break
            if not ret_iphone:
                print("Erreur : Échec de la lecture de l'image de l'iphone.")
                break

            cv2.imshow(webcam.name, frame_webcam)
            cv2.imshow(iphone.name, frame_iphone)
        
            if cv2.waitKey(1) == ord('q'):
                break
    finally:
        webcam.release()
        iphone.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()