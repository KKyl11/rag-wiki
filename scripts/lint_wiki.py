"""Wiki 健康檢查（AGENTS.md §8.3，需求 R8）。

用法：python scripts/lint_wiki.py [--report docs/lint-report.md]
exit code：0 = 無 error；1 = 有 error。warning 不影響 exit code。

檢查項目
(a) 斷的內部連結           (b) 孤兒頁（index/log 的連入不算）
(c) 沒有出處的段落／條列／表格列
(d) 出處 key 不存在、出處格式錯誤、PDF 頁碼超出 raw 頁數、網頁 § 小節在 raw 找不到
(e) 頁面未列入 index.md    (f) 矛盾區塊少於兩個不同來源
(g) frontmatter 缺欄位、type 不合法、source 頁缺 key/url/raw、body 引用的 key 未列在 frontmatter sources
(h) 「教學比喻」行含數字    (i) AGENTS.md 超過 12,000 字元
(j) wiki 區塊裡的數字，必須出現在所引用的 raw 頁面（PDF 依頁碼、網頁依整份 md）
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
RAW = ROOT / "raw"
SPECIAL = {"index.md", "log.md"}
CITE_RE = re.compile(r"\[src:\s*([^\]]+)\]")
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)\)")
EXEMPT_HEADINGS = ("相關頁面",)
ANALOGY_MARK = "教學比喻（非來源內容）"


def parse_frontmatter(text):
    if not text.startswith("---\n"):
        return {}, text, 0
    end = text.find("\n---", 4)
    if end < 0:
        return {}, text, 0
    fm = {}
    for line in text[4:end].splitlines():
        m = re.match(r"^(\w+):\s*(.*)$", line)
        if m:
            k, v = m.group(1), m.group(2).strip()
            if v.startswith("[") and v.endswith("]"):
                v = [x.strip() for x in v[1:-1].split(",") if x.strip()]
            fm[k] = v
    body_start = end + 4
    return fm, text[body_start:], text[:body_start].count("\n")


def parse_citations(s):
    """回傳 [(key, locator)]；locator 例：'p.3'、'p.3-4'、'§Methodology'。"""
    out = []
    for inner in CITE_RE.findall(s):
        # 允許 [src: a, p.1; b, p.2]
        for part in inner.split(";"):
            bits = [b.strip() for b in part.split(",", 1)]
            out.append((bits[0], bits[1] if len(bits) > 1 else ""))
    return out


def pdf_pages(key, cache={}):
    if key in cache:
        return cache[key]
    p = RAW / f"{key}.pdf"
    n = None
    if p.exists():
        try:
            import logging
            logging.disable(logging.WARNING)
            from pypdf import PdfReader
            n = len(PdfReader(str(p)).pages)
        except Exception:
            n = None
    cache[key] = n
    return n


def md_headings(key, cache={}):
    if key in cache:
        return cache[key]
    p = RAW / f"{key}.md"
    hs = set()
    if p.exists():
        for line in p.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^#{1,6}\s+(.*)$", line)
            if m:
                hs.add(m.group(1).strip())
    cache[key] = hs
    return hs


NUM_RE = re.compile(r"(?<![\w.\-])\d+(?:\.\d+)?")


def strip_for_numbers(s):
    """移除出處標記、連結、型號名稱等不需要對照的數字。"""
    s = CITE_RE.sub("", s)
    s = re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", s)  # 條列符號（含 1. 2. 編號）
    s = re.sub(r"\d{4}-\d{2}-\d{2}", "", s)  # 日期（書目、抓取日）
    s = re.sub(r"\]\([^)]*\)", "]", s)
    s = re.sub(r"`[^`]*`", "", s)
    s = re.sub(r"[A-Za-z]+[\w.\-]*\d[\w.\-]*", "", s)  # Llama2、GPT-4、Claude-1.3、C0、TS-999、p.3 等
    return s.replace(",", "")


def raw_text(key, pages, cache={}):
    if (key, pages) in cache:
        return cache[(key, pages)]
    txt = ""
    if (RAW / f"{key}.pdf").exists():
        if key not in cache:
            import logging
            logging.disable(logging.WARNING)
            from pypdf import PdfReader
            cache[key] = [pg.extract_text() or "" for pg in PdfReader(str(RAW / f"{key}.pdf")).pages]
        allp = cache[key]
        lo, hi = pages
        txt = " ".join(allp[i - 1] for i in range(lo, hi + 1) if 1 <= i <= len(allp))
    elif (RAW / f"{key}.md").exists():
        txt = (RAW / f"{key}.md").read_text(encoding="utf-8")
    txt = txt.replace(",", "")
    words = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
             "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "twenty": 20, "fifty": 50, "hundred": 100}
    txt += " " + " ".join(str(v) for k, v in words.items() if re.search(rf"\b{k}\b", txt, re.I))
    cache[(key, pages)] = txt
    return txt


def number_in(num, txt):
    return re.search(r"(?<![\d.])" + re.escape(num) + r"(?![\d]|\.\d)", txt) is not None


def blocks(body, line_offset):
    """把 body 切成需要出處的區塊：(行號, 種類, 文字)。"""
    lines = body.splitlines()
    out, i, in_code, heading = [], 0, False, ""
    para, para_start = [], 0
    is_header_row = True

    def flush_para():
        nonlocal para
        if para:
            out.append((para_start, "paragraph", " ".join(para), heading))
            para = []

    while i < len(lines):
        raw = lines[i]
        ln = line_offset + i + 1
        s = raw.strip()
        if s.startswith("```"):
            flush_para()
            in_code = not in_code
        elif in_code:
            pass
        elif not s:
            flush_para()
            is_header_row = True
        elif s.startswith("#"):
            flush_para()
            heading = s.lstrip("#").strip()
        elif s.startswith(">"):
            flush_para()
            # 收集連續 blockquote 成一個區塊
            q, start = [], ln
            while i < len(lines) and lines[i].strip().startswith(">"):
                q.append(lines[i].strip().lstrip(">").strip())
                i += 1
            out.append((start, "quote", "\n".join(q), heading))
            continue
        elif s.startswith("|"):
            flush_para()
            if re.match(r"^\|[\s:\-|]+\|$", s):
                pass  # 分隔列
            elif is_header_row:
                is_header_row = False  # 表頭不需要出處
            else:
                out.append((ln, "table-row", s, heading))
        elif re.match(r"^([-*]|\d+\.)\s+", s):
            flush_para()
            out.append((ln, "list-item", s, heading))
        else:
            if not para:
                para_start = ln
            para.append(s)
        i += 1
    flush_para()
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--report", default=str(ROOT / "docs" / "lint-report.md"))
    args = ap.parse_args()

    errors, warnings = [], []

    def err(code, where, msg):
        errors.append((code, where, msg))

    def warn(code, where, msg):
        warnings.append((code, where, msg))

    pages = sorted(p for p in WIKI.rglob("*.md") if p.name not in SPECIAL)
    source_keys = {p.stem for p in (WIKI / "sources").glob("*.md")}
    inbound = {p.resolve(): set() for p in pages}
    all_md = pages + [WIKI / n for n in SPECIAL if (WIKI / n).exists()]

    # (a) 斷連結 + 收集連入
    for p in all_md:
        text = p.read_text(encoding="utf-8")
        for n, line in enumerate(text.splitlines(), 1):
            line = re.sub(r"`[^`]*`", "", line)  # 行內程式碼裡的範例不算連結
            for target in LINK_RE.findall(line):
                if re.match(r"^[a-z]+://", target) or target.startswith("#") or target.startswith("mailto:"):
                    continue
                t = (p.parent / target.split("#")[0]).resolve()
                rel = p.relative_to(ROOT).as_posix()
                if not t.exists():
                    err("a", f"{rel}:{n}", f"斷連結 → {target}")
                elif t in inbound and p.name not in SPECIAL and t != p.resolve():
                    inbound[t].add(p.resolve())

    # (b) 孤兒頁
    for p in pages:
        if not inbound[p.resolve()]:
            err("b", p.relative_to(ROOT).as_posix(), "孤兒頁：沒有任何其他 wiki 頁面連入（index/log 不算）")

    # (e) index 收錄
    index_text = (WIKI / "index.md").read_text(encoding="utf-8") if (WIKI / "index.md").exists() else ""
    indexed = {(WIKI / t.split("#")[0]).resolve() for t in LINK_RE.findall(index_text)}
    for p in pages:
        if p.resolve() not in indexed:
            err("e", p.relative_to(ROOT).as_posix(), "未列入 wiki/index.md")

    for p in pages:
        rel = p.relative_to(ROOT).as_posix()
        text = p.read_text(encoding="utf-8")
        fm, body, off = parse_frontmatter(text)

        # (g) frontmatter
        for k in ("type", "sources", "updated"):
            if k not in fm or fm[k] in ("", []):
                err("g", rel, f"frontmatter 缺 `{k}`")
        t = fm.get("type")
        expected = {"sources": "source", "concepts": "concept", "comparisons": "comparison"}.get(p.parent.name)
        if t and expected and t != expected:
            err("g", rel, f"type={t} 但放在 {p.parent.name}/（應為 {expected}）")
        if t == "source":
            for k in ("key", "url", "raw"):
                if k not in fm:
                    err("g", rel, f"source 頁 frontmatter 缺 `{k}`")
            if fm.get("raw") and not (ROOT / fm["raw"]).exists():
                err("g", rel, f"raw 檔不存在：{fm['raw']}")
        fm_sources = set(fm.get("sources") or []) if isinstance(fm.get("sources"), list) else set()

        used = set()
        for ln, kind, txt, heading in blocks(body, off):
            where = f"{rel}:{ln}"
            cites = parse_citations(txt)
            # (h) 教學比喻
            if ANALOGY_MARK in txt:
                if re.search(r"\d", txt.replace(ANALOGY_MARK, "")):
                    err("h", where, "教學比喻含數字（比喻不得含事實或數字）")
                continue
            # (f) 矛盾區塊
            if kind == "quote" and "⚖️" in txt:
                keys = {k for k, _ in cites}
                if len(keys) < 2:
                    err("f", where, f"矛盾區塊只引用 {len(keys)} 個來源（至少 2 個不同來源）")
            # (c) 出處
            # 「相關頁面」底下只豁免「純連結」的條列項；其他內容照樣要出處
            pure_link = kind == "list-item" and not re.sub(r"\[[^\]]*\]\([^)]*\)|[-*\s、，,]", "", txt)
            exempt = pure_link and any(h in heading for h in EXEMPT_HEADINGS)
            if not cites and not exempt:
                err("c", where, f"{kind} 沒有出處：{txt[:60]}")
            # (d) key 與 locator
            for key, loc in cites:
                used.add(key)
                if key not in source_keys:
                    err("d", where, f"出處 key 不存在：{key}")
                    continue
                if (RAW / f"{key}.pdf").exists():
                    m = re.match(r"^pp?\.\s*(\d+)(?:\s*[-–]\s*(\d+))?$", loc)
                    if not m:
                        err("d", where, f"PDF 來源 {key} 的出處需寫頁碼 p.N：「{loc}」")
                    else:
                        n = pdf_pages(key)
                        hi = int(m.group(2) or m.group(1))
                        if n and (int(m.group(1)) < 1 or hi > n):
                            err("d", where, f"{key} 頁碼 {loc} 超出 raw PDF 頁數 {n}")
                elif (RAW / f"{key}.md").exists():
                    if not loc.startswith("§"):
                        err("d", where, f"網頁來源 {key} 的出處需寫 §小節：「{loc}」")
                    elif loc[1:].strip() not in md_headings(key):
                        err("d", where, f"{key} 找不到小節「{loc[1:].strip()}」")
            # (j) 數字對照 raw
            if cites:
                corpus = ""
                for key, loc in cites:
                    m = re.match(r"^pp?\.\s*(\d+)(?:\s*[-–]\s*(\d+))?$", loc)
                    pages = (int(m.group(1)), int(m.group(2) or m.group(1))) if m else (0, 0)
                    corpus += " " + raw_text(key, pages)
                for num in NUM_RE.findall(strip_for_numbers(txt)):
                    if not number_in(num, corpus):
                        err("j", where, f"數字 {num} 在引用的 raw 頁面找不到")
        missing = used - fm_sources
        if missing:
            err("g", rel, f"body 引用了 {sorted(missing)} 但 frontmatter sources 沒列")
        unused = fm_sources - used
        if unused:
            warn("g", rel, f"frontmatter sources 列了 {sorted(unused)} 但 body 沒引用")

    # (i) AGENTS.md 長度
    agents = ROOT / "AGENTS.md"
    if agents.exists():
        n = len(agents.read_text(encoding="utf-8"))
        if n > 12000:
            err("i", "AGENTS.md", f"{n} 字元，超過 12,000")

    # 統計
    counts = {d: len(list((WIKI / d).glob("*.md"))) for d in ("sources", "concepts", "comparisons")}
    lines = [
        "# Lint report",
        "",
        f"- 指令：`python scripts/lint_wiki.py`",
        f"- 頁面：sources {counts['sources']}、concepts {counts['concepts']}、comparisons {counts['comparisons']}（共 {len(pages)} 頁）",
        f"- 結果：**{'PASS' if not errors else 'FAIL'}** — {len(errors)} error、{len(warnings)} warning",
        "",
    ]
    if errors:
        lines += ["## Errors", "", "| 項目 | 位置 | 說明 |", "|---|---|---|"]
        lines += [f"| ({c}) | `{w}` | {m} |" for c, w, m in errors]
        lines.append("")
    if warnings:
        lines += ["## Warnings", "", "| 項目 | 位置 | 說明 |", "|---|---|---|"]
        lines += [f"| ({c}) | `{w}` | {m} |" for c, w, m in warnings]
        lines.append("")
    report = "\n".join(lines)
    Path(args.report).parent.mkdir(parents=True, exist_ok=True)
    Path(args.report).write_text(report, encoding="utf-8")
    sys.stdout.reconfigure(encoding="utf-8")
    print(report)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
