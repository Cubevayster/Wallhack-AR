import cv2
from time import perf_counter, sleep

def dual_camera_lecture():
    webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    iphone = cv2.VideoCapture(1, cv2.CAP_DSHOW)

    image_counter = 0
    past_time = perf_counter()
    i_image_shape = 0
    if webcam.isOpened() and iphone.isOpened():
        while True:

                ret_webcam, frame_webcam = webcam.read()
                ret_iphone, frame_iphone = iphone.read()

                if not ret_webcam:
                    print("Erreur : Échec de la lecture de l'image de la webcam.")
                    break
                if not ret_iphone:
                    print("Erreur : Échec de la lecture de l'image de l'iphone.")
                    break
                        
                if i_image_shape == 0:
                    print("RESOLUTION WEBCAM : ",frame_webcam.shape)
                    print("RESOLUTION IPHONE : ",frame_iphone.shape)
                    i_image_shape += 1

                image_counter += 1

                current_time = perf_counter()
                elapsed_time = current_time - past_time

                if elapsed_time >= 1.0:
                    fps = float(image_counter) / (current_time - past_time)
                    past_time = current_time
                    image_counter = 0
                    print(fps)

                cv2.imshow('Camera WEBCAM', frame_webcam)
                cv2.imshow('Camera IPHONE', frame_iphone)

                if cv2.waitKey(1) == ord('q'):
                    break
    else:
        print("Erreur : Impossible d'accéder aux caméras.")

    iphone.release()
    webcam.release()
    cv2.destroyAllWindows()

dual_camera_lecture()