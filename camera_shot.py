#camera Shot
from PIL import Image
from picamera import PiCamera

def shot():
	
	camera = PiCamera()
	camera.start_preview()
	camera.capture('image.jpg')
	camera.stop_preview()
	camera.close()
	im = Image.open('image.jpg')
	im.show()
shot()
