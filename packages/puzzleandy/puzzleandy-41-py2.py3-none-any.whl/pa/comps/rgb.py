from pa.misc.basic import get_comp,set_comp

def get_r(im):
	return get_comp(im,0)

def set_r(im,rp):
	return set_comp(im,0,rp)

def get_g(im):
	return get_comp(im,1)

def set_g(im,gp):
	return set_comp(im,1,gp)

def get_b(im):
	return get_comp(im,2)

def set_b(im,bp):
	return set_comp(im,2,bp)