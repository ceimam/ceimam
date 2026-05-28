import shutil, os

fotos = "C:/Users/guilh/ceimam/fotos"

mapping = {
    "page1_img1_X5.jpg":  "amanda-danaga.jpg",
    "page2_img1_X9.jpg":  "daniel-robledo.jpg",
    "page2_img2_X10.jpg": "edgar-cunha.jpg",
    "page3_img1_X14.png": "jordeanes-araujo.png",
    "page4_img1_X17.png": "ligia-almeida.png",
    "page5_img1_X20.png": "niminon-pinheiro.png",
    "page5_img2_X21.png": "paride-bollettin.png",
    "page6_img1_X24.png": "robson-rodrigues.png",
    "page7_img1_X27.png": "solange-schiavetto.png",
    "page7_img2_X28.png": "wilson-garcia.png",
}

for src, dst in mapping.items():
    shutil.copy2(os.path.join(fotos, src), os.path.join(fotos, dst))
    print(f"  {src} → {dst}")

print("Done.")
