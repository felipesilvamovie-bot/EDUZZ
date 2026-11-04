---
name: operacao-2027
description: "Trilha 7 do Guia Master 2027: operação, métricas, retenção, comunidade, automação e o plano anual - plano em uma página (Harnish), pedras de 90 dias e painel semanal (Wickman, EOS), OKRs (Doerr), retenção e superfãs (McLaren, Pat Flynn, Kevin Kelly, Nir Eyal), automação com n8n + MCP e WhatsApp, time e revisão trimestral. Use quando pedirem \"monta meu plano 2027\", metas, OKR, métricas, painel, LTV, CAC, churn, reembolso, retenção de alunos, onboarding, comunidade, automação, contratação, ou a parte 6 do plano."
---

# OPERAÇÃO E PLANO 2027

Base: `trilhas/7-operacao-e-plano-2027/README.md` e `PLANO-2027.md`.

## Fluxo
1. **Números atuais**: preencher o painel (leads, CAC, conversão, ticket, LTV, reembolso, % com primeiro resultado). Sem dado: marcar `[CONFIRMAR]`, nunca estimar como se fosse real.
2. **Meta de 2027** (um número) e **no máximo 3 prioridades**, cada uma com um OKR (objetivo + 3–5 resultados mensuráveis).
3. **Pedras de 90 dias** para os 4 trimestres.
4. **Retenção**: desenhar a primeira vitória em 7 dias, o onboarding, os rituais e o pedido de indicação.
5. **Automação**: escolher **um** fluxo (o que mais consome tempo) e montá-lo com o n8n-mcp; estimar as horas economizadas.
6. **Lista do que parar de fazer** e a data da primeira revisão trimestral.

## Motores
`czlonkowski/n8n-mcp` (o Claude monta o fluxo no n8n), `enescingoz/awesome-n8n-templates` (consulta; licença a conferir), `coreyhaines31/marketingskills` → `analytics`, `churn-prevention`, `community-marketing`, `onboarding`, `referrals`.

## Saída
PLANO-2027.md preenchido · painel semanal · OKRs · desenho de retenção · fluxo de automação. Checagem dos 5 verbos.

Este repositório fica dois níveis acima da pasta real desta skill (resolver com `readlink -f`). Ler `MAPA.md` (o caminho e os 5 verbos), a trilha indicada abaixo e só a parte do `AUTORES.md` que for citar. Os motores estão em `registry.json` e o status de cada um em `VALIDACAO.md`: use o primário; se ele não estiver instalado ou tiver ressalva que pese no caso, use o reserva e diga por quê.

**Regras de todas as skills do Guia Master**
- Falar com o infoprodutor em português simples e direto. Entregar **decisão e peça pronta**, não aula.
- Nunca inventar número, depoimento, resultado ou escassez. Dado que falta: perguntar uma vez ou marcar `[CONFIRMAR]`.
- Não citar nomes de pessoas ou empresas do mercado brasileiro. Autores internacionais só os do `AUTORES.md`, com a obra.
- Todo texto final passa por `python3 scripts/copy_lint.py arquivo --peca anuncio|roteiro|livre` (nota ≥ 85, zero erro grave).
- Terminar com a checagem dos 5 verbos (PARAR, ENTENDER, SENTIR, LEMBRAR, AGIR + CONFIANÇA), uma linha cada.
