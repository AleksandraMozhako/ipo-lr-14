from PIL import Image, ImageFilter, ImageOps

class ImageHandler:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = None
        self.load_image()

    def load_image(self):
        """Загружает изображение по указанному пути."""
        try:
            self.image = Image.open(self.image_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл не найден: {self.image_path}")
        except Exception as e:
            raise Exception(f"Ошибка при открытии изображения: {e}")

    def convert_to_jpg(self, output_path):
        """Конвертирует изображение в JPG и сохраняет по новому пути."""
        self.image.convert("RGB").save(output_path, "JPEG")
        return output_path

    def rotate_45_degrees(self):
        """Поворачивает изображение на 45 градусов."""
        self.image = self.image.rotate(45, expand=True)

class ImageProcessor:
    def __init__(self, image):
        self.image = image.copy()

    def apply_sharpen_filter(self):
        """Применяет фильтр повышения резкости (SHARPEN)."""
        self.image = self.image.filter(ImageFilter.SHARPEN)

    def add_border(self, border_width=15):
        """Добавляет рамку вокруг изображения."""
        self.image = ImageOps.expand(self.image, border=border_width, fill="black")
