from PIL import Image

#   Converted File Name
converted_file_name = 'python.jpg'

#   Dir Name
#dir_converted = '../convertImage/converted_image/'

#   Open Image
converted_image = Image.open(converted_file_name)
print(converted_image)

#   Print Image Size
print(converted_image.size)

#   Get Pixel Code & Save RGB(tuple) in List(1024)
cnt = 0

for i in range(1, 33):
    for j in range(1, 33):
        print(converted_image.getpixel((i-1,j-1)))