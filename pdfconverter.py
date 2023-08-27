import unicodedata
from img2table import document
from pdf2image.pdf2image import convert_from_path
import codecs
import arabic_reshaper
from bidi.algorithm import get_display
from PIL import Image
from pytesseract import pytesseract
from img2table.ocr import TesseractOCR
import pandas as pd


class ImagesConverter:
    def __init__(self, file_name, txt_file, pdf_file):
        self.file_name_to_be_converted = file_name
        self.txt_file = txt_file
        self.pdf_file = pdf_file
        self.pages = None

    def open_file_pdf(self):
        with open(self.file_name_to_be_converted) as my_file:
            self.pages = convert_from_path(self.file_name_to_be_converted)

    def converter(self):
        self.open_file_pdf()
        file_txt = codecs.open(self.txt_file, "w", encoding="utf-8")
        file_data_pdf = open(self.pdf_file, "w+b")
        path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        pytesseract.tesseract_cmd = path_to_tesseract

        for i in range(len(self.pages)):
            self.pages[i].save(f'img{i}.png', 'PNG')
            # Define path to tessaract.exe
            path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            # Point tessaract_cmd to tessaract.exe
            pytesseract.tesseract_cmd = path_to_tesseract
            # Open image with PIL
            image = Image.open(f'img{i}.png', 'r')
            # Extract ARABIC text from image
            text = pytesseract.image_to_string(image, lang='ara', config='.')
            table = pytesseract.image_to_pdf_or_hocr(image, lang='ara', config='', nice=0, extension='pdf')
            # extract tables from image, Instantiation of the image
            img = document.Image(src=f'img{i}.png')
            # Table identification
            img_tables = img.extract_tables()
            # Print Result of table identification
            print(img_tables)
            # reshape text
            reshaped_text = arabic_reshaper.reshape(u"" + text)
            bidi_text = get_display(reshaped_text)
            unicodedata.normalize('NFC', reshaped_text)
            file_txt.writelines(reshaped_text)
            file_txt.writelines("\n")
            file_txt.writelines("\n")
            file_txt.writelines("\n")

    def tables_converter(self):
        pass
        # ocr = TesseractOCR(lang="ara")
        # file = codecs.open("TABLES.txt", "w", encoding="utf-8")
        # # file = codecs.open("convertrdMergedFiles.txt", "w", encoding="utf-8")
        # path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        # pytesseract.tesseract_cmd = path_to_tesseract
        # for i in range(len(self.pages)):
        #         self.pages[i].save(f'img{i}.jpeg', 'jpeg')
        #         # Instantiation of the image
        #         img = Image(src=f"img{i}.jpeg")
        #  # Instantiation of the pdf
        # # Instantiation of the OCR, Tesseract, which requires prior installation
        #
        #  # Table identification and extraction
        # pdf_tables = img.extract_tables(ocr=ocr)
        # # We can also create an excel file with the tables
        # img.to_xlsx('tables.xlsx', ocr=ocr)
        # excel_data = pd.read_excel('tables.xlsx')
        # # Read the values of the file in the dataframe
        # data = pd.DataFrame(excel_data)
        # # Print the content, reshape text
        # # reshaped_text = arabic_reshaper.reshape(u"" + data)
        # # bidi_text = get_display(reshaped_text)
        # # unicodedata.normalize('NFC', reshaped_text)
        # file.writelines(data)
        # # fileData.writelines(table)
        # file.writelines("\n")
        # file.writelines("\n")
        # file.writelines("\n")
        #     # print(u'' + data)
        #     # print("The content of the file is:\n", data)
