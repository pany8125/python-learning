from PIL import Image
from PIL import ImageFilter

qq = Image.open("123.jpg")
black_white = qq.convert("L")
blur = qq.filter(ImageFilter.BLUR) # add a blur filter to a image
detail = qq.filter(ImageFilter.DETAIL)
edges = qq.filter(ImageFilter.FIND_EDGES)

# black_white.show()
# blur.show()
detail.show()
edges.show()