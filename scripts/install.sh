#!/usr/bin/env bash
# GUIA MASTER 2027: instalação.
#   ./scripts/install.sh              instala as skills do Guia Master + as skills externas primárias do registry.json
#   ./scripts/install.sh --tools      + cria um ambiente Python isolado por ferramenta (auto-editor, faster-whisper...)
#   ./scripts/install.sh --dry        mostra o que faria
# Skills vão para ~/.claude/skills (mude com CLAUDE_SKILLS_DIR). Clones ficam em vendor/ (fora do git).
# MCPs (Meta Ads, Figma, n8n) e ferramentas comerciais: ver o README de cada repositório.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
VENDOR="$ROOT/vendor"; TOOLS="$ROOT/vendor/tools"
SKILLS_DIR="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
DRY=0; DO_TOOLS=0
for a in "$@"; do case "$a" in --dry) DRY=1;; --tools) DO_TOOLS=1;; *) echo "opção desconhecida: $a" >&2; exit 2;; esac; done
run() { if [ "$DRY" = 1 ]; then echo "[dry] $*"; else "$@"; fi; }
mkdir -p "$VENDOR" "$SKILLS_DIR"

echo "== skills do Guia Master 2027"
for d in "$ROOT"/skills/*/; do n="$(basename "$d")"; t="gm-$n"; [ "$n" = guia-master ] && t=guia-master; run ln -sfn "$d" "$SKILLS_DIR/$t"; echo "  $t"; done

echo "== motores (registry.json)"
python3 - "$ROOT/registry.json" <<'PY' > "$VENDOR/.fila"
import json, re, sys
eng = {}
for at in json.load(open(sys.argv[1]))["atividades"]:
    for m in at["motores"]:
        if m["papel"] == "estudo" or m["repo"].startswith("local:"): continue
        e = eng.setdefault(m["repo"], {"tipo": m["tipo"], "papel": m["papel"], "usar": set()})
        if m["papel"] == "primario": e["papel"] = "primario"
        for u in m.get("usar", []):
            nome = re.split(r"[ :(]", u.strip())[0]
            if re.fullmatch(r"[a-z0-9-]+", nome): e["usar"].add(nome)
for r, e in eng.items():
    print(r, e["tipo"], e["papel"], ",".join(sorted(e["usar"])) or "-")
PY
while read -r repo tipo papel usar; do
  case "$tipo" in
    skill)
      if [ "$repo" = heygen-com/hyperframes ]; then
        # o próprio projeto pede para instalar as skills pela CLI, na versão que casa com ela
        echo "  skill  [$papel] $repo → rode: npx hyperframes skills update"; continue
      fi
      dest="$VENDOR/${repo//\//__}"
      if [ -d "$dest/.git" ]; then run git -C "$dest" pull --ff-only -q || true
      else
        # clone parcial + checkout esparso: baixa só as pastas que têm SKILL.md (algumas bibliotecas de prompt passam de 200 MB de imagens)
        run git clone --depth 1 --filter=blob:none --no-checkout -q "https://github.com/$repo.git" "$dest" || { echo "  aviso: falhou $repo"; continue; }
        if [ "$DRY" = 0 ]; then
          dirs=$(git -C "$dest" ls-tree -r --name-only HEAD | grep 'SKILL.md$' | grep -v node_modules | xargs -r -n1 dirname | sort -u)
          git -C "$dest" sparse-checkout init --cone -q 2>/dev/null || git -C "$dest" sparse-checkout init --cone
          if printf '%s\n' $dirs | grep -qx '\.'; then git -C "$dest" sparse-checkout disable; else git -C "$dest" sparse-checkout set $dirs; fi
          git -C "$dest" checkout -q
        fi
      fi
      [ -d "$dest" ] && find "$dest" -name SKILL.md -not -path '*/node_modules/*' -not -path '*/.claude/*' -not -path '*/test*' | while read -r f; do
        sd="$(dirname "$f")"; sn="$(basename "$sd")"; [ "$sd" = "$dest" ] && sn="$(basename "$dest")"
        # só as skills que o registry usa (evita encher o Claude de skills que o Guia Master não chama)
        if [ "$usar" != "-" ] && [ "$sd" != "$dest" ] && ! printf ',%s,' "$usar" | grep -q ",$sn,"; then continue; fi
        run ln -sfn "$sd" "$SKILLS_DIR/ext-${repo%%/*}-$sn"
      done
      echo "  skill  [$papel] $repo";;
    cli|lib)
      if [ "$DO_TOOLS" = 1 ]; then
        name="${repo##*/}"; env="$TOOLS/$name"
        case "$repo" in
          SYSTRAN/faster-whisper) pkgs='faster-whisper av<16';;   # av<16 obrigatório (validado em 2026-11-04)
          Breakthrough/PySceneDetect) pkgs='scenedetect opencv-python-headless';;
          danielgatis/rembg) pkgs='rembg[cpu,cli]';;
          WyattBlue/auto-editor) pkgs='auto-editor';;
          m-bain/whisperX) pkgs='whisperx';;
          facebookresearch/demucs) pkgs='demucs';;
          *) pkgs='';;
        esac
        if [ -n "$pkgs" ]; then run python3 -m venv "$env"; run "$env/bin/pip" install -q $pkgs; echo "  tool   [$papel] $repo → $env/bin"; fi
      else echo "  tool   [$papel] $repo (use --tools para instalar num ambiente isolado)"; fi;;
    lista) echo "  lista  [$papel] $repo → consulta (não instala)";;
    mcp) echo "  mcp    [$papel] $repo → instalar no computador (ver README do repositório)";;
  esac
done < "$VENDOR/.fila"
rm -f "$VENDOR/.fila"
echo
echo "Pronto. Reinicie o Claude Code e diga: monta meu plano 2027. Para revalidar os motores: python3 scripts/validate.py"
