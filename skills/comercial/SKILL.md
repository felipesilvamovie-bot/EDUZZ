---
name: comercial
description: "Trilha 5 do Guia Master 2027: comercial e vendas de ticket alto para infoproduto (mentoria, consultoria, grupo, evento) - máquina comercial com SDR e closer (Ross, Blount), qualificação, call de diagnóstico e fechamento (SPIN de Rackham, CLOSER de Hormozi, empatia tática de Chris Voss, Challenger Sale), as 6 objeções e suas raízes, e WhatsApp como canal de venda. Use quando pedirem roteiro de call, script de vendas, \"como fechar\", objeções, follow-up, cadência, time comercial, SDR, closer, venda pelo WhatsApp, ou a parte 4 do plano 2027."
---

# COMERCIAL

Base: `trilhas/5-comercial/README.md` e `templates/roteiro-call-de-vendas.md`.

## Fluxo
1. Desenhar a **máquina**: quem prospecta, quem fecha, quem entrega a primeira vitória, quem retém.
2. **Critérios de qualificação** (dor, desejo, decisor, dinheiro, prazo) e as perguntas do formulário de aplicação.
3. **Roteiro de call** nas 10 etapas, adaptado ao produto, com as perguntas exatas.
4. **Objeções** do público com a raiz e a resposta (perguntas calibradas, nunca pressão).
5. **Cadência** de follow-up (dia 0, 1, 3, 7, 14) com canal e mensagem de cada toque.
6. **Automação** do que é repetitivo (lembrete, confirmação, follow-up); a conversa de fechamento é humana.

## Motores
`coreyhaines31/marketingskills` → `sales-enablement`, `cold-email`, `prospecting`. `devlikeapro/waha` (API de WhatsApp) e `czlonkowski/n8n-mcp` para automação. `zubair-trabzada/ai-sales-team-claude` foi reprovado na validação: só como referência.

## Saída
Máquina comercial · formulário de aplicação · roteiro de call · tabela de objeções · cadência. Checagem dos 5 verbos.

Este repositório fica dois níveis acima da pasta real desta skill (resolver com `readlink -f`). Ler `MAPA.md` (o caminho e os 5 verbos), a trilha indicada abaixo e só a parte do `AUTORES.md` que for citar. Os motores estão em `registry.json` e o status de cada um em `VALIDACAO.md`: use o primário; se ele não estiver instalado ou tiver ressalva que pese no caso, use o reserva e diga por quê.

**Regras de todas as skills do Guia Master**
- Falar com o infoprodutor em português simples e direto. Entregar **decisão e peça pronta**, não aula.
- Nunca inventar número, depoimento, resultado ou escassez. Dado que falta: perguntar uma vez ou marcar `[CONFIRMAR]`.
- Não citar nomes de pessoas ou empresas do mercado brasileiro. Autores internacionais só os do `AUTORES.md`, com a obra.
- Todo texto final passa por `python3 scripts/copy_lint.py arquivo --peca anuncio|roteiro|livre` (nota ≥ 85, zero erro grave).
- Terminar com a checagem dos 5 verbos (PARAR, ENTENDER, SENTIR, LEMBRAR, AGIR + CONFIANÇA), uma linha cada.
