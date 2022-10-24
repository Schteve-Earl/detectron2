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
    cam_color = cv2.VideoCapture(4)
    # cam_depth = cv2.VideoCapture(6)

    while True:
        ret, frame_color = cam_color.read()
        # ret, frame_depth = cam_depth.read()
        
        # Show the captured image
        cv2.imshow('WebCamColor', frame_color)
        # cv2.imshow('WebCamDepth', frame_depth)
        
        # wait for the key and come out of the loop
        if cv2.waitKey(1) == ord('q'):
            break
    cam_color.release()
    cv2.destroyAllWindows()
