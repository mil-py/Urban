from PIL import Image, ImageDraw, ImageFont


def new_photo(file_name):
    im = Image.open(file_name)
    print(im.format, im.size, im.mode)
    w, h = im.size
    return im.resize((int(w / 2), int(h / 2)))


im1 = new_photo('mil24.jpg')
im2 = new_photo("python.png")

mask_im = Image.new("L", im2.size, 0)
draw = ImageDraw.Draw(mask_im)
draw.ellipse((10, 0, 330, 320), fill=255)
# mask_im.save('mask_circle.jpg', quality=95)

im1.paste(im2, (100, 100), mask_im)
font = ImageFont.truetype('Roboto-Black.ttf', size=88)
draw_text = ImageDraw.Draw(im1)
draw_text.text(
     (100, im1.size[1]-150),
    'НуНеКрасавчегЛи',
    # Добавляем шрифт к изображению
    font=font,
    fill='#ff0000')  #

# im1.save('fon_pillow_paste_mask_circle.jpg', quality=95)
im1.show()

im1.close()
im2.close()
mask_im.close()
