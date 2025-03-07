import cv2
import numpy as np
from pa.space.hsv import hsv_to_rgb

def gray_strip(n):
	im = np.linspace(0,1,n,dtype=np.float32)
	return im

def hue_strip(n):
	h = np.linspace(0,360,n,dtype=np.float32)
	s = v = np.full(n,1,np.float32)
	im = cv2.merge((h,s,v))
	im = hsv_to_rgb(im)
	return im