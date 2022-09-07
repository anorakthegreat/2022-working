import numpy as np
import argparse
import cv2
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("apple.jpg")
args = vars(ap.parse_args())
# load the image
image = cv2.imread(args["image"])