from PyPDF2 import PdfWriter, PdfReader

from getpass import getpass
from pathlib import Path

def password_protect_pdf_file(pdf_file):
    """Защищает Pdf-файл паролем."""
    pdfwriter = PdfWriter()
    pdf = PdfReader(pdf_file)

    for page in range(len(pdf.pages)):
        pdfwriter.add_page(pdf.pages[page])
    
    password = getpass(prompt='Введите пароль: ')
    pdfwriter.encrypt(password)

    with open(f'protected_{pdf_file.stem}.pdf', 'wb') as file:
        pdfwriter.write(file)

    
if __name__ == '__main__':
    pdf_file = Path('test.pdf')
    password_protect_pdf_file(pdf_file)




    