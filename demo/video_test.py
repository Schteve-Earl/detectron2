# Copyright (c) Facebook, Inc. and its affiliates.
import argparse
import glob
import multiprocessing as mp
import numpy as np
import os
import tempfile
import time
import warnings
import cv2


if __name__ == "__main__":
    cam = cv2.VideoCapture(8)

    while True:
        ret, frame = cam.read()
        
        # Show the captured image
        cv2.imshow('WebCam', frame)
        
        # wait for the key and come out of the loop
        if cv2.waitKey(1) == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()
