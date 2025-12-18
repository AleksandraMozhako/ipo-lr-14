from task.image import ImageHandler, ImageProcessor
import os

def main():
    image_path = input("Введите путь к изображению: ").strip()

    if not os.path.isfile(image_path):
        print("Указанный файл не существует. Проверьте путь и повторите попытку.")
        return

    # Работа с ImageHandler
    handler = ImageHandler(image_path)
    print("Изображение загружено.")

    handler.rotate_45_degrees()
    print("Изображение повёрнуто на 45 градусов.")

    jpg_path = image_path.replace(".png", "_converted.jpg").replace(".jpeg", "_converted.jpg")
    handler.convert_to_jpg(jpg_path)
    print(f"Изображение конвертировано в JPG: {jpg_path}")

    # Работа с ImageProcessor
    processor = ImageProcessor(handler.image)
    processor.apply_sharpen_filter()
    print("Применён фильтр повышения резкости (SHARPEN).")

    processor.add_border()
    print("Добавлена рамка шириной 15 пикселей.")

    final_path = jpg_path.replace("_converted.jpg", "_processed.jpg")
    processor.image.save(final_path)
    print(f"Обработанное изображение сохранено как: {final_path}")

    print("Обработка завершена успешно!")

if __name__ == "__main__":
    main()
