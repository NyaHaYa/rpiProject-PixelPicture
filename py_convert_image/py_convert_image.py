from PIL import Image

def convert(_image_name, _convert_iamge_name):

    # Image dir
    dir_image = '../image/'
    dir_convert_image = '../converted_image/'

    #   Open Image
    im = Image.open(dir_image + _image_name).convert('RGB')

    #   Compress Image to 32*32 Size (Use Thunmbnail)
    size = (32, 32)
    im.thumbnail(size)

    #   Save Converted Image
    im.save(dir_convert_image + _convert_iamge_name)

    return _convert_iamge_name

