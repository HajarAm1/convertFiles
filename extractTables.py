# import codecs
# import unicodedata
# from arabic_reshaper import arabic_reshaper
# from bidi.algorithm import get_display
# from img2table.document import Image
# from pdf2image import convert_from_path
# from pytesseract import pytesseract
# from img2table.document import PDF
# from img2table.ocr import TesseractOCR
# import pandas as pd
#
#
# def tables_converter():
#     with open("tstPdf.pdf") as my_file:
#         pages = convert_from_path("tstPdf.pdf")
#         file = codecs.open("TABLES.txt", "w", encoding="utf-8")
#         # file = codecs.open("convertrdMergedFiles.txt", "w", encoding="utf-8")
#         path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#         pytesseract.tesseract_cmd = path_to_tesseract
#         for i in range(len(pages)):
#             pages[i].save(f'img{i}.jpeg', 'jpeg')
#             # Instantiation of the image
#             img = Image(src=f"img{i}.jpeg")
#         # Instantiation of the pdf
#         # Instantiation of the OCR, Tesseract, which requires prior installation
#         ocr = TesseractOCR(lang="ara")
#         # Table identification and extraction
#         pdf_tables = img.extract_tables(ocr=ocr)
#         # We can also create an excel file with the tables
#         img.to_xlsx('tables.xlsx', ocr=ocr)
#         excel_data = pd.read_excel('tables.xlsx')
#         # Read the values of the file in the dataframe
#         data = pd.DataFrame(excel_data)
#         # Print the content
#         # reshape text
#         # reshaped_text = arabic_reshaper.reshape(u"" + data)
#         # bidi_text = get_display(reshaped_text)
#         # unicodedata.normalize('NFC', reshaped_text)
#         file.writelines(data)
#         # fileData.writelines(table)
#         file.writelines("\n")
#         file.writelines("\n")
#         file.writelines("\n")
#         # print(u'' + data)
#         # print("The content of the file is:\n", data)
