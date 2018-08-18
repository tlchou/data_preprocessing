from PIL import Image

import os


for filename in os.listdir('./data_dir'):
    img = Image.open('./data_dir/'+filename)
    img = img.convert("RGBA")
    # print('c:/image/png/'+filename)
    pixdata = img.load()


    for y in range(img.size[1]):
        for x in range(img.size[0]): #RGBA
            if pixdata[x,y][0]>10 and pixdata[x,y][1]>10 and pixdata[x,y][2]>10 and pixdata[x,y][3]>10:
                pixdata[x, y] = (0, 0, 0, 0)
    img.save("./result2/"+filename, "bmp")
