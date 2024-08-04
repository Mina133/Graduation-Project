import cv2
import pytesseract

# initialize the camera
camera = cv2.VideoCapture(0)  # 0 is the ID of the default camera on the Raspberry Pi

# set the resolution of the camera
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# set up the OCR engine
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
tessdata_dir_config = '--tessdata-dir "/usr/share/tesseract-ocr/4.00/tessdata"'

# loop through frames from the camera
while True:
    # read a frame from the camera
    ret, frame = camera.read()

    # check if the frame was successfully read
    if not ret:
        break

    # convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # perform thresholding to enhance text
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # perform OCR on the thresholded image
    text = pytesseract.image_to_string(thresh, config=tessdata_dir_config)

    # display the frame and recognized text
    cv2.imshow("Frame", frame)
    cv2.imshow("Text", thresh)
    print(text)

    # wait for a key press
    key = cv2.waitKey(1) & 0xFF

    # if the 'q' key is pressed, break from the loop
    if key == ord("q"):
        break

# release the camera and close all windows
camera.release()
cv2.destroyAllWindows()
