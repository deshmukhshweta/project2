#WAP to open a Image

from PIL import Image as im

ref = im.open(r"images\one.jpg")
ref.rotate(45).show()
