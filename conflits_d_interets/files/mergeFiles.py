from PIL import Image

def decode_shares(share1_path, share2_path, output_path):
    share1 = Image.open(share1_path).convert('1')
    share2 = Image.open(share2_path).convert('1')

    width, height = share1.size
    decoded_image = Image.new('1', (width, height), color=255)

    for x in range(width):
        for y in range(height):
            pixel_share1 = share1.getpixel((x, y))
            pixel_share2 = share2.getpixel((x, y))
            decoded_pixel = pixel_share1 ^ pixel_share2
            decoded_image.putpixel((x, y), decoded_pixel)

    decoded_image.save(output_path)
    
    result = Image.open(output_path)
    result.show()

if __name__ == "__main__":
    share1_path = "ouvremoi/lausiv.bmp"
    share2_path = "ouvremoi/yhpargotpyrc.bmp"
    output_path = "merge.bmp"
    decode_shares(share1_path, share2_path, output_path)
