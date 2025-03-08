import os
from PIL import Image
from easy_image_processor import to_grayscale, resize_image

def create_test_image(filename="test_input.jpg", size=(100, 100), color=(255, 0, 0)):
    img = Image.new("RGB", size, color)
    img.save(filename)

def test_to_grayscale():
    create_test_image()
    to_grayscale("test_input.jpg", "test_gray.jpg")
    assert os.path.exists("test_gray.jpg")

def test_resize_image():
    create_test_image()
    resize_image("test_input.jpg", "test_resized.jpg", (100, 100))
    assert os.path.exists("test_resized.jpg")

def teardown_module(_):
    for file in ["test_input.jpg", "test_gray.jpg", "test_resized.jpg"]:
        if os.path.exists(file):
            os.remove(file)