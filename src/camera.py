import cv2

def camera_lecture():
    # Open the default camera
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    i = 0

    while True:
        ret, frame = cam.read()

        if not ret:
                print("Erreur : Échec de la lecture de l'image.")
                break
        
        if i == 0:
            print(frame.shape)
            i += 1
        
        # Display the captured frame
        cv2.imshow('Camera', frame)

        # Press 'q' to exit the loop
        if cv2.waitKey(1) == ord('q'):
            break

    # Release the capture and writer objects
    cam.release()
    cv2.destroyAllWindows()

camera_lecture()