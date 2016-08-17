from PIL import Image

img = Image.open("123.jpg")
print(img.size)
print(img.format)

area = (100, 100, 200, 200)
cropped_img = img.crop(area)

img.show() #open image by your default application
cropped_img.show() #open cropped image

bg = Image.open('fo.jpg')

area = (0, 0, 338, 466)
bg.paste(img, area)
bg.show()