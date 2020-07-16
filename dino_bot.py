import cv2
from mss.linux import MSS as mss 
import time
import numpy as np
import imutils
import pyautogui as pg

#установите параметры mon подходящие вашему окну
mon = {'top': 250, 'left': 270, 'width': 50, 'height': 30}

def process_image(original_img):
	process_image = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
	process_image = cv2.Canny(process_image, threshold1=200, threshold2=300)
	return process_image

def screen_record():
	sct = mss()                   
	last_time = time.time()

	while (True):
		img = sct.grab(mon)
		# определение параметров mon подходящие вашему окну
		image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
		cv2.imshow("Screenshot", imutils.resize(image, width=600))
		ch = cv2.waitKey(0)
		#закрыть окно кнопка esc
		if ch == 27:
		    break
        
		print('время полета {} seconds'.format(time.time() - last_time))
		last_time = time.time()
		img = np.array(img)
		mean = np.mean(process_image(img))
		print(mean)

		if not mean == float(0):
		   	pg.press('up')

		if cv2.waitKey(25) & 0xFF == ord('q'):
		 	cv2.destroyAllWindows()
		 	break
	
	
screen_record()
