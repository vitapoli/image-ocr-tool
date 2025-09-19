from PIL import Image, ImageEnhance, ImageFilter, ImageOps

def preprocess_image(image):
    # Преобразуем в градации серого
    gray = image.convert('L')
    
    # Увеличиваем контраст
    enhancer = ImageEnhance.Contrast(gray)
    enhanced = enhancer.enhance(3)
    
    # Увеличиваем резкость
    sharp = enhanced.filter(ImageFilter.SHARPEN)
    
    # Бинаризация для выделения текста
    threshold = 128
    binary = sharp.point(lambda p: p > threshold and 255)
    
    # Инвертируем изображение, если фон светлый, а текст тёмный
    inverted = ImageOps.invert(binary)
    
    # Можно дополнительно применять фильтры для устранения шума
    denoised = inverted.filter(ImageFilter.MedianFilter(size=3))
    
    return denoised
