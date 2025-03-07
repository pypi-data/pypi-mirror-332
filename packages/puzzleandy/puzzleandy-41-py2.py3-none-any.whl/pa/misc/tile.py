import numpy as np

def tile_x(im,n):
	return np.tile(im,(1,n,1))

def tile_y(im,n):
	return np.tile(im,(n,1,1))