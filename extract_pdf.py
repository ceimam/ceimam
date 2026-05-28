from pypdf import PdfReader
reader = PdfReader("C:/Users/guilh/Downloads/Documento sem título (2).pdf")
for i, p in enumerate(reader.pages):
    print(f"=== PAGE {i+1} ===")
    print(p.extract_text())
    print()
