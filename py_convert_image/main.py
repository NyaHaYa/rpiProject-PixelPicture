import py_convert_image
import py_getImage_info
import py_fileIO_list
import arduino

#   Get File Names
fileName = input('INPUT FILE NAME >> ')
convert_image_name = input('INPUT CONVERT IMAGE NAME >> ')

def start(_fileName, _convert_image_name):

    py_convert_image.convert(_fileName, _convert_image_name)

    return py_getImage_info.get_info(_convert_image_name)

list = py_fileIO_list._fileIO_list(fileName, start(fileName, convert_image_name))
print(list)

arduino.arduino_make_code(fileName, list)