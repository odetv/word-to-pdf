import os
from docx2pdf import convert

def convert_docx_folder_to_pdf(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".docx"):
            docx_file = os.path.join(input_folder, filename)
            pdf_file = os.path.join(output_folder, os.path.splitext(filename)[0] + '.pdf')
            convert(docx_file, pdf_file)
            print(f"Converted {filename} to PDF.")

# Contoh penggunaan
input_folder = 'doc'  # Ganti dengan path ke folder yang berisi file .docx Anda
output_folder = 'pdf'  # Folder output untuk menyimpan file PDF
convert_docx_folder_to_pdf(input_folder, output_folder)
