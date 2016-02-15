import numpy as np
import cv2

def findRectanglesandFilter(hulls):
	temp[:] = 0
	for cnt in hulls:
		area = cv2.contourArea(cnt)
		rect = cv2.minAreaRect(cnt)
		w,h = rect[1]
		ar = abs(w/float(h) - 1)
		if (w*h)/float(area) < 1.2 and ar<0.1:
			box = cv2.boxPoints(rect)
			box = np.int0(box)
			cv2.drawContours(temp,[box],0,255,-1)	
	ret,labels,stats,centroids = cv2.connectedComponentsWithStats(temp)
	print ret
	return temp

def findFace():
	while True:
		ret,img = cam.read()
		hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		val = hsv[:,:,2]
		regions = mser.detectRegions(val, None)
		hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]
		rHulls = findRectanglesandFilter(hulls)
		cv2.imshow('img', rHulls)
		if 0xFF & cv2.waitKey(5) == 27:
			break

if __name__ == '__main__':
	import sys
	try:
		video_src = int(sys.argv[1])
	except:
		video_src = 0
	print video_src
	cam = cv2.VideoCapture(video_src)
	_,temp = cam.read()
	temp = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
	mser = cv2.MSER_create(5,500,5000,.25,.1)
	findFace()
	cv2.destroyAllWindows()