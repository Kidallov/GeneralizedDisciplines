import os
from PIL import Image

folder_path = 'images/'
for filename in os.listdir(folder_path):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        img = Image.open(os.path.join(folder_path, filename))
        # Сохраняем как PNG с оптимизацией
        img.save(os.path.join(folder_path, 'compressed_' + filename), 
                 optimize=True, compress_level=9)
