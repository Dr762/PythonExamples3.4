import PIL.ExifTags
import glob
import os
from PIL import Image

# images(used images from first examples,requires pillow lib)
pix = Image.open("1drachmi_1973.jpg")
print(pix)
pix.save("test.tiff")
print(pix.info.keys())
pix = Image.open("Common_face_of_one_euro_coin.jpg")
exif = pix._getexif()
print(exif.keys())

for k, v in pix._getexif().items():
    print(PIL.ExifTags.TAGS[k], v)

# resizing images and creating thumb copy
for filename in glob.glob("*.jpg"):
    name, ext = os.path.splitext(filename)
    if name.endswith("_thumb"):
        continue
    img = Image.open(filename)
    thumb = img.copy()
    w, h = img.size
    largest = max(w, h)
    w_n, h_n = w * 128 // largest, h * 128 // largest
    print("Resize", filename, "from", w, h, "to", w_n, h_n)
    thumb.thumbnail((w_n, h_n), PIL.Image.ANTIALIAS)  # resample PIL.Image.ANTIALIAS
    thumb.save(name + "_thumb" + ext)

# cropping images
pix = Image.open("DSC_0811.JPG")
print(pix.size)
w, h = pix.size
pix.crop(box=(w // 3, 0, 2 * 2 // 3, h // 3)).show()
pix.crop(box=(w // 3, h // 3, 2 * 2 // 3, h // 3)).show()
