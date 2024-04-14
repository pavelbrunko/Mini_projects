import pyqrcode

# String for qr-code
S = 'https://dizyme.aicidlab.itmo.ru/'

# QR-code creation
url = pyqrcode.create(S)

# Creating and saving PNG file 'myqr.png'
url.svg('dizyme.svg', scale=8)