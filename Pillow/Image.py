from PIL import Image

im = Image.open('123Capture.JPG')
print(im.format, im.mode, im.size)
res = im.transpose()
res.show()