from PIL import Image, ImageDraw, ImageFont

def create_poster(text, output="media/images/poster.png", size=(3840, 2160)):
    img = Image.new("RGB", size, color=(20, 20, 20))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 120)
    except:
        font = ImageFont.load_default()

    draw.text((200, 900), text, fill=(255, 255, 255), font=font)
    img.save(output)
    return output
