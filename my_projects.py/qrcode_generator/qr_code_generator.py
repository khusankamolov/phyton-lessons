# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 16:28:50 2025

@author: Surface
"""

import qrcode

data = input("Enter the text or URL: ").strip()
filename = input('Enter the filename: ').strip()
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color = 'white', back_color = 'black')
image.save(filename)
print(f'QR code saved as {filename}')
    
    