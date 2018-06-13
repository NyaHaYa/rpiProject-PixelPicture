from PIL import Image

#   Converted File Name
converted_file_name = 'converted_image/python.jpg'

#   Dir Name
#dir_converted = '../convertImage/converted_image/'

#   Open Image
converted_image = Image.open(converted_file_name)
print(converted_image)

#   Print Image Size
print(converted_image.size)

#   Get Pixel Code
cnt = 0

for i in range(1, 33):
    for j in range(1, 33):
        cnt = cnt + 1
        print(cnt, ':', i, ',', j)
        print(converted_image.getpixel((i-1, j-1)))