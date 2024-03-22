import PyPDF2 as pdf

def chunk_pdf_by_pages(pdf_path, pages_per_chunk):
    pdf_reader = pdf.PdfReader(pdf_path)
    chunks = []
    current_chunk = []

    for page_num in range(len(pdf_reader.pages)):
        current_chunk.append(pdf_reader.pages[page_num])
        if (page_num + 1) % pages_per_chunk == 0:
            chunks.append(current_chunk)
            current_chunk = []

    if current_chunk:  
        chunks.append(current_chunk)

    return chunks

def extract_text_from_chunk(chunk):
    text = ""
    for page in chunk:
        text += page.extract_text()
    #print(text)
    return text

def extract_text_from_chunks(chunks):
    return [extract_text_from_chunk(chunk) for chunk in chunks]

def process_pdf(pdf_path, pages_per_chunk):
    pdf_chunks = chunk_pdf_by_pages(pdf_path, pages_per_chunk=pages_per_chunk) 

    for i, chunk in enumerate(pdf_chunks):
        writer = pdf.PdfWriter()
        for page in chunk:
            writer.add_page(page)
        with open(f"chunk_{i+1}.pdf", "wb") as f:
            writer.write(f)


    
    

    