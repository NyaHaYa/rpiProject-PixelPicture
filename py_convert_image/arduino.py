def arduino_make_code(_fileName, _list):

    f = open("/home/pi/rpiProject-PixelPicture/ino/"+ _fileName + "/"  + _fileName + ".ino",'w')

    idata = """
#include <Adafruit_GFX.h>
#include <RGBmatrixPanel.h>
#define CLK 11
#define OE 9
#define LAT 10
#define A A0
#define B A1
#define C A2
#define D A3

uint8_t array1[3072]=
{
    %s
};
 
RGBmatrixPanel matrix(A, B, C, D, CLK, LAT, OE, false); 
void setup() {
matrix.begin();
}
void loop() {
int line = 0;
for(int i=0;i<32;i++){
    for(int j=0;j<32;j++){
    matrix.drawPixel(i, j, matrix.Color333(array1[line], array1[line+1], array1[line+2])); 
    line+=3;
    }
}
delay(500);
}""" % _list
    f.write(idata)
    print("Sucessfully Maked %s.ino file!!" % _fileName)
