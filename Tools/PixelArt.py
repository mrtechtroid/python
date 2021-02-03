# Github: Mr Techtroid
from PIL import Image
# image = Image.open(input("Image Name:"))
image = Image.open("python-logo.png")
w,h = image.size
aspratio = w/h
#Resizing Images
width = 100
height = 100
image = image.resize((width,int(height)))

# Conversion To Grey Scale
image = image.convert("L")
pixels = image.getdata()
chars = ["B","S","#","&","@","$","%","*","!",":","."]
newpixels = [chars[pixel//25] for pixel in pixels]
newpixels = ''.join(newpixels)
new_pixels_count = len(newpixels)
ascii_image = [newpixels[index:index + width] for index in range(0, new_pixels_count, width)]
ascii_image = "\n".join(ascii_image)
print(ascii_image)
