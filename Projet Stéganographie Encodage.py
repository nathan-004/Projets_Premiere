#https://media.discordapp.net/attachments/1174065242918109185/1318144968606355477/images.png?ex=676141aa&is=675ff02a&hm=194fc3af33cb59983a3d0de66abbf0a3c92d050115de371dd65c5670c7b51f28&=&format=webp&quality=lossless

from PIL import Image


im_init = Image.open("M:/NSISteno/image.jpg")
image_encode =  Image.new("RGBA")


def txt_to_binaire(txt):
    for lettres in txt:
        print(ord(lettres))

txt_to_binaire("abcdefg")


