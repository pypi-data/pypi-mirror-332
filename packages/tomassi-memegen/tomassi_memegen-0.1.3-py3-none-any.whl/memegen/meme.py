from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import argparse

def create_meme(image_url, top_text, font_path="arial.ttf", font_size=50):
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))

    draw = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()

    img_width, img_height = img.size

    def add_text(text, y_offset):
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        padding = 10
        background_y_offset = y_offset - padding
        draw.rectangle(
            [(0), background_y_offset, (img_width), y_offset + text_height + padding],
            fill="white"
        )

        x = (img_width - text_width) / 2
        y = y_offset
        draw.text((x, y), text, font=font, fill="black")
        border_thickness = 5
        draw.rectangle(
            [(0), y_offset + text_height + padding, (img_width), y_offset + text_height + padding + border_thickness],
            fill="black"
        )

    add_text(top_text, 10)

    img.save("created_meme_with_border.jpg")

    return "created_meme_with_border.jpg"

def main():
    parser = argparse.ArgumentParser(description='Create a meme with text on an image')
    parser.add_argument('image_url', help='URL of the image to create meme from')
    parser.add_argument('text', help='Text to add to the image')
    parser.add_argument('--font', default='arial.ttf', help='Font to use (default: arial.ttf)')
    parser.add_argument('--size', type=int, default=50, help='Font size (default: 50)')
    
    args = parser.parse_args()
    
    output_file = create_meme(args.image_url, args.text, args.font, args.size)
    print(f"Meme created: {output_file}")

if __name__ == '__main__':
    main()
