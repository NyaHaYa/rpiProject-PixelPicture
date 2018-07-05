import py_convert_image
import py_getImage_info
import py_fileIO_list
import arduino
import os, sys

#   Get File Names
fileName = input('INPUT FILE NAME >> ')
convert_image_name = input('INPUT CONVERT IMAGE NAME >> ')

makedir = "mkdir /home/pi/rpiProject-PixelPicture/ino/%s" % fileName
os.system(makedir)

def start(_fileName, _convert_image_name):

    py_convert_image.convert(_fileName, _convert_image_name)

    return py_getImage_info.get_info(_convert_image_name)

list = py_fileIO_list._fileIO_list(fileName, start(fileName, convert_image_name))
print(list)

arduino.arduino_make_code(fileName, list)

os.system("/home/pi/arduino-1.8.5/arduino --board arduino:avr:mega:cpu=atmega2560 --port /dev/ttyACM0 --upload /home/pi/rpiProject-PixelPicture/ino/%s/%s.ino"%(fileName, fileName))

print("Successful UPLOAD!!")

os.system("rm -r /home/pi/rpiProject-PixelPicture/converted_image/%s /home/pi/rpiProject-PixelPicture/ino/%s /home/pi/rpiProject-PixelPicture/list/%s.txt"%(convert_image_name, fileName, fileName))
