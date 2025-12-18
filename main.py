from task.image import ImageHandler, ImageProcessor
import os

def main():
    image_path = input("Введите путь к изображению: ").strip()

    if not os.path.isfile(image_path):
        print("Указанный файл не существует. Проверьте путь и повторите попытку.")
        return

    # Работа с ImageHandler
    handler = ImageHandler(image_path)

    handler.rotate_45_degrees()

    jpg_path = image_path.replace(".png", "_converted.jpg").replace(".jpeg", "_converted.jpg")
    handler.convert_to_jpg(jpg_path)
    print(f"Изображение конвертировано в JPG: {jpg_path}")

    # Работа с ImageProcessor
    processor = ImageProcessor(handler.image)
    processor.apply_sharpen_filter()

    processor.add_border()

    final_path = jpg_path.replace("_converted.jpg", "_processed.jpg")
    processor.image.save(final_path)
    print(f"Обработанное изображение сохранено как: {final_path}")

    print("Обработка завершена успешно!")

if __name__ == "__main__":
    main()
