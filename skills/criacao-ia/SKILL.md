---
name: criacao-ia
description: "Trilha 6 do Guia Master 2027: produção com IA no padrão dos melhores - design de página e de peça (Rams, Norman, Bass; skills ui-ux-pro-max, hallmark, anthropics frontend-design, Figma MCP, Stitch, Pencil), prompts de imagem (GPT Image 2, Nano Banana Pro, Magnific/Freepik), prompts de vídeo com IA (Higgsfield, Seedance, Veo, Kling), motion (HyperFrames, princípios da LottieFiles, motion storytelling editorial) e edição (auto-editor, ffmpeg-skill, faster-whisper). Use quando pedirem arte, criativo, página, landing, prompt de imagem, prompt de vídeo, \"faz no Nano Banana\", \"prompt pro GPT\", Higgsfield, Seedance, Veo, Kling, Magnific, motion, vinheta, legenda, edição, corte, ou a parte 5 do plano 2027."
---

# CRIAÇÃO COM IA

Base: `trilhas/6-criacao-com-ia/README.md` e `templates/briefing-criativo.md`.

## Fluxo
1. **Briefing de uma página**: pra quem, a ideia em uma frase, o verbo que a peça resolve, o nível de consciência, os ativos da marca.
2. **Escolher o motor** pela tabela da trilha (design, imagem, vídeo, motion, edição). Instalado? Usar. Não instalado? Indicar o comando do `registry.json` e entregar o prompt pronto para a ferramenta.
3. **Imagem**: prompt na ordem sujeito → cenário → câmera → luz → estilo → texto exato → marca → formato → evitar. Entregar a arte final (com título, CTA e hierarquia), não só o fundo. Consultar as bibliotecas de prompt (GPT Image 2, Nano Banana Pro) para o estilo.
4. **Vídeo com IA**: um plano por prompt, sujeito descrito igual em todas as cenas, primeiro e último frame quando possível, 3–4 variações por plano.
5. **Motion**: escolher o estilo pela mensagem (editorial para storytelling, legenda de impacto para UGC, keynote para lançamento, one-take para explainer, dados para resultados). HyperFrames para construir; checklist de timing e easing da LottieFiles.
6. **Edição**: auto-editor para tirar silêncios; faster-whisper (instalar com `"av<16"`) para a legenda palavra por palavra; ffmpeg-skill para formato, loudness e entrega.
7. **Crítica antes de entregar**: os 5 verbos, as 7 regras de design, nada de cara de IA (checagem do `hallmark`).
8. **Linha vermelha**: nunca apresentar pessoa ou depoimento gerado por IA como real.

## Motores
Design: `nextlevelbuilder/ui-ux-pro-max-skill`, `Nutlope/hallmark`, `anthropics/skills`, `GLips/Figma-Context-MCP`, `google-labs-code/stitch-skills`. Imagem: `freestylefly/awesome-gpt-image-2`, `YouMind-OpenLab/nano-banana-pro-prompts-recommend-skill`, `ZeroLu/awesome-nanobanana-pro`, conector Magnific/Freepik. Vídeo IA: `OSideMedia/higgsfield-ai-prompt-skill`, `dexhunter/seedance2-skill`, `smixs/visual-skills`. Motion e edição: `heygen-com/hyperframes`, `LottieFiles/motion-design-skill`, `WyattBlue/auto-editor`, `kajisho5/ffmpeg-skill`, `SYSTRAN/faster-whisper`.

## Saída
Peças, prompts prontos por ferramenta, roteiro de motion ou o arquivo final, com o motor usado. Checagem dos 5 verbos.

Este repositório fica dois níveis acima da pasta real desta skill (resolver com `readlink -f`). Ler `MAPA.md` (o caminho e os 5 verbos), a trilha indicada abaixo e só a parte do `AUTORES.md` que for citar. Os motores estão em `registry.json` e o status de cada um em `VALIDACAO.md`: use o primário; se ele não estiver instalado ou tiver ressalva que pese no caso, use o reserva e diga por quê.

**Regras de todas as skills do Guia Master**
- Falar com o infoprodutor em português simples e direto. Entregar **decisão e peça pronta**, não aula.
- Nunca inventar número, depoimento, resultado ou escassez. Dado que falta: perguntar uma vez ou marcar `[CONFIRMAR]`.
- Não citar nomes de pessoas ou empresas do mercado brasileiro. Autores internacionais só os do `AUTORES.md`, com a obra.
- Todo texto final passa por `python3 scripts/copy_lint.py arquivo --peca anuncio|roteiro|livre` (nota ≥ 85, zero erro grave).
- Terminar com a checagem dos 5 verbos (PARAR, ENTENDER, SENTIR, LEMBRAR, AGIR + CONFIANÇA), uma linha cada.
