import os
import tempfile
from PIL import Image, ImageChops, ImageEnhance

def perform_ela(image_path, quality=90):
    temp_filename = None
    try:
        with Image.open(image_path) as source:
            original = source.convert('RGB')
        with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as temp_file:
            temp_filename = temp_file.name
        original.save(temp_filename, 'JPEG', quality=quality)
        with Image.open(temp_filename) as compressed_file:
            compressed = compressed_file.convert('RGB')
        
        ela_image = ImageChops.difference(original, compressed)
        
        extrema = ela_image.getextrema()
        max_diff = max([ex[1] for ex in extrema])
        if max_diff == 0:
            max_diff = 1 
            
        scale = 255.0 / max_diff
        ela_image = ImageEnhance.Brightness(ela_image).enhance(scale)
        return ela_image

    except Exception as e:
        print(f"Error processing image: {e}")
        return
    finally:
        if temp_filename and os.path.exists(temp_filename):
            os.remove(temp_filename)