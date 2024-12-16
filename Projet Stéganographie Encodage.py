from PIL import Image
import random

def hide_msg(msg,img):

    img_init = Image.open(str(img))
    L, H = img_init.size
    #print(L, H)
    #img_init.show()
    img_encode = Image.new("RGB", (L, H))

    message = []

    for el in msg:
        message.append(int(el))
    indice = 0

    for y in range(H):
        for x in range(L):
            pixel = img_init.getpixel((x, y))

            if indice >= len(message):
                img_encode.putpixel((x, y), pixel)
            else:
                if message[indice] == 0:
                    if pixel[0] % 2 != 0:
                        R = pixel[0] + 1
                        G = pixel[1]
                        B = pixel[2]
                        pixel_new = (R, G, B)
                        img_encode.putpixel((x, y), pixel_new)
                    else:
                        img_encode.putpixel((x, y), pixel)

                else:
                    if pixel[0] % 2 != 0:
                        img_encode.putpixel((x, y), pixel)

                    else:
                        R = pixel[0] + 1
                        G = pixel[1]
                        B = pixel[2]
                        pixel_new = (R, G, B)
                        img_encode.putpixel((x, y), pixel_new)

                indice += 1

    img_encode.save("Image_encode.png")

hide_msg("01110101", "Image.png")

