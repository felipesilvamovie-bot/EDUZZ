# GUIA MASTER 2027

**O repositório do infoprodutor.** Os métodos que construíram os maiores negócios digitais do
mundo (oferta, conteúdo, lançamento, vendas, marca, criação com IA e operação), organizados em
**7 trilhas** e transformados em **skills** que executam com os **melhores repositórios abertos**,
cada um validado.

> **Quem é você no digital, e qual negócio você vai construir em 2027?**
> Este repositório existe para responder a essa pergunta e transformar a resposta num plano.

---

## Como funciona

```
RECONHECER  →  ESCOLHER  →  PLANEJAR  →  EXECUTAR
(Trilha 1)     (2, 3, 4, 5)   (7 + plano)   (6)
```

| # | Trilha | A pergunta | Skill |
|---|---|---|---|
| 1 | [Identidade](trilhas/1-identidade) | Quem eu sirvo e por que eu? | `identidade` |
| 2 | [Oferta](trilhas/2-oferta) | O que eu vendo, por quanto, em que escada? | `oferta` |
| 3 | [Conteúdo e audiência](trilhas/3-conteudo-e-audiencia) | Como paro o dedo e construo confiança? | `conteudo-viral` |
| 4 | [Aquisição](trilhas/4-aquisicao) | Como atenção vira venda, todo mês? | `aquisicao` |
| 5 | [Comercial](trilhas/5-comercial) | Como fecho ticket alto sem empurrar? | `comercial` |
| 6 | [Criação com IA](trilhas/6-criacao-com-ia) | Como produzo no padrão dos melhores? | `criacao-ia` |
| 7 | [Operação e plano 2027](trilhas/7-operacao-e-plano-2027) | O que priorizo e como meço? | `operacao-2027` |

A skill **`guia-master`** é a porta de entrada: descreva o que precisa, e ela identifica a trilha
e chama a skill e o repositório certos.

## O que tem dentro

- **[MAPA.md](MAPA.md)**: o caminho, os 5 verbos do consumidor (parar, entender, sentir, lembrar, agir), a regra anti-salada e a linha vermelha.
- **[AUTORES.md](AUTORES.md)**: o conselho de autores internacionais (Hormozi, Gary Vaynerchuk, McKee, Brunson, Jeff Walker, Schwartz, Ogilvy, Godin, Kahneman, Cialdini, Chris Voss, Rackham, MrBeast e outros), cada um com a ideia que muda uma decisão.
- **[trilhas/](trilhas)**: 7 trilhas com os métodos em formato aplicável, exercício para 2027, métricas e motores.
- **[PLANO-2027.md](PLANO-2027.md)**: o plano do ano em uma página.
- **[skills/](skills)**: 8 skills prontas para o Claude Code.
- **[templates/](templates)**: oferta em uma página, roteiro de conteúdo, roteiro de call de vendas, briefing de criativo.
- **[registry.json](registry.json)** e **[VALIDACAO.md](VALIDACAO.md)**: os repositórios externos de cada trilha e o status de cada um.
- **[scripts/](scripts)**: instalador, validador e o corretor de objetividade (`copy_lint.py`).

## Os motores (o melhor do GitHub, validado)

| Área | Repositórios |
|---|---|
| Marketing, oferta, copy, anúncio, lançamento | `coreyhaines31/marketingskills` (58k ★, 53 skills com evals) |
| Ganchos e conteúdo | `instagram-agent-skill` (26 fórmulas de gancho), `youtube-agent-skill` (21 fórmulas) |
| Design | `ui-ux-pro-max-skill`, `hallmark` (design sem cara de IA), `anthropics/skills` (oficial), Figma MCP, Stitch skills, Pencil |
| Imagem | `awesome-gpt-image-2` (GPT Image 2), bibliotecas com milhares de prompts de Nano Banana Pro, conector Magnific/Freepik |
| Vídeo com IA | `higgsfield-ai-prompt-skill` (36 skills: Seedance, Kling, Veo), `seedance2-skill`, `visual-skills` |
| Motion e edição | `hyperframes` (78k ★), `motion-design-skill` (LottieFiles), `auto-editor`, `ffmpeg-skill`, `faster-whisper` |
| Vendas e automação | `waha` (WhatsApp), `n8n-mcp` (o Claude monta automações), templates de n8n |

Status de cada um em [VALIDACAO.md](VALIDACAO.md): metadados (estrelas, último commit, licença) +
estrutura (as skills têm formato válido) + teste funcional ou revisão de conteúdo. A validação
**reprova** o que não passa: um repositório de vendas com 1,5k estrelas foi reprovado porque nenhuma das suas 14 skills tinha formato válido.

## Instalação

```bash
git clone https://github.com/felipesilvamovie-bot/EDUZZ guia-master && cd guia-master
./scripts/install.sh              # 8 skills do guia + skills externas (só as pastas de skill, sem os GB de imagens)
./scripts/install.sh --tools      # + ferramentas Python em ambientes isolados (auto-editor, faster-whisper...)
npx hyperframes skills update     # skills de motion do HyperFrames, na versão da CLI
```
Reinicie o Claude Code e diga: **"monta meu plano 2027"**.

## Comandos

- "monta meu plano 2027" · "por onde eu começo?"
- "me ajuda a me posicionar" · "monta minha oferta" · "cria minha escada de valor"
- "30 ganchos para o meu nicho" · "roteiro de Reels para consciência zero" · "monta uma série"
- "planeja meu lançamento" · "roteiro de anúncio" · "estrutura da minha VSL"
- "roteiro de call de vendas" · "responde essas objeções" · "cadência de follow-up no WhatsApp"
- "prompt pro Nano Banana / GPT Image / Higgsfield / Seedance" · "faz o motion" · "edita esse vídeo"
- "monta meu painel de métricas" · "automatiza meu onboarding"

## Regras

1. **Anti-salada**: comece pela trilha que trava hoje. No máximo 3 prioridades por ano.
2. **Linha vermelha**: nada de número, depoimento, resultado ou escassez inventados; nada subliminar; respeito às regras das plataformas, ao CONAR e ao CDC.
3. **Objetividade**: todo texto passa pelo `scripts/copy_lint.py` (nota ≥ 85).
4. **Revalidar** os motores a cada mês: `python3 scripts/validate.py`.

## Créditos

Os métodos citados pertencem aos seus autores, listados com as obras em [AUTORES.md](AUTORES.md).
Este repositório resume conceitos e aponta as fontes, sem reproduzir as obras. Os repositórios
externos mantêm as próprias licenças (ver [VALIDACAO.md](VALIDACAO.md)).
