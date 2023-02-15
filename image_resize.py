from PIL import Image

image = Image.open('FP.png')

size = 32
new_image = image.resize((size, size))
new_image.save(f'FP_{size}.gif')