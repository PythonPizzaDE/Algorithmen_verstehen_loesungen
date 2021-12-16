from PIL import Image, ImageChops

img1 = Image.open('1.png').convert('1')
img2 = Image.open('2.png').convert('1')

result = ImageChops.logical_xor(img1, img2)
result.save('3.png')

