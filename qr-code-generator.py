import qrcode
from datetime import datetime

content = input("Enter the text or URL: ")

'''
# Default
now = int(datetime.now().timestamp())
image_name = (f"qr_code_{now}.png")
img = qrcode.make(content)
type(img)  # qrcode.image.pil.PilImage
img.save(image_name)
'''


# Customized
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(content)
qr.make() #qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white") #qr.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))

now = int(datetime.now().timestamp())
image_name = (f"qr_code_{now}.png")
img.save(image_name)
print("QR code generated successfully")