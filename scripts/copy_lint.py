#!/usr/bin/env python3
"""copy_lint: corretor de objetividade para copy em PT-BR (Guia Master 2027).

Aponta o que deixa um texto subjetivo, genérico, com cara de IA ou arriscado:
  - clichês e muletas de texto gerado por IA
  - adjetivos vazios que deveriam virar fato ou número
  - promessas proibidas (renda/cura/resultado garantido)
  - frases longas demais para vídeo
  - (com --peca anuncio|roteiro) falta de número, de "você" e de CTA

Uso:
  python3 scripts/copy_lint.py arquivo.txt [--peca anuncio|roteiro|livre] [--max-palavras 18]
  echo "texto" | python3 scripts/copy_lint.py - --peca anuncio
Saída: relatório + nota de 0 a 100. Código de saída 1 se houver erro grave (promessa proibida)
ou nota abaixo de 70.
"""
import argparse
import re
import sys
import unicodedata

def norm(s):
    return unicodedata.normalize("NFC", s.lower())

# Muletas e clichês típicos de texto de IA / de agência (PT-BR).
CLICHES = [
    "no cenário atual", "nos dias de hoje", "em um mundo onde", "num mundo onde", "cada vez mais",
    "mergulhar", "mergulhe", "mergulhando", "jornada", "desvendar", "desvende", "desbloquear",
    "desbloqueie", "potencializar", "potencialize", "alavancar", "alavanque", "elevar ao próximo nível",
    "próximo nível", "é importante ressaltar", "vale ressaltar", "vale destacar", "é fundamental",
    "em suma", "em resumo", "por fim, mas não menos importante", "não é apenas", "não se trata apenas",
    "mais do que um", "muito mais do que", "transformar sua vida", "transforme sua vida",
    "solução completa", "soluções inovadoras", "de forma eficiente", "de maneira eficaz",
    "experiência única", "no fim das contas", "sem sombra de dúvidas", "a chave para",
    "o segredo para o sucesso", "tapeçaria", "sinfonia", "navegar pelo", "no universo de",
    "prezado cliente", "temos o prazer", "venha conferir", "não perca essa oportunidade",
]

# Adjetivos/advérbios vazios: trocar por fato, número ou demonstração.
VAZIOS = [
    "incrível", "incríveis", "revolucionário", "revolucionária", "inovador", "inovadora",
    "inovadores", "extraordinário", "extraordinária", "excelente", "fantástico", "fantástica",
    "maravilhoso", "maravilhosa", "sensacional", "perfeito", "perfeita", "único no mercado",
    "melhor do mercado", "o melhor", "a melhor", "alta qualidade", "qualidade superior",
    "exclusivo", "exclusiva", "poderoso", "poderosa", "impressionante", "surpreendente",
    "muito", "extremamente", "totalmente", "realmente", "simplesmente",
]

# Promessas que a Meta, o CONAR ou o CDC barram, ou que são mentira na prática.
PROIBIDAS = [
    r"renda garantida", r"lucro garantido", r"resultado garantido", r"garantimos resultado",
    r"fique rico", r"enrique[çc]a", r"dinheiro f[áa]cil", r"sem esfor[çc]o nenhum", r"sem esfor[çc]o",
    r"cura (definitiva|garantida)", r"\bcura\b", r"emagre[çc]a \d+ ?kg em \d+ dias? garantid",
    r"100% garantido", r"100% eficaz", r"nunca mais", r"[úu]ltimas? vagas?(?! reais)",
    r"risco zero de", r"aprovado (pela|pelo) (anvisa|fda)",
]

CTA_VERBOS = [
    "clique", "clica", "toque", "toca", "chama", "chame", "compre", "compra", "garanta", "garante",
    "acesse", "acessa", "baixe", "baixa", "assista", "assiste", "comenta", "comente", "salva",
    "salve", "manda", "mande", "inscreva", "inscreve", "agende", "agenda", "peça", "pede",
    "link", "whatsapp", "zap", "cupom", "arrasta", "arraste", "liga", "ligue", "experimente",
    "teste", "cadastre", "entre",
]

def frases(texto):
    partes = re.split(r"(?<=[.!?…])\s+|\n+", texto)
    return [p.strip() for p in partes if p.strip()]

def achar(lista, texto_norm):
    hits = []
    for termo in lista:
        padrao = r"(?<![\wà-ú])" + re.escape(termo) + r"(?![\wà-ú])"
        n = len(re.findall(padrao, texto_norm))
        if n:
            hits.append((termo, n))
    return hits

def main():
    ap = argparse.ArgumentParser(description="Corretor de objetividade para copy PT-BR")
    ap.add_argument("arquivo", help="arquivo de texto ou - para stdin")
    ap.add_argument("--peca", choices=["anuncio", "roteiro", "livre"], default="livre")
    ap.add_argument("--max-palavras", type=int, default=18, help="limite de palavras por frase")
    a = ap.parse_args()

    texto = sys.stdin.read() if a.arquivo == "-" else open(a.arquivo, encoding="utf-8").read()
    t = norm(texto)
    nota = 100
    graves, avisos = [], []

    for padrao in PROIBIDAS:
        m = re.search(padrao, t)
        if m:
            graves.append(f"PROMESSA PROIBIDA/ARRISCADA: '{m.group(0)}' (Meta, CONAR ou CDC). Reescreva com prova e sem garantia de resultado.")
            nota -= 25

    for termo, n in achar(CLICHES, t):
        avisos.append(f"clichê de IA/agência: '{termo}' x{n}. Corte ou troque por algo concreto.")
        nota -= 4 * n

    vazios = achar(VAZIOS, t)
    for termo, n in vazios:
        avisos.append(f"adjetivo vazio: '{termo}' x{n}. Troque por fato, número ou demonstração.")
        nota -= 3 * n

    travessoes = texto.count("—")
    if travessoes > 2:
        avisos.append(f"travessão (—) x{travessoes}: marca típica de texto de IA. Use ponto ou vírgula.")
        nota -= 2 * (travessoes - 2)

    longas = [(i + 1, f) for i, f in enumerate(frases(texto)) if len(f.split()) > a.max_palavras]
    for i, f in longas:
        avisos.append(f"frase {i} longa ({len(f.split())} palavras > {a.max_palavras}): \"{f[:70]}...\"")
        nota -= 3

    if a.peca in ("anuncio", "roteiro"):
        if not re.search(r"\d", texto):
            avisos.append("nenhum número: especificidade vende. Ponha prazo, quantidade, preço ou resultado real.")
            nota -= 8
        if not re.search(r"(?<![\wà-ú])(você|vc|seu|sua|te)(?![\wà-ú])", t):
            avisos.append("não fala com a pessoa: use 'você'.")
            nota -= 6
        if not achar(CTA_VERBOS, t):
            avisos.append("sem CTA claro: diga exatamente o que fazer (clique, chama no WhatsApp, salva...).")
            nota -= 10

    nota = max(0, nota)
    print(f"NOTA DE OBJETIVIDADE: {nota}/100  (peça: {a.peca})")
    for g in graves:
        print("  [ERRO]  " + g)
    for w in avisos:
        print("  [AVISO] " + w)
    if not graves and not avisos:
        print("  Limpo: direto, concreto e sem muletas.")
    sys.exit(1 if graves or nota < 70 else 0)

if __name__ == "__main__":
    main()
