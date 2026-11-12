import cv2
import numpy as np
from typing import Optional, Tuple

class Camera:
    def __init__(self, camera_id: int, name: str, src_type: int, capture: Optional[cv2.VideoCapture] = None)->None:
        self.camera_id = camera_id
        self.name = name
        self.src_type = src_type
        self.capture = capture

    def open(self)->None: 
        self.capture = cv2.VideoCapture(self.camera_id, self.src_type)
        if not self.capture.isOpened():
            raise RuntimeError(f"Impossible to open the camera ID : {self.camera_id} and Name : {self.name} with this specified backhend.")

    def read(self)->Tuple[bool, np.ndarray]:
        if self.capture is None or not self.capture.isOpened():
            raise RuntimeError("The camera is not opened")
        
        ret, frame = self.capture.read()
        return ret, frame

    def release(self)->None:
        if self.capture is not None:
            self.capture.release()

