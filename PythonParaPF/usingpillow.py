from PIL import Image

image_path = 'D:\\Downloads\\coollogo_com-59081568.jpg'  
#Coloque aqui o caminho do seu arquivo de imagem jpg. Escolha uma imagem pequenininha para testar o seu programa...

img = Image.open(image_path)

width, height = img.size

im_info = lambda width, height : [[img.getpixel((x, y)) for y in range (height)] for x in range (width)]

modified_img_info = lambda funct, iminf : [[tuple (map (funct, iminf[x][y])) for y in range (len (iminf[x]))] for x in range (len (iminf))]

print (im_info (width, height))

m = modified_img_info (lambda x : x + 10, im_info (width, height))
print (m)

# Para atualizar o valor para a nova image, utilize image.putpixel((x, y), modified_pixel)
