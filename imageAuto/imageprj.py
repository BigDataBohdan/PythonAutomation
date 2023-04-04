from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs'
pathOut = '/editedImg'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    
    #edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)
    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(0)
    factor = 2.5
    enchancer = ImageEnhance.Contrast(edit)
    edit = enchancer.enhance(factor)
    clean_name = os.path.splitext(filename)[0]
    
    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')
    
    