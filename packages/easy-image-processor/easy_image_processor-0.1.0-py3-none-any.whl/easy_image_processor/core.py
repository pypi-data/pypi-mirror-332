from PIL import Image

def to_grayscale(input_path: str, output_path: str):
    """Convert an image to grayscale."""
    img = Image.open(input_path).convert('L')
    img.save(output_path)

def resize_image(input_path: str, output_path: str, size: tuple):
    """Resize an image to a given size"""
    img = Image.open(input_path)
    img_resized = img.resize(size)
    img_resized.save(output_path)