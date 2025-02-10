from PyPDF2 import PdfReader, PdfWriter
import os

# Dictionary with chapter names and page ranges
chapters = {
    "Matemática Financeira": (3, 50),
    "Indicadores Financeiros": (53, 73),
    "Institucional B3": (75, 103),
    "Título de Renda Fixa": (105, 121),
    "Mercados de Capitais": (123, 178),
    "Mercado de Derivativos": (181, 280),
    "Fundos de Investimento": (282, 295),
    "Gestão de Riscos": (297, 340),
    "Tributação": (344, 377),
    "Regulamentação de Operações": (378, 428),
    "Liquidação Bovespa": (429, 517),
    "Regulamentação de Operações BMEF": (518, 550),
    "Liquidação de Derivativos": (551, 569)
}

def split_pdf(input_pdf_path, output_dir="./"):
    # Create main output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Open the PDF file
    pdf = PdfReader(input_pdf_path)
    
    # Process each chapter
    for idx, (chapter_name, (start_page, end_page)) in enumerate(chapters.items(), 1):
        # Create folder name with number prefix
        folder_name = f"{idx:02d}. {chapter_name}"
        chapter_dir = os.path.join(output_dir, folder_name)
        
        # Create chapter directory if it doesn't exist
        if not os.path.exists(chapter_dir):
            os.makedirs(chapter_dir)
        
        # Create a PDF writer object
        pdf_writer = PdfWriter()
        
        # Add pages for this chapter (subtract 1 from page numbers since PDF indexing starts at 0)
        for page_num in range(start_page - 1, end_page):
            pdf_writer.add_page(pdf.pages[page_num])
        
        # Create the output filename (without number prefix since folder has it)
        output_filename = f"{chapter_name}.pdf"
        output_path = os.path.join(chapter_dir, output_filename)
        
        # Save the chapter PDF
        with open(output_path, "wb") as output_file:
            pdf_writer.write(output_file)
        
        print(f"Created: {folder_name}/{output_filename}")

if __name__ == "__main__":
    # Replace with your PDF path
    input_pdf = "bmf-bovespa-apostila-pqo-v2-anterior-a-31-01-2017.pdf"
    split_pdf(input_pdf)
