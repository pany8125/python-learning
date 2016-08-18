from PIL import Image

qq = Image.open("123.jpg")
print(qq.mode)
r, g, b = qq.split() # split pic to individual channels, represent by tuple
# print(r)
'''
r.show() # r mains red
g.show() # g mains green
b.show() # b mains blue
'''

new_img = Image.merge("RGB", (r, g, b)) # color channel in correct order
# new_img = Image.merge("RGB", (b, g, r)) # color channel in error order
# new_img.show()

fo = Image.open("fo.jpg")
r2, g2, b2 = fo.split()
new_img_2 = Image.merge("RGB", (r, g2, b))
# new_img_2.show() # size mismatch ... :(