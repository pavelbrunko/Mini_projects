import pyqrcode 
from pyqrcode import QRCode

# String for qr-code
S = 'https://vk.com/p.brnk'

# QR-code creation
url = pyqrcode.create(S)

# Creating and saving PNG file 'myqr.png'
url.svg('myqrcode.svg', scale=8)