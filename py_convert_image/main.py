from PIL import Image
import py_convert_image
#import py_getImage_info
import time

#   Get File Names
fileName = input('INPUT FILE NAME >> ')
convert_image_name = input('INPUT CONVERT IMAGE NAME >> ')

py_convert_image.convert(fileName, convert_image_name)

#time.sleep(2)

#print(py_getImage_info.get_info(convert_image_name))