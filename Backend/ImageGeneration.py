from PIL import Image, ImageDraw, ImageFont

def generate_image(prompt):
    image = Image.new("RGB", (100, 100), color=(73, 109, 137))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    draw.text((10, 10), prompt, font=font)
    image.save("image.png")

if __name__ == "__main__":
    prompt = input("Enter the prompt for the image: ")
    generate_image(prompt)