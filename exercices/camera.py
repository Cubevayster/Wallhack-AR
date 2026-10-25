import cv2
from time import perf_counter, sleep

def camera_lecture():
    cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)

    image_counter = 0
    past_time = perf_counter()
    i_image_shape = 0

    while True:
        if cam.isOpened():
            ret, frame = cam.read()

            if not ret:
                    print("Erreur : Échec de la lecture de l'image.")
                    break
                    
            if i_image_shape == 0:
                print(frame.shape)
                i_image_shape += 1

            image_counter += 1

            current_time = perf_counter()
            elapsed_time = current_time - past_time

            if elapsed_time >= 1.0:
                fps = float(image_counter) / (current_time - past_time)
                past_time = current_time
                image_counter = 0
                print(fps)

            cv2.imshow('Camera', frame)

            if cv2.waitKey(1) == ord('q'):
                break
        else:
            print("Erreur : Impossible d'accéder à la caméra.")

    cam.release()
    cv2.destroyAllWindows()

camera_lecture()