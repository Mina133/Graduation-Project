import OCR as ocr
import Screen
import DB
import camera_shot

def scan():
	
	shot = camera_shot.shot()
	img = ocr.chooseImg()
	sure = ocr.cheack()
	if sure == 0:
		main()
	else:
		print(Screen.printOnScreen(img))
		DB.showData()
		return 0
	

scan()



