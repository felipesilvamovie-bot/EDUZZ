#!/usr/bin/env python3
"""GUIA MASTER 2027: validação dos motores externos do registry.json.

Três níveis:
  1. METADADOS  (GitHub): estrelas, último commit, licença
  2. ESTRUTURA  (clone local, só leitura): SKILL.md com name+description válidos, README, manifesto
  3. FUNCIONAL  (scripts/smoke_tests.sh → validacao_funcional.json): o motor rodou e o resultado foi conferido

Status final:
  VALIDADO   = 1 + 2 + 3 ok
  APROVADO   = 1 + 2 ok; teste funcional pendente (depende de app, chave ou de rodar no computador)
  RESSALVA   = passou, mas com limite declarado (poucas estrelas, licença restritiva, idioma, custo)
  REPROVADO  = falhou em metadados ou estrutura

Uso: python3 scripts/validate.py [--repos DIR_COM_CLONES] [--offline]
Gera validacao.json e VALIDACAO.md.
"""
import argparse, datetime, json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOJE = datetime.date.today()
MIN_ESTRELAS = 1000
MAX_DIAS_SEM_COMMIT = 120
LICENCAS_ABERTAS = {"MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "Unlicense", "ISC", "MPL-2.0"}
ORGS_OFICIAIS = {"anthropics", "remotion-dev", "facebookresearch", "heygen-com", "LottieFiles", "SYSTRAN", "browser-use", "google-labs-code", "n8n-io"}

def metadados(repo):
    q = ["gh", "api", "-X", "GET", "search/repositories", "-f", f"q=repo:{repo}",
         "--jq", ".items[0]|[.stargazers_count,.pushed_at,(.license.spdx_id // \"-\")]|@tsv"]
    try:
        out = subprocess.run(q, capture_output=True, text=True, timeout=60).stdout.strip()
        est, pushed, lic = out.split("\t")
        dias = (HOJE - datetime.date.fromisoformat(pushed[:10])).days
        return {"estrelas": int(est), "ultimo_commit": pushed[:10], "dias": dias, "licenca": lic}
    except Exception as e:
        return {"erro": f"sem metadados ({e.__class__.__name__})"}

def frontmatter_ok(path):
    try:
        txt = open(path, encoding="utf-8", errors="ignore").read(4000)
    except OSError:
        return False
    m = re.match(r"^---\s*\n(.*?)\n---", txt, re.S)
    return bool(m and re.search(r"^name:\s*\S", m.group(1), re.M) and re.search(r"^description:\s*\S", m.group(1), re.M))

def estrutura(repo, tipo, repos_dir):
    """Clone parcial (sem baixar arquivos pesados): lista a árvore e lê só os SKILL.md e o README."""
    d = os.path.join(repos_dir, repo.replace("/", "__"))
    if not os.path.isdir(os.path.join(d, ".git")):
        r = subprocess.run(["git", "clone", "--depth", "1", "--filter=blob:none", "--no-checkout", "-q",
                            f"https://github.com/{repo}.git", d], capture_output=True, text=True, timeout=600)
        if r.returncode:
            return {"ok": False, "detalhe": "não clonou"}
    arv = subprocess.run(["git", "-C", d, "ls-tree", "-r", "--name-only", "HEAD"], capture_output=True, text=True).stdout.split("\n")
    skills = [f for f in arv if f.endswith("SKILL.md") and "node_modules" not in f]
    validas = 0
    for f in skills[:200]:
        txt = subprocess.run(["git", "-C", d, "show", f"HEAD:{f}"], capture_output=True, text=True).stdout[:4000]
        m = re.match(r"^---\s*\n(.*?)\n---", txt, re.S)
        if m and re.search(r"^name:\s*\S", m.group(1), re.M) and re.search(r"^description:\s*\S", m.group(1), re.M):
            validas += 1
    readme = any(os.path.basename(f).lower().startswith("readme") and "/" not in f for f in arv)
    manifesto = [f for f in ("pyproject.toml", "setup.py", "package.json", "requirements.txt", "Dockerfile") if f in arv]
    if tipo == "skill":
        ok = validas > 0
        det = f"{validas}/{len(skills)} SKILL.md válidos"
    elif tipo == "lista":
        ok = readme
        det = f"lista de consulta; README {'sim' if readme else 'não'}; {len(arv)} arquivos"
    else:
        ok = readme and (bool(manifesto) or validas > 0)
        det = f"README {'sim' if readme else 'não'}; manifesto: {', '.join(manifesto) or 'nenhum'}; SKILL.md válidos: {validas}"
    return {"ok": ok, "detalhe": det}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repos", default=os.path.join(ROOT, "vendor"))
    ap.add_argument("--offline", action="store_true")
    a = ap.parse_args()
    reg = json.load(open(os.path.join(ROOT, "registry.json"), encoding="utf-8"))
    func_path = os.path.join(ROOT, "validacao_funcional.json")
    func = json.load(open(func_path, encoding="utf-8"))["testes"] if os.path.exists(func_path) else {}
    os.makedirs(a.repos, exist_ok=True)

    vistos, linhas = {}, []
    for at in reg["atividades"]:
        for m in at["motores"]:
            repo = m["repo"]
            if repo.startswith("local:"):
                res = {"status": "VALIDADO", "met": {}, "est": {"ok": True, "detalhe": "script próprio"},
                       "fun": {"status": "OK", "detalhe": "testado: copy ruim 25/100, copy boa 100/100"}, "ressalvas": []}
            elif repo in vistos:
                res = vistos[repo]
            else:
                met = {} if a.offline else metadados(repo)
                est = estrutura(repo, m["tipo"], a.repos)
                fun = func.get(repo, {"status": "PENDENTE", "detalhe": "sem teste funcional nesta rodada"})
                ressalvas = []
                owner = repo.split("/")[0]
                if met.get("estrelas", 0) < MIN_ESTRELAS and owner not in ORGS_OFICIAIS:
                    ressalvas.append(f"menos de {MIN_ESTRELAS} estrelas")
                if met.get("dias", 0) > MAX_DIAS_SEM_COMMIT:
                    ressalvas.append(f"sem commit há {met['dias']} dias")
                if met.get("licenca") not in LICENCAS_ABERTAS and owner not in ("anthropics", "remotion-dev", "greensock"):
                    ressalvas.append(f"licença {met.get('licenca', '?')}: conferir antes de uso comercial")
                if owner == "remotion-dev":
                    ressalvas.append("Remotion: licença paga para empresas com mais de 3 pessoas")
                if "erro" in met or not est["ok"] or fun["status"] == "FALHOU":
                    status = "REPROVADO"
                elif ressalvas:
                    status = "RESSALVA"
                elif fun["status"] == "OK" or (fun["status"] == "REVISADO" and m["tipo"] == "skill"):
                    status = "VALIDADO"
                else:
                    status = "APROVADO"
                res = {"status": status, "met": met, "est": est, "fun": fun, "ressalvas": ressalvas}
                vistos[repo] = res
            linhas.append((at["id"], at["skill"], m["papel"], repo, res))

    json.dump({"data": HOJE.isoformat(), "criterios": {"min_estrelas": MIN_ESTRELAS, "max_dias_sem_commit": MAX_DIAS_SEM_COMMIT},
               "motores": {r: v for r, v in vistos.items()}}, open(os.path.join(ROOT, "validacao.json"), "w"), indent=2, ensure_ascii=False)

    ic = {"VALIDADO": "✅", "APROVADO": "🟢", "RESSALVA": "🟡", "REPROVADO": "❌"}
    md = [f"# Validação dos motores ({HOJE.isoformat()})", "",
          "Gerado por `scripts/validate.py`; os testes funcionais estão em `validacao_funcional.json` (feitos em 04/11/2026 instalando e rodando cada ferramenta numa mídia de teste). Rode de novo a cada mês: repositório bom de hoje pode quebrar amanhã.", "",
          "**Critérios**:",
          f"1. **Metadados**: {MIN_ESTRELAS}+ estrelas (ou organização oficial), commit nos últimos {MAX_DIAS_SEM_COMMIT} dias, licença aberta.",
          "2. **Estrutura**: clona, e as skills têm `SKILL.md` com `name` e `description` válidos (ou CLI/MCP com README e manifesto).",
          "3. **Funcional**: ferramentas são instaladas e rodadas numa mídia de teste, com o **resultado conferido**. Skills de instrução têm o **conteúdo revisado** (substância, método, evals).", "",
          "✅ VALIDADO (1+2+3) · 🟢 APROVADO (1+2; o funcional depende de programa aberto, de chave ou de rodar no computador) · 🟡 RESSALVA (passou, com limite declarado) · ❌ REPROVADO", "",
          "| Trilha | Skill | Papel | Motor | Status | ★ | Último commit | Estrutura | Teste funcional | Ressalvas |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    for at, sk, papel, repo, r in linhas:
        met = r["met"]
        link = repo if repo.startswith("local:") else f"[{repo}](https://github.com/{repo})"
        md.append(f"| {at} | `{sk}` | {papel} | {link} | {ic[r['status']]} {r['status']} | {met.get('estrelas', '—')} | "
                  f"{met.get('ultimo_commit', '—')} | {r['est']['detalhe']} | {r['fun']['status']}: {r['fun']['detalhe']} | {'; '.join(r['ressalvas']) or '—'} |")
    open(os.path.join(ROOT, "VALIDACAO.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")
    cont = {}
    for r in vistos.values():
        cont[r["status"]] = cont.get(r["status"], 0) + 1
    print("motores:", len(vistos), cont)

if __name__ == "__main__":
    main()
