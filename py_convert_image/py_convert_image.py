from PIL import Image

# Image dir
dir_image = '../image/'
dir_convert_image = 'converted_image/'

#   Get File Names
fileName = input('INPUT FILE NAME >> ')
convert_image_name = input('INPUT CONVERT IMAGE NAME >> ')

#   Open Image
im = Image.open(dir_image + fileName)

#   Compress Image to 32*32 Size (Thumbnail)
size = (32, 32)
im.thumbnail(size)

#   Save Converted Image
im.save(dir_convert_image + convert_image_name)
