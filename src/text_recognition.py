author = 'Mivili Suganthan'

import pytesseract
from PIL import Image, ImageFilter, ImageDraw
import string
import os


def text_recognition(file: str) -> None:
    """Return image with boxes surrounding any recognized text (specifically the words) given the original photo.
    
    Preconditions: Ensure the path has double slashes ('\\') or an r before the quotes of the path
    
    >>> text_recognition("C:\\Users\\mivil\\Downloads\\textsegment\\sample1\\images")
    >>> text_recognition("C:\\Users\\mivil\\Downloads\\textsegment\\sample3")
    >>> text_recognition("C:\\Users\\mivil\\Downloads\\textsegment\\sample2\\test22\\Images")
    """
    #Iterating through folder to access image files
    for images in os.listdir(file):
        #Checking if images are png files
        if 'png' in images:
            # Loading and modifying image from unwanted noise
            path = file + '/' + images
            image = Image.open(path)
            cleaned = image.filter(ImageFilter.DETAIL).filter(ImageFilter.SHARPEN)
            # Using pytesseract to recognize text within the given image
            boxes = pytesseract.image_to_data(cleaned)
            things = [] # Enclosing data from the above line in a dictionary then into this list
            key_list = [] # List of the header of the output of the pytessract function
            count = 0
            # Arranges data from the pytesseract function in a way that it can be used (dictionaries stored in a list)
            for elements in boxes.splitlines():
                data = {}
                words = elements.strip().split('\t')
                count += 1
                if count == 1:
                    key_list += words
                if len(words) == 12 and count > 1:
                    for n in range(len(key_list)):
                        if key_list[n] == 'left' or key_list[n] == 'top' or key_list[n] == 'height' or key_list[n] == 'width':
                            data[key_list[n]] = int(words[n])
                    things.append(data)
            # Draws boxes around the recognized words within the image
            for attributes in things:
                top_left = (attributes['left'], attributes['top'])
                right = attributes['left'] + attributes['width']
                bottom = attributes['top'] + attributes['height']
                bottom_right = (right, bottom)
                draw = ImageDraw.Draw(image)
                draw.rectangle((top_left, bottom_right), outline='green')
            # Displays New Image
            image.show()
            image.close()
    return None


def ias(folder: str, language: str) -> None:
    """Return ias file of text and word position recognized in the png files. Files are placed within a folder named 'ias' which is created as a subdirectory of the the given folder. 
    
    Preconditions: Files cannot be multilangual (must only have one language present in all files), language parameter is the three letter code of the language present in all files (eg. eng, fra, rus)
    
    >>> ias("C:\\Users\\mivil\\Downloads\\sample_ias\\sample4", 'eng')
    >>> ias("C:\\Users\\mivil\\Downloads\\sample_ias\\sample4", 'fra')
    >>> ias("C:\\Users\\mivil\\Downloads\\sample_ias\\sample4", 'heb')
    """
    #Checking if the folder exists or not
    if not os.path.exists(folder + '/' + 'ias'):
        new_folder = os.mkdir(folder + '/' + 'ias')
    for images in os.listdir(folder): #Iterating through the images in a folder
        if 'png' in images:
            path = folder + '/' + images #Modifying the path and ensuring that it is read raw
            image = Image.open(path)
            #Using pytesseract to recognize text within the image
            boxes = pytesseract.image_to_data(image, lang=language)
            things = [] # Enclosing data from the above line in a dictionary then into this list
            key_list = [] # List of the header from the output of the pytessract function
            count = 0
            # Arranges data from the pytesseract function in a way that it can be used (dictionaries stored in a list)
            for elements in boxes.splitlines():
                data = {}
                words = elements.strip().split('\t')
                count += 1
                if count == 1:
                    key_list += words
                if len(words) == 12 and count > 1:
                    for n in range(len(key_list)):
                        data[key_list[n]] = words[n]
                    things.append(data)
            #Turning png files from folder into ias files
                file = images.replace('png', 'ias')
                path_two = folder + '/' + 'ias' + '/' + file
                file = open(path_two, "w", encoding='utf-8-sig')
                for x in things:
                    top = x['top']
                    left = x['left']
                    width = x['width']
                    height = x['height']
                    text = x['text']
                    file.write(top + '\t' + left + '\t' + width + '\t' + height + '\t' + text + '\n')
    return None





















