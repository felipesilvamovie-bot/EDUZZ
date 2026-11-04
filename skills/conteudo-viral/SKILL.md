---
name: conteudo-viral
description: "Trilha 3 do Guia Master 2027: conteúdo, ganchos virais, storytelling e audiência. Aplica embalagem primeiro e retenção (MrBeast), Hook Point (Brendan Kane), as 12 famílias de gancho, toda cena vira (McKee), o roteiro de consciência zero para viralizar fora da bolha, STEPPS (Berger), SUCCESs (Heath), o modelo de conteúdo pilar e o jab-jab-jab-right-hook (Gary Vaynerchuk) e séries com formato fixo. Use quando pedirem roteiro de Reels, TikTok, Shorts ou YouTube, ganchos, ideias de conteúdo, calendário, storytelling, \"como viralizar\", carrossel, série, ou a parte 3 do plano 2027."
---

# CONTEÚDO VIRAL

Base: `trilhas/3-conteudo-e-audiencia/README.md` e `templates/roteiro-conteudo.md`.

## Fluxo
1. **Nível de consciência** do público-alvo do conteúdo. Para consciência zero, usar o roteiro Reconhecer → Nomear → Revelar → Ponte, **sem falar do produto**.
2. **Embalagem primeiro**: título, capa e primeira frase. Se não dá vontade de clicar, refazer antes de roteirizar.
3. **5 ganchos de famílias diferentes** para cada peça (das 12 famílias).
4. **Roteiro** na tabela tempo | fala | texto na tela | imagem | som, com uma virada a cada 2–4 s ligada por "mas" e "por isso".
5. **Compartilhamento**: qual emoção de alta ativação e qual moeda social a peça entrega?
6. **Sistema**: peça pilar → cortes → carrosséis → comentários viram pauta. Propor série com nome e formato fixo.

## Motores
`Jakeschincariol/instagram-agent-skill` (26 fórmulas de gancho pontuadas), `Jakeschincariol/youtube-agent-skill` (21 fórmulas), `coreyhaines31/marketingskills` → `content-strategy`, `social`, `video`. Reserva: `AgriciDaniel/claude-youtube`.

## Saída
Roteiros prontos · 5 ganchos por peça · legenda do post · plano da série. Checagem dos 5 verbos.

Este repositório fica dois níveis acima da pasta real desta skill (resolver com `readlink -f`). Ler `MAPA.md` (o caminho e os 5 verbos), a trilha indicada abaixo e só a parte do `AUTORES.md` que for citar. Os motores estão em `registry.json` e o status de cada um em `VALIDACAO.md`: use o primário; se ele não estiver instalado ou tiver ressalva que pese no caso, use o reserva e diga por quê.

**Regras de todas as skills do Guia Master**
- Falar com o infoprodutor em português simples e direto. Entregar **decisão e peça pronta**, não aula.
- Nunca inventar número, depoimento, resultado ou escassez. Dado que falta: perguntar uma vez ou marcar `[CONFIRMAR]`.
- Não citar nomes de pessoas ou empresas do mercado brasileiro. Autores internacionais só os do `AUTORES.md`, com a obra.
- Todo texto final passa por `python3 scripts/copy_lint.py arquivo --peca anuncio|roteiro|livre` (nota ≥ 85, zero erro grave).
- Terminar com a checagem dos 5 verbos (PARAR, ENTENDER, SENTIR, LEMBRAR, AGIR + CONFIANÇA), uma linha cada.
