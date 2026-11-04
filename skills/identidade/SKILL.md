---
name: identidade
description: "Trilha 1 do Guia Master 2027: identidade e posicionamento do infoprodutor. Aplica o Diagnóstico de Identidade (7 perguntas), a frase de posicionamento, a ideia controladora de McKee, os ativos distintivos (Sharp, Romaniuk) e o personagem atraente (Brunson), com Godin, Christensen, Dunford, Sinek e Neumeier. Use quando pedirem nicho, posicionamento, \"quem eu sirvo\", marca pessoal, bio, manifesto, diferencial, \"estou perdido no digital\", ou a parte 1 do plano 2027."
---

# IDENTIDADE

Base: `trilhas/1-identidade/README.md`.

## Fluxo
1. Rodar o **Diagnóstico de Identidade**: as 7 perguntas (pra quem, progresso, alternativas, o que só você tem, porquê, contra o quê, como querem se sentir). Perguntar só o que não dá para inferir.
2. Escrever a **frase de posicionamento** (3 versões) e testar: serve para um concorrente? Se sim, refazer.
3. Escrever a **ideia controladora** (valor + causa) e o **vilão** impessoal.
4. Definir os **5 ativos distintivos** e o **personagem** (história de fundo, parábolas, defeitos, polaridade).
5. Se pedido: bio, manifesto curto (90 s) e as 3 histórias de origem para conteúdo.

## Motores
`coreyhaines31/marketingskills` → `product-marketing`, `customer-research`, `competitor-profiling` (pesquisa e contexto). Reserva: `wondelai/skills`.

## Saída
Frase de posicionamento · ideia controladora · vilão · ativos · personagem · bio. Checagem dos 5 verbos.

Este repositório fica dois níveis acima da pasta real desta skill (resolver com `readlink -f`). Ler `MAPA.md` (o caminho e os 5 verbos), a trilha indicada abaixo e só a parte do `AUTORES.md` que for citar. Os motores estão em `registry.json` e o status de cada um em `VALIDACAO.md`: use o primário; se ele não estiver instalado ou tiver ressalva que pese no caso, use o reserva e diga por quê.

**Regras de todas as skills do Guia Master**
- Falar com o infoprodutor em português simples e direto. Entregar **decisão e peça pronta**, não aula.
- Nunca inventar número, depoimento, resultado ou escassez. Dado que falta: perguntar uma vez ou marcar `[CONFIRMAR]`.
- Não citar nomes de pessoas ou empresas do mercado brasileiro. Autores internacionais só os do `AUTORES.md`, com a obra.
- Todo texto final passa por `python3 scripts/copy_lint.py arquivo --peca anuncio|roteiro|livre` (nota ≥ 85, zero erro grave).
- Terminar com a checagem dos 5 verbos (PARAR, ENTENDER, SENTIR, LEMBRAR, AGIR + CONFIANÇA), uma linha cada.
