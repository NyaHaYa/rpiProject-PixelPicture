from PIL import Image

#   Converted File Name
converted_file_name = 'converted_image/python.jpg'

# Save RGB Value in List
rgb = []

#   Dir Name
#dir_converted = '../convertImage/converted_image/'

#   Open Image
converted_image = Image.open(converted_file_name)
print(converted_image)

#   Print Image Size
print(converted_image.size)

#   Get Pixel Code & Save RGB(tuple) in List(1024)
cnt = 0
cnt1 = 0

for i in range(1, 33):
    for j in range(1, 33):
        rgb.append(list(converted_image.getpixel((i-1,j-1))))
#        print(rgb[cnt])


        if rgb[cnt][0] <= 31:
            rgb[cnt][0] = 0

        elif rgb[cnt][cnt1] >= 32 and rgb[cnt][0] <= 63:
            rgb[cnt][0] = 1

        elif rgb[cnt][0] >= 64 and rgb[cnt][0] <= 95:
            rgb[cnt][0] = 2

        elif rgb[cnt][0] >= 96 and rgb[cnt][0] <= 127:
            rgb[cnt][0] = 3

        elif rgb[cnt][0] >= 128 and rgb[cnt][0] <= 159:
            rgb[cnt][0] = 4

        elif rgb[cnt][0] >= 160 and rgb[cnt][0] <= 191:
            rgb[cnt][0] = 5

        elif rgb[cnt][0] >= 192 and rgb[cnt][0] <= 223:
            rgb[cnt][0] = 6

        elif rgb[cnt][0] >= 224 and rgb[cnt][0] <= 255:
            rgb[cnt][0] = 7


##############################################################
        if rgb[cnt][1] <= 31:
            rgb[cnt][1] = 0

        elif rgb[cnt][1] >= 32 and rgb[cnt][1] <= 63:
            rgb[cnt][1] = 1

        elif rgb[cnt][1] >= 64 and rgb[cnt][1] <= 95:
            rgb[cnt][1] = 2

        elif rgb[cnt][1] >= 96 and rgb[cnt][1] <= 127:
            rgb[cnt][1] = 3

        elif rgb[cnt][1] >= 128 and rgb[cnt][1] <= 159:
            rgb[cnt][1] = 4

        elif rgb[cnt][1] >= 160 and rgb[cnt][1] <= 191:
            rgb[cnt][1] = 5

        elif rgb[cnt][1] >= 192 and rgb[cnt][1] <= 223:
            rgb[cnt][1] = 6

        elif rgb[cnt][1] >= 224 and rgb[cnt][1] <= 255:
            rgb[cnt][1] = 7


##############################################################
        if rgb[cnt][2] <= 31:
            rgb[cnt][2] = 0

        elif rgb[cnt][2] >= 32 and rgb[cnt][2] <= 63:
            rgb[cnt][2] = 1

        elif rgb[cnt][2] >= 64 and rgb[cnt][2] <= 95:
            rgb[cnt][2] = 2

        elif rgb[cnt][2] >= 96 and rgb[cnt][2] <= 127:
            rgb[cnt][2] = 3

        elif rgb[cnt][2] >= 128 and rgb[cnt][2] <= 159:
            rgb[cnt][2] = 4

        elif rgb[cnt][2] >= 160 and rgb[cnt][2] <= 191:
            rgb[cnt][2] = 5

        elif rgb[cnt][2] >= 192 and rgb[cnt][2] <= 223:
            rgb[cnt][2] = 6

        elif rgb[cnt][2] >= 224 and rgb[cnt][2] <= 255:
            rgb[cnt][2] = 7


        print(rgb[cnt])

        cnt = cnt + 1

print(rgb[1023][0])