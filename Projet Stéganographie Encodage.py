#https://media.discordapp.net/attachments/1174065242918109185/1318144968606355477/images.png?ex=676141aa&is=675ff02a&hm=194fc3af33cb59983a3d0de66abbf0a3c92d050115de371dd65c5670c7b51f28&=&format=webp&quality=lossless

from PIL import Image


im_init = Image.open("M:/NSISteno/image.jpg")
image_encode =  Image.new("RGBA")


def txt_to_binaire(txt):
    for lettres in txt:
        print(ord(lettres))

txt_to_binaire("abcdefg")




from PIL import Image
im_ada = Image.open("Ada_Lovelace.jpg") #On ouvre l'image que le professeur a déjà intégré à l'activité
L, H = im_ada.size

print(L,H)
im_ada.show()

im_encode =  Image.new("RGB",(L,H))

message = [0,1,1]
indice = 0

for y in range(H):	
    for x in range(L):
        pixel = im_ada.getpixel((x,y)) # ??? à compléter 
        
        if indice >= len(message):
            im_encode.putpixel((x,y),pixel)
        else :
        
            if message[indice] == 0:
                if pixel[0]%2 == 0:
                    None
                else:
                    R = pixel[0] + 1
                    G = pixel[1]
                    B = pixel[2]
                    pixel_prime = (R, G, B)

            elif message[indice] == 1:

                if pixel[0]%2 == 0:
                    R = pixel[0] + 1
                    G = pixel[1]
                    B = pixel[2]
                    pixel_prime = (R, G, B)

                else :
                    None

            indice +=1

im_encode.show()





from PIL import Image
im_ada = Image.open("Ada_Lovelace.jpg") #On ouvre l'image que le professeur a déjà intégré à l'activité
L, H = im_ada.size

print(L,H)
im_ada.show()

im_encode =  Image.new("RGB",(L,H))

message = [1,0,0]
indice = 0

for y in range(H):	# ??? à compléter
    for x in range(L):# ??? à compléter
        pixel = im_ada.getpixel((x,y)) # ??? à compléter 
        
        if indice >= len(message):
            im_ada.putpixel((x,y), pixel)
        else:
            if message[indice] % 2 == 0:
                if pixel[0]%2 == 0:
                    im_ada.putpixel((x,y), pixel)
                else:
                    R = pixel[0]+1
                    G = pixel[1]
                    B = pixel[2]
                    pixel_new = (R,G,B)
                    im_ada.putpixel((x,y), pixel_new)
            else:
                if pixel[0]%2 != 0:
                    im_ada.putpixel((x,y), pixel)
                else:
                    R = pixel[0]+1
                    G = pixel[1]
                    B = pixel[2]
                    pixel_new = (R,G,B)
                    im_ada.putpixel((x,y), pixel_new)
            indice +=1

im_ada.show()







from PIL import Image
im_ada = Image.open("Ada_Lovelace.jpg") #On ouvre l'image que le professeur a déjà intégré à l'activité
L, H = im_ada.size

print(L,H)
im_ada.show()

im_encode =  Image.new("RGB",(L,H))

message = [1,0,0]
indice = 0

for y in range(H):	# ??? à compléter
    for x in range(L):# ??? à compléter
        pixel = im_ada.getpixel((x,y)) # ??? à compléter 
        
        if indice >= len(message):
            im_ada.putpixel((x,y), pixel)
        else:
            if message[indice] % 2 == 0:
                if pixel[0]%2 == 0:
                    R = pixel[0]+1
                    G = pixel[1]
                    B = pixel[2]
                    pixel_new = (R,G,B)
                    im_ada.putpixel((x,y), pixel_new)

                else:
                    im_ada.putpixel((x,y), pixel)
            else:
                if pixel[0]%2 != 0:
                    im_ada.putpixel((x,y), pixel)

                else:
                    R = pixel[0]+1
                    G = pixel[1]
                    B = pixel[2]
                    pixel_new = (R,G,B)
                    im_ada.putpixel((x,y), pixel_new)

            indice +=1

im_ada.show()
