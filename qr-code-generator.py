import qrcode
from datetime import datetime

content = input("Enter the text or URL: ")


# Default
now = int(datetime.now().timestamp())
image_name = (f"qr_code_{now}.png")
img = qrcode.make(content)
type(img)  # qrcode.image.pil.PilImage
img.save(image_name)
