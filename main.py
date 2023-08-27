from pdfconverter import ImagesConverter


def main():
    print("Hello World!")
    ImagesConverter(main_file, txt_file, pdf_file).converter()


if __name__ == "__main__":
    main_file = "tstPdf.pdf"
    txt_file = "MYFILE.txt"
    pdf_file = "MYDATAFILE.pdf"
    main()
