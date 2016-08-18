from PIL import Image

qq = Image.open("123.jpg")
square_qq = qq.resize((200, 200))
flip_qq = qq.transpose(Image.FLIP_TOP_BOTTOM)
spin_qq = qq.transpose(Image.ROTATE_90)

qq.show()
square_qq.show()
flip_qq.show()
spin_qq.show()