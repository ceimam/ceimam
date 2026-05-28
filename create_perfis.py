#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

REPO = r"C:/Users/guilh/ceimam"

NAV = """<nav class="nav" role="navigation" aria-label="Navegação principal">
  <div class="nav__inner">
    <a class="nav__logo" href="index.html" aria-label="CEIMAM — Página inicial">
      <img src="logo-header.png" alt="CEIMAM" />
    </a>
    <button class="nav__toggle" aria-label="Abrir menu" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
    <ul class="nav__links" role="list">
      <li><a class="nav__link" href="index.html">Início</a></li>
      <li><a class="nav__link" href="sobre.html">Sobre</a></li>
      <li><a class="nav__link" href="pesquisadores.html">Pesquisadores</a></li>
      <li><a class="nav__link" href="parceiros.html">Parceiros</a></li>
      <li><a class="nav__link" href="projetos.html">Projetos</a></li>
      <li><a class="nav__link" href="publicacoes.html">Publicações</a></li>
      <li><a class="nav__link" href="eventos.html">Eventos</a></li>
    </ul>
  </div>
</nav>"""

FOOTER = """<footer class="footer" role="contentinfo">
  <div class="footer__inner">
    <div class="footer__brand">
      <img src="logo-footer.png" alt="CEIMAM" />
      <p>Centro de Estudos Indígenas &ldquo;Miguel Angel Menéndez&rdquo;.<br />Faculdade de Ciências e Letras — UNESP Araraquara.</p>
    </div>
    <div>
      <p class="footer__heading">Institucional</p>
      <ul class="footer__links">
        <li><a href="sobre.html">Sobre o CEIMAM</a></li>
        <li><a href="pesquisadores.html">Pesquisadores</a></li>
        <li><a href="parceiros.html">Parceiros</a></li>
      </ul>
    </div>
    <div>
      <p class="footer__heading">Pesquisa</p>
      <ul class="footer__links">
        <li><a href="projetos.html">Projetos</a></li>
        <li><a href="publicacoes.html">Publicações</a></li>
        <li><a href="eventos.html">Eventos</a></li>
      </ul>
    </div>
    <div>
      <p class="footer__heading">Contato</p>
      <p style="font-size:.85rem; color:var(--text-muted); line-height:1.8;">Rodovia Araraquara–Jaú, Km 1<br />14800-901 — Araraquara/SP<br />(16) 3334-6218<br /><a href="mailto:ceimam.fclar@unesp.br" style="color:var(--accent);">ceimam.fclar@unesp.br</a></p>
      <ul class="footer__links" style="margin-top:.75rem;">
        <li><a href="https://www.youtube.com/@centrodeestudosindigenas8309" target="_blank">YouTube</a></li>
        <li><a href="https://www.instagram.com/ceimam.fclar" target="_blank">Instagram</a></li>
      </ul>
    </div>
  </div>
  <div class="footer__bottom">
    <span>&copy; CEIMAM — Universidade Estadual Paulista (UNESP)</span>
    <span>Araraquara, São Paulo, Brasil</span>
  </div>
</footer>"""

PLACEHOLDER_SVG = """<div class="perfil-foto-placeholder"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" style="width:80px;height:80px;color:#aaa"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg></div>"""

