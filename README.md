# OCR Project with Python

Этот проект использует pytesseract и Pillow для извлечения текста из изображений. Включает предварительную обработку изображений для повышения точности OCR.

## Как использовать

1. Установите зависимости:
pip install -r requirements.txt

2. Запустите скрипт:
python main.py

3. Введите путь к изображению, когда будет предложено.

## Структура

- `preprocessing.py` — функции обработки изображений
- `main.py` — запуск основной программы

## Зависимости

- pytesseract
- Pillow

## Примечание
Убедитесь, что у вас установлен Tesseract OCR: [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)
