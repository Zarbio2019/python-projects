# Author: Zarbio Romulo

import qrcode

img = qrcode.make('https://google.com')
img.save('qr1.png')