STYLE = """<style>
    .perfil-hero { display:flex; gap:2.5rem; align-items:flex-start; margin-bottom:2.5rem; flex-wrap:wrap; }
    .perfil-foto { width:220px; height:220px; object-fit:cover; border-radius:50%; flex-shrink:0; box-shadow:0 4px 20px rgba(0,0,0,.15); }
    .perfil-foto-placeholder { width:220px; height:220px; border-radius:50%; background:var(--surface); display:flex; align-items:center; justify-content:center; flex-shrink:0; }
    .perfil-info { flex:1; min-width:220px; }
    .perfil-role { font-size:.85rem; font-weight:600; text-transform:uppercase; letter-spacing:.08em; color:var(--accent); margin-bottom:.4rem; }
    .perfil-name { font-size:2rem; font-weight:700; color:var(--text); margin-bottom:.3rem; line-height:1.2; }
    .perfil-inst { color:var(--text-muted); font-size:1rem; margin-bottom:1.2rem; }
    .perfil-bio { font-size:1rem; line-height:1.8; color:var(--text); max-width:72ch; }
    .perfil-lattes { display:inline-flex; align-items:center; gap:.4rem; margin-top:1.5rem; padding:.55rem 1.2rem; background:var(--accent); color:#fff; border-radius:6px; font-size:.85rem; font-weight:600; text-decoration:none; transition:opacity .2s; }
    .perfil-lattes:hover { opacity:.85; }
    @media(max-width:600px){ .perfil-foto, .perfil-foto-placeholder{ width:160px; height:160px; } .perfil-name{ font-size:1.5rem; } }
  </style>"""

def make_page(name, role, inst, bio, lattes_id):
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{name} — CEIMAM</title>
  <meta name="description" content="Perfil de {name} — CEIMAM, Centro de Estudos Indígenas Miguel Angel Menéndez, UNESP Araraquara." />
  <link rel="icon" type="image/png" href="favicon.png" />
  <link rel="stylesheet" href="style.css" />
  {STYLE}
</head>
<body>

{NAV}

<header class="page-hero">
  <div class="page-hero__inner">
    <a class="back-link" href="pesquisadores.html">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/></svg>
      Pesquisadores
    </a>
    <span class="page-hero__label">Perfil</span>
    <h1 class="page-hero__title reveal">{name}</h1>
  </div>
</header>

<section class="section">
  <div class="section__inner">
    <div class="perfil-hero">
      {PLACEHOLDER_SVG}
      <div class="perfil-info">
        <p class="perfil-role">{role}</p>
        <h2 class="perfil-name">{name}</h2>
        <p class="perfil-inst">{inst}</p>
        <p class="perfil-bio">{bio}</p>
        <a class="perfil-lattes" href="http://lattes.cnpq.br/{lattes_id}" target="_blank">Currículo Lattes</a>
      </div>
    </div>
  </div>
</section>

{FOOTER}

