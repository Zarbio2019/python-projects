import cv2
import webbrowser

image = cv2.imread('qr.png')
detector = cv2.QRCodeDetector()

url, coords, pixels = detector.detectAndDecode(image)

print(url)
print(url, coords, pixels)
# url: ex: https://google.com
# coords: coordinates
# pixels: matrix of 0 and 255, 0 = black, 255 = white

webbrowser.open(url) # open url in browser
