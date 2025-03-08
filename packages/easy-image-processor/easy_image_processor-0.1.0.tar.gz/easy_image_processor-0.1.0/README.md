# 📸 Easy Image Processor

A simple and efficient Python package for **image processing**, allowing you to convert images to grayscale and resize them easily.

## 🚀 Features

-   Convert images to **grayscale**
-   Resize images to a **custom dimension**
-   Lightweight and easy to use

## 📦 Installation

Install the package using pip:

```sh
pip install image-processor
```

Or, for local development:

```sh
pip install .
```

## 📜 Usage

### **Convert an image to grayscale**

```python
from image_processor.processor import to_grayscale

to_grayscale("input.jpg", "output_gray.jpg")
```

### **Resize an image**

```python
from image_processor.processor import resize_image

resize_image("input.jpg", "output_resized.jpg", (200, 200))
```

## 🛠 Dependencies

-   [Pillow](https://python-pillow.org/) - A powerful library for image processing.

## ✅ Running Tests

To ensure everything is working properly, run the tests using **pytest**:

```sh
pytest tests/
```

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🌟 Show Your Support

Give this project a ⭐ on GitHub if you find it useful!