<script src="main.js"></script>
</body>
</html>
"""

researchers = [
    {
        "slug": "perfil-amanda-danaga",
        "name": "Amanda Cristina Danaga",
        "role": "Pesquisadora Colaboradora",
        "inst": "Universidade Estadual de Mato Grosso do Sul (UEMS)",
        "lattes_id": "8230760897259077",
        "bio": "Doutora em Antropologia Social pela Universidade Federal de São Carlos (UFSCar), com pós-doutorado pela Universidade Federal de Santa Catarina (UFSC). É docente da Universidade Estadual de Mato Grosso do Sul (UEMS), com atuação na graduação e na pós-graduação, sendo professora permanente no Mestrado Profissional em Sociologia (PROFSOCIO/UEMS), no Programa de Pós-Graduação em Ciências Sociais da Universidade Estadual Paulista Júlio de Mesquita Filho (UNESP/Araraquara) e no Programa de Pós-Graduação em Antropologia da Universidade Federal da Grande Dourados (UFGD). Possui experiência em gestão acadêmica, tendo exercido os cargos de Pró-Reitora de Pesquisa, Pós-Graduação e Inovação e de Coordenadora do curso de Ciências Sociais. Coordena o Mundéu Laboratório de Antropologia, Etnografia e suas Variações (UEMS/CNPq) e integra o Centro de Ensino, Pesquisa e Extensão em Educação, Gênero, Raça e Etnia (CEPEGRE/UEMS) e o Centro de Ensino, Pesquisa e Extensão Rede de Saberes Indígenas (CEPERSI/UEMS). Atua na área de Antropologia, com ênfase em Etnologia Indígena, especialmente em Etnologia Guarani, com foco em narrativas, discursos, regimes de subjetivação, etnobiografias, gênero, bem como políticas e lideranças ameríndias."
    },
    {
        "slug": "perfil-daniel-robledo",
        "name": "Daniel dos Santos Robledo",
        "role": "Pesquisador Colaborador",
        "inst": "Universidade Estadual Paulista (UNESP) — Campus Araraquara",
        "lattes_id": "4596789099911809",
        "bio": "Bacharel e licenciado em Letras (Português e Inglês) pela Universidade Estadual Paulista Júlio de Mesquita Filho (UNESP). Bacharel em Desenho Industrial (UNESP). Mestre em Comunicação e Semiótica (PUC). Atualmente é doutorando no Programa de Pós-Graduação em Estudos Literários (PPGELI) da Faculdade de Ciências e Letras de Araraquara (FCLAr/UNESP), com tese focada no estudo de cosmogonias de populações indígenas da região do Alto Rio Negro. Áreas de interesse: Literaturas Indígenas, Literaturas de Língua Inglesa, Teoria Literária, História da Arte, Teoria da Comunicação, Semiótica."
    },
    {
        "slug": "perfil-edgar-cunha",
        "name": "Edgar Teodoro da Cunha",
        "role": "Pesquisador Colaborador",
        "inst": "Universidade Estadual Paulista (UNESP) — Campus Araraquara",
        "lattes_id": "6539261486388368",
        "bio": "Professor do Departamento de Ciências Sociais da UNESP (Campus Araraquara) e integrante do corpo permanente do Programa de Pós-Graduação em Ciências Sociais na mesma instituição. Possui mestrado (2000) e doutorado (2005) em Antropologia Social e Pós-Doutorado (2009–10) na Universidade de São Paulo. Em 2015 foi Visiting Scholar na University of Oxford e pesquisador visitante na Universidade de Barcelona em 2023. Atualmente coordena o NAIP — Núcleo de Antropologia da Imagem e Performance (UNESP) e é pesquisador associado do GRAVI — Grupo de Antropologia Visual e do NAPEDRA — Núcleo de Antropologia da Performance e do Drama (USP). É autor de <em>Índio Imaginado</em> (Alameda, 2016) e coautor de <em>Antropologia e Imagem</em> (Zahar, 2006). Dirigiu os documentários <em>Jean Rouch, subvertendo fronteiras</em> (2000), <em>Ritual da Vida</em> (2005) e <em>Mbaraká, a palavra que age</em> (2011). Tem experiência em Antropologia Visual, Performance, Etnologia e Teoria Antropológica."
    },
    {
        "slug": "perfil-graziele-accolini",
        "name": "Graziele Açolini",
        "role": "Pesquisadora Colaboradora",
        "inst": "Universidade Federal da Grande Dourados (UFGD)",
        "lattes_id": "4477794450477197",
        "bio": "Possui graduação em Ciências Sociais pela FCL/UNESP Araraquara (1993), mestrado em Ciências Sociais com área de concentração em Antropologia pela Pontifícia Universidade Católica (PUC-SP, 1996) e doutorado no Programa de Pós-Graduação em Sociologia na linha de pesquisa Cultura, Representações e Identidade pela FCLAr/UNESP Araraquara (2004). Atualmente é professora associada da FCH/Ciências Sociais da Universidade Federal da Grande Dourados (UFGD). Membro efetivo da ABA e da Fundação Araporã. Pesquisadora dos grupos CEIMAM (CNPq/UNESP) e Diversos (CNPq/UFGD). Possui experiência na área de Antropologia, com ênfase em Etnologia Indígena, atuando principalmente com os seguintes temas: sociedades indígenas, contatos interétnicos, cosmologias indígenas, xamanismos e religiões cristãs."
    },
    {
        "slug": "perfil-jordeanes-araujo",
        "name": "Jordeanes do Nascimento Araujo",
        "role": "Pesquisador Colaborador",
        "inst": "Universidade Federal do Amazonas (UFAM)",
        "lattes_id": "1730905579503048",
        "bio": "Doutorado em Ciências Sociais pela Universidade Estadual Paulista (UNESP, 2019). Mestrado em Sociedade e Cultura na Amazônia pela Universidade Federal do Amazonas (UFAM, 2010). Graduação em Ciências Sociais — Bacharelado e Licenciatura pela Universidade Federal do Amazonas (2007). Pesquisador do Projeto Nova Cartografia Social da Amazônia desde 2010. Coordenador do Núcleo de Estudos e Pesquisas Afro e Indígenas (NEABI/IEAA) e Vice-Líder do Grupo de Pesquisa Cultura e Ambiente no Contexto Amazônico (CNPq). Atualmente é Professor Adjunto IV da Universidade Federal do Amazonas, Campus de Humaitá, e professor do Programa de Mestrado em Ciências Ambientais (IEAA/Humaitá). Coordena o projeto Mapeamento de garimpos ilegais, desmatamentos e madeireiras ilegais em Terras Indígenas no Sul do Amazonas. Tem experiência em Antropologia Indígena, atuando principalmente nos seguintes temas: Amazônia, cultura, identidades, territorialidades e conflitos socioambientais."
    },
    {
        "slug": "perfil-ligia-almeida",
        "name": "Lígia Rodrigues de Almeida",
        "role": "Pesquisadora Colaboradora",
        "inst": "Universidade Estadual Paulista (UNESP) — Campus Araraquara",
        "lattes_id": "9263580065240516",
        "bio": "Doutora em Antropologia Social pela Universidade de São Paulo (USP), com bolsa da CAPES. Mestra em Antropologia Social pelo Programa de Pós-Graduação em Antropologia Social da Universidade Federal de São Carlos (PPGAS/UFSCar), com bolsa da FAPESP. Graduação em Ciências Sociais (licenciatura e bacharelado) pela Universidade Estadual Paulista Júlio de Mesquita Filho (UNESP/Araraquara). É pesquisadora colaboradora do Centro de Estudos Ameríndios (CEstA/USP), do Laboratório de Estudos de Populações Tradicionais e Etnologia (LEPTE/IFMA) e do Centro de Estudos Indígenas Miguel Angel Menéndez (CEIMAM/UNESP). Atua na área de Antropologia, com ênfase em etnologia indígena, cosmologias ameríndias e modos de saber, sobretudo com trabalhos voltados às famílias Tupi Guarani no Estado de São Paulo."
    },
    {
        "slug": "perfil-marilia-lourenco",
        "name": "Marília Sene de Lourenço",
        "role": "Pesquisadora Colaboradora",
        "inst": "Museu Nacional — Universidade Federal do Rio de Janeiro (MN-UFRJ)",
        "lattes_id": "2639771998853175",
        "bio": "Doutora em Antropologia Social pelo Museu Nacional da Universidade Federal do Rio de Janeiro (MN-UFRJ), mestre em Antropologia Social pela Universidade Federal de São Carlos (UFSCar) e licenciada e bacharel em Ciências Sociais pela Universidade Estadual Paulista (UNESP/Araraquara). Membro do Laboratório de Inovações Ameríndias (LInA), coordenado por Aparecida Vilaça. Desde 2007 desenvolve pesquisa entre os Kaingang, povo da família linguística jê, ramo meridional. Atua em processos de consulta livre, prévia e informada a povos indígenas e comunidades tradicionais no âmbito do licenciamento ambiental de empreendimentos de infraestrutura. Possui experiência em docência nos ensinos superior, médio, PROEJA e formação de professores. Suas pesquisas abrangem metafísicas ameríndias, parentesco, dualismo e ritual, e conversão ao cristianismo."
    },
    {
        "slug": "perfil-niminon-pinheiro",
        "name": "Niminon Suzel Pinheiro",
        "role": "Pesquisadora Colaboradora",
        "inst": "Centro Universitário de Rio Preto (UNIRP)",
        "lattes_id": "4548989655330560",
        "bio": "Graduada em História e Economia. Mestre em História e Movimentos Sociais (1992) e doutora em História e Sociedade (1999), ambos pela UNESP-Assis. Pós-doutora em Antropologia pela UNESP-Marília (2012). Professora no Centro Universitário de Rio Preto (UNIRP), onde coordena o programa \"Adote uma Aldeia\" (há 25 anos) e o Projeto Brasil Negro \"Aristides dos Santos\" (há 21 anos). Como pesquisadora voluntária, assessora o Museu Histórico e Pedagógico Índia Vanuíre e é membro da Fundação Araporã. Integra o Conselho Editorial da Revista Terra Indígena e da Coleção Museu de Antropologia e Arqueologia (MAnA/UFU). Como escritora, recebeu o Prêmio Nelson Seixas de literatura pelo livro <em>Os Óculos do Pajé</em>; em 2019 foi premiada na categoria audiovisuais pelo game <em>Tupi no Reino de Santa Cruz</em>. Atua como palestrante, professora e pesquisadora em História, Educação, Antropologia, História Indígena, Museologia e Arte."
    },
    {
        "slug": "perfil-paride-bollettin",
        "name": "Paride Bollettin",
        "role": "Pesquisador Colaborador",
        "inst": "Masaryk University (República Tcheca)",
        "lattes_id": "0155793037669041",
        "bio": "Possui graduação em Storia pela Università degli Studi di Padova (2005), mestrado em Scienze Antropologiche pela Università degli Studi di Perugia (2007), doutorado em Antropologia pela Università degli Studi di Siena (2011) e pós-doutorado em Antropologia na Universidade de São Paulo (2012–2014). Tem experiência como pesquisador e professor em diversas universidades na América do Sul, Europa e África. Atualmente é Assistant Professor na Masaryk University (República Tcheca), professor no Programa de Pós-Graduação em Ciências Sociais da Universidade Estadual Paulista (UNESP), Honorary Research Fellow na University of Durham (Reino Unido) e Diretor Científico do Museu Etnográfico do Centro Studi Americanistici (Itália)."
    },
    {
        "slug": "perfil-paulo-santilli",
        "name": "Paulo José Brando Santilli",
        "role": "Pesquisador Colaborador",
        "inst": "Universidade Estadual Paulista (UNESP) — Campus Araraquara",
        "lattes_id": "1828355386855191",
        "bio": "Graduado em Ciências Sociais pela Universidade Nacional de Brasília (1979), Mestre em Antropologia Social pela Universidade Estadual de Campinas (1989) e Doutor em Antropologia Social pela Universidade de São Paulo (1997). Realizou Postdoctoral Fellow junto ao Centre for Indigenous American Studies — Department of Social Anthropology da University of St. Andrews (2001). Livre-Docente em Antropologia Social e Cultural junto ao Departamento de Antropologia, Política e Filosofia da Universidade Estadual Paulista (2016). É Professor Sênior junto à Faculdade de Ciências e Letras de Araraquara da Universidade Estadual Paulista, atuante nas áreas de Teoria Antropológica, Etnologia Sul-Americana, Ambientalismo e Direitos Territoriais."
    },
    {
        "slug": "perfil-robson-rodrigues",
        "name": "Robson Antonio Rodrigues",
        "role": "Pesquisador Colaborador",
        "inst": "Fundação Araporã / Universidade Federal de Uberlândia (UFU)",
        "lattes_id": "0068480121184829",
        "bio": "Possui graduação em Ciências Sociais pela Universidade Estadual Paulista/FCLAr (1996), mestrado em Arqueologia pela Universidade de São Paulo (2001) e doutorado em Arqueologia pela Universidade de São Paulo (2007). Realizou pós-doutorado em Antropologia na FCL/UNESP (2011) e pós-doutorado em Antropologia no INCIS/UFU (2020). Atualmente é pesquisador da URUTY — Assessoria e Consultoria em Arqueologia, Educação e Cultura, pesquisador associado da Fundação Araporã e pesquisador do Museu de Antropologia e Arqueologia da Universidade Federal de Uberlândia (MAnA-UFU). Tem experiência na área de Arqueologia, com ênfase em Etnologia, atuando principalmente nos seguintes temas: arqueologia, etnoarqueologia, territórios e culturas indígenas."
    },
    {
        "slug": "perfil-silvia-carvalho",
        "name": "Sílvia Maria Schmuziger de Carvalho",
        "role": "Pesquisadora Colaboradora",
        "inst": "Universidade Estadual Paulista (UNESP) — Campus Araraquara",
        "lattes_id": "8221280631276020",
        "bio": "Possui graduação em Geografia e História pela Universidade de São Paulo (1955), especialização em Antropologia pela Universidade de São Paulo (1957), doutorado pela Universidade Estadual Paulista Júlio de Mesquita Filho (1974) e pós-doutorado pela Université de Franche-Comté (1981). Tem experiência na área de Antropologia, atuando principalmente nos seguintes temas: Mitologia, Teoria Antropológica e Relação Homem-Natureza."
    },
    {
        "slug": "perfil-solange-schiavetto",
        "name": "Solange Nunes de Oliveira Schiavetto",
        "role": "Pesquisadora Colaboradora",
        "inst": "Universidade do Estado de Minas Gerais (UEMG)",
        "lattes_id": "6684330455459541",
        "bio": "Possui graduação em Ciências Sociais pela Universidade Estadual Paulista Júlio de Mesquita Filho (UNESP/Araraquara, 1997), mestrado em História Social do Trabalho pelo IFCH/Unicamp (2002), doutorado em História Cultural pelo IFCH/Unicamp (2007) e pós-doutorado em História pelo IFCH/Unicamp (2014). Tem experiência nas áreas de Arqueologia, Antropologia, História Cultural e Educação, com ênfase em Arqueologia das populações indígenas e Antropologia Educacional, atuando principalmente nos seguintes temas: diversidade cultural, arqueologia indígena e educação patrimonial. Docente da Universidade do Estado de Minas Gerais (UEMG/Poços de Caldas) e integrante do Núcleo de Estudos e Pesquisas em Memória, Cultura e Educação (UEMG). É membro da Fundação Araporã, coordenadora do Comitê de Ética em Pesquisa da UEMG/Poços de Caldas e do Centro de Pesquisa e Extensão da UEMG/Poços de Caldas."
    },
    {
        "slug": "perfil-wilson-garcia",
        "name": "Wilson Galhego Garcia",
        "role": "Pesquisador Colaborador",
        "inst": "Faculdade de Odontologia de Araçatuba — UNESP (FOA-UNESP)",
        "lattes_id": "7844658853315755",
        "bio": "Mestrado em Linguística pela Universidade de São Paulo (1979) e doutorado em Ciências Sociais (Antropologia Social) pela Universidade de São Paulo (1985). Livre-docente e titular na FOA-UNESP. Pró-reitor de graduação da UNESP (2001–2004). Visiting Scholar e Visiting Professor na Faculty of Medicine da University of Toronto. Realizou estágios no Museu de Arqueologia e Etnologia da USP, no Royal Kew Gardens (Londres), na Ulm Universität e em Giessen (Alemanha). Atualmente é professor sênior de Ciências Humanas e Sociais da FOA-UNESP. Participou do Working Group on Indigenous Populations que elaborou a Declaração Universal dos Direitos dos Povos Indígenas (Genebra/ONU). Tem experiência em projetos de grande porte nas áreas de formação de professores, Atenção Primária à Saúde na África e no Brasil, Estratégia Saúde da Família e saúde bucal na primeira infância."
    },
]

for r in researchers:
    html = make_page(r["name"], r["role"], r["inst"], r["bio"], r["lattes_id"])
    path = os.path.join(REPO, r["slug"] + ".html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Created: {path}")

print("Done!")
