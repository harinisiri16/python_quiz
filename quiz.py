# make_qr_drive.py
import qrcode
from PIL import Image

# Example: https://drive.google.com/file/d/1AbCdEFgHIjklMNOP/view?usp=sharing
# Extract the FILE_ID (between /d/ and /view)
DRIVE_FILE_ID = "PASTE_FILE_ID_HERE"

direct_link = f"https://drive.google.com/uc?export=download&id={DRIVE_FILE_ID}"

img = qrcode.make(direct_link)
img.save("quiz_qr_drive.png")
print("Saved quiz_qr_drive.png — scan it to open the Drive download link.")
try:
    Image.open("quiz_qr_drive.png").show()
except:
    pass
