def resizeimage():
    import os
    import glob

    from PIL import Image, ImageDraw, ImageFilter

    im = Image.open('capture.png')
    thumb_width = 200

    def crop_center(pil_img, crop_width, crop_height):
        img_width, img_height = pil_img.size
        return pil_img.crop(((img_width - crop_width) // 2,
                             (img_height - crop_height) // 2,
                             (img_width + crop_width) // 2,
                             (img_height + crop_height) // 2))

    im_thumb = crop_center(im, thumb_width, thumb_width)
    im_thumb.save('capture2.png', quality=95)
