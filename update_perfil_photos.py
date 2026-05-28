import os, re

REPO = "C:/Users/guilh/ceimam"

# slug -> foto filename (only those with photos)
photos = {
    "perfil-amanda-danaga":    "amanda-danaga.jpg",
    "perfil-daniel-robledo":   "daniel-robledo.jpg",
    "perfil-edgar-cunha":      "edgar-cunha.jpg",
    "perfil-jordeanes-araujo": "jordeanes-araujo.png",
    "perfil-ligia-almeida":    "ligia-almeida.png",
    "perfil-niminon-pinheiro": "niminon-pinheiro.png",
    "perfil-paride-bollettin": "paride-bollettin.png",
    "perfil-robson-rodrigues": "robson-rodrigues.png",
    "perfil-solange-schiavetto": "solange-schiavetto.png",
    "perfil-wilson-garcia":    "wilson-garcia.png",
}

PLACEHOLDER = '<div class="perfil-foto-placeholder"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" style="width:80px;height:80px;color:#aaa"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg></div>'

for slug, foto in photos.items():
    path = os.path.join(REPO, slug + ".html")
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    img_tag = f'<img class="perfil-foto" src="fotos/{foto}" alt="" />'
    new_html = html.replace(PLACEHOLDER, img_tag)

    if new_html != html:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_html)
        print(f"Updated: {slug}.html")
    else:
        print(f"No change: {slug}.html")

print("Done.")
