def _fileIO_list(_fileName, data):
    f = open("/Users/gameplay/Desktop/rpiProject-PixelPicture/list/" + _fileName + ".txt", 'w')

    idata = "%s" % data

    replace1_data = idata.replace("[","")
    replace2_data = replace1_data.replace("]","")

    f.write(replace2_data)
    f.close()