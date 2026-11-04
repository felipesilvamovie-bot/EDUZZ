---
name: guia-master
description: "A porta de entrada do Guia Master 2027, o repositório do infoprodutor para o plano de 2027. Recebe qualquer pedido de negócio digital - posicionamento, oferta, conteúdo, ganchos virais, tráfego, lançamento, funil, vendas de ticket alto, design, imagem e vídeo com IA, motion, edição, automação, métricas, plano anual - identifica a trilha (1 identidade, 2 oferta, 3 conteúdo, 4 aquisição, 5 comercial, 6 criação com IA, 7 operação) e chama a skill e o repositório validado certos. Use SEMPRE que alguém pedir \"monta meu plano 2027\", \"por onde eu começo\", \"o que eu priorizo\", \"guia master\", ou trouxer um pedido que cruze várias trilhas."
---

# GUIA MASTER 2027: o roteador

**A pergunta que guia tudo: quem é você no digital, e qual negócio você vai construir em 2027?**

## Mapa das trilhas
| Se o pedido é... | Trilha | Skill |
|---|---|---|
| nicho, posicionamento, marca pessoal, "quem eu sirvo" | `trilhas/1-identidade` | `identidade` |
| produto, preço, escada de valor, bônus, garantia, upsell | `trilhas/2-oferta` | `oferta` |
| post, Reels, Shorts, YouTube, gancho, roteiro, série, storytelling | `trilhas/3-conteudo-e-audiencia` | `conteudo-viral` |
| anúncio, tráfego, lançamento, funil, VSL, e-mail, afiliados | `trilhas/4-aquisicao` | `aquisicao` |
| call de vendas, SDR, closer, objeções, WhatsApp, follow-up | `trilhas/5-comercial` | `comercial` |
| design, página, imagem, prompt (GPT, Nano Banana, Magnific), vídeo com IA (Higgsfield, Seedance, Veo, Kling), motion, edição | `trilhas/6-criacao-com-ia` | `criacao-ia` |
| métricas, retenção, comunidade, automação, time, plano anual | `trilhas/7-operacao-e-plano-2027` | `operacao-2027` |

## Fluxo
1. **Descobrir a trilha que trava hoje** (não a mais legal). Se o pedido é amplo, perguntar em uma linha: "o que mais está travando: ser escolhido, a oferta, a atenção, a venda, a produção ou a operação?"
2. Chamar a skill daquela trilha. Pedido que cruza trilhas: seguir a ordem do `MAPA.md` (Reconhecer → Escolher → Planejar → Executar).
3. **"Monta meu plano 2027"**: preencher o `PLANO-2027.md` bloco a bloco, chamando cada skill para o seu bloco, e no fim escolher **no máximo 3 prioridades**.
4. Entregar o resultado + uma linha por trilha usada: "trilha → skill → repositório".

Este repositório fica dois níveis acima da pasta real desta skill (resolver com `readlink -f`). Ler `MAPA.md` (o caminho e os 5 verbos), a trilha indicada abaixo e só a parte do `AUTORES.md` que for citar. Os motores estão em `registry.json` e o status de cada um em `VALIDACAO.md`: use o primário; se ele não estiver instalado ou tiver ressalva que pese no caso, use o reserva e diga por quê.

**Regras de todas as skills do Guia Master**
- Falar com o infoprodutor em português simples e direto. Entregar **decisão e peça pronta**, não aula.
- Nunca inventar número, depoimento, resultado ou escassez. Dado que falta: perguntar uma vez ou marcar `[CONFIRMAR]`.
- Não citar nomes de pessoas ou empresas do mercado brasileiro. Autores internacionais só os do `AUTORES.md`, com a obra.
- Todo texto final passa por `python3 scripts/copy_lint.py arquivo --peca anuncio|roteiro|livre` (nota ≥ 85, zero erro grave).
- Terminar com a checagem dos 5 verbos (PARAR, ENTENDER, SENTIR, LEMBRAR, AGIR + CONFIANÇA), uma linha cada.
