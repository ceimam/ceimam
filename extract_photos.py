from pypdf import PdfReader
import os

reader = PdfReader("C:/Users/guilh/Downloads/Documento sem título (2).pdf")

out_dir = "C:/Users/guilh/ceimam/fotos"
os.makedirs(out_dir, exist_ok=True)

count = 0
for page_num, page in enumerate(reader.pages):
    for img_num, img in enumerate(page.images):
        name = f"page{page_num+1}_img{img_num+1}_{img.name}"
        path = os.path.join(out_dir, name)
        with open(path, "wb") as f:
            f.write(img.data)
        print(f"Saved: {name} ({len(img.data)} bytes)")
        count += 1

print(f"\nTotal: {count} images extracted")
