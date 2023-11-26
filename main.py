from PIL import Image
import math
import os.path


asciis = "$@B%8&W#*oahkbdpqwmZ00QLCJUYXz******:::::,......       :,\ "
asciiArray = list(asciis)
asciiLen = len(asciis)
Interval = asciiLen / 256
save_path = 'Desktop'

def AsciiConverter(imgInt):
    return asciiArray[math.floor(imgInt * Interval)]


ascii_output = open("Output.text", "w")

factor = int(input("How much would you like to scale your Image? (try 70) : "))
img = Image.open("haha.jpg")
img.thumbnail((factor, factor ))
img.save("Scaled.jpg")
img = Image.open("Scaled.jpg")

width, height = img.size
pix = img.load()

print(width, height)


for i in range(height):
    for j in range(width):
        r, g, b = pix[j, i]
        h = int(r / 3 + g / 3 + b / 3)
        pix[j, i] = (h, h, h)
        ascii_output.write(AsciiConverter(h))
    ascii_output.write('\n')
