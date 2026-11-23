"""topic-slides 流程共用的解析工具（檢查腳本與渲染腳本共用，避免各寫各的解析規則）。"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"

CITE_RE = re.compile(r"\[src:\s*([^\]]+)\]")
WIKI_REF_RE = re.compile(r"\[wiki:\s*([^\]]+)\]")
EVID_RE = re.compile(r"^- (E\d+):\s*(.*)$")
QUAL_RE = re.compile(r"〔限定[:：]\s*([^〕]+)〕")  # v2：證據卡上的限定詞（範圍／條件／歸屬）
GENERALIZERS = ["常常", "通常", "經常", "常把", "常用", "總是", "一定會", "一定要", "所有的", "全部都", "永遠", "保證", "必然", "絕對", "完全消除", "都能", "最好的"]
NUM_RE = re.compile(r"(?<![\w.\-])\d+(?:\.\d+)?")
ANALOGY_MARK = "教學比喻（非來源內容）"


def parse_frontmatter(text):
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    fm = {}
    for line in text[4:end].splitlines():
        m = re.match(r"^(\w+):\s*(.*)$", line)
        if m:
            k, v = m.group(1), m.group(2).strip()
            if v.startswith("[") and v.endswith("]"):
                v = [x.strip() for x in v[1:-1].split(",") if x.strip()]
            fm[k] = v
    return fm, text[end + 4:].lstrip("\n")


def wiki_path(p):
    """接受 'concepts/rag.md' 或 'wiki/concepts/rag.md'，回傳 wiki 內的 Path。"""
    p = p.strip()
    if p.startswith("wiki/"):
        p = p[5:]
    return WIKI / p


def norm_wiki(p):
    p = p.strip()
    return p[5:] if p.startswith("wiki/") else p


def strip_for_numbers(s):
    """移除出處標記、條列編號、日期、型號名稱等不需要對照的數字，回傳要檢查的文字。"""
    s = CITE_RE.sub("", s)
    s = WIKI_REF_RE.sub("", s)
    s = re.sub(r"(?m)^\s*(?:[-*]|\d+\.)\s+", "", s)
    s = re.sub(r"\d{4}-\d{2}-\d{2}", "", s)
    s = re.sub(r"\]\([^)]*\)", "]", s)
    s = re.sub(r"`[^`]*`", "", s)
    s = re.sub(r"[A-Za-z]+[\w.\-]*\d[\w.\-]*", "", s)  # Llama2、GPT-4、Claude-1.3、C0、TS-999、Q2 等
    s = re.sub(r"\d+(?:\.\d+)?\s*[-–]\s*(?=\d)", lambda m: m.group(0).replace("-", " ").replace("–", " "), s)
    return s.replace(",", "")


def numbers_in(text):
    return NUM_RE.findall(strip_for_numbers(text))


def number_found(num, corpus):
    corpus = corpus.replace(",", "")
    return re.search(r"(?<![\d.])" + re.escape(num) + r"(?![\d]|\.\d)", corpus) is not None


def parse_cards(run):
    """回傳 {key: {"fm":..., "items": {Eid: (claim, [wiki refs])}}}"""
    cards = {}
    for p in sorted((Path(run) / "cards").glob("*.md")):
        fm, body = parse_frontmatter(p.read_text(encoding="utf-8"))
        items, quals = {}, {}
        for line in body.splitlines():
            m = EVID_RE.match(line.strip())
            if m:
                items[m.group(1)] = (m.group(2), [norm_wiki(x) for x in WIKI_REF_RE.findall(m.group(2))])
                quals[m.group(1)] = [q.strip() for qs in QUAL_RE.findall(m.group(2)) for q in re.split(r"[／/]", qs) if q.strip()]
        cards[fm.get("source", p.stem)] = {"fm": fm, "items": items, "quals": quals, "path": p}
    return cards


def parse_sources(run):
    text = (Path(run) / "sources.md").read_text(encoding="utf-8")
    pages, keys, sec = [], [], None
    for line in text.splitlines():
        if line.startswith("## "):
            sec = line[3:].strip()
        m = re.match(r"^- `?(wiki/[\w\-/]+\.md)`?", line.strip())
        if m:
            pages.append(norm_wiki(m.group(1)))
        elif sec and sec.startswith("來源") and re.match(r"^- [\w\-]+\s*$", line.strip()):
            keys.append(line.strip()[2:].strip())
    return pages, keys


def parse_outline(run):
    """回傳 [{"n":int, "title":str, "evidence":[...], "wiki":[...]}]"""
    text = (Path(run) / "outline.md").read_text(encoding="utf-8")
    slides, cur = [], None
    for line in text.splitlines():
        m = re.match(r"^## Slide (\d+)[:：]\s*(.*)$", line)
        if m:
            cur = {"n": int(m.group(1)), "title": m.group(2).strip(), "evidence": [], "wiki": []}
            slides.append(cur)
            continue
        if cur is None:
            continue
        m = re.match(r"^- evidence[:：]\s*(.*)$", line.strip())
        if m:
            cur["evidence"] = [x.strip() for x in re.split(r"[,，]", m.group(1)) if x.strip() and x.strip() != "—"]
        m = re.match(r"^- wiki[:：]\s*(.*)$", line.strip())
        if m:
            cur["wiki"] = [norm_wiki(x) for x in re.split(r"[,，]", m.group(1)) if x.strip() and x.strip() != "—"]
    return slides


def parse_drafts(run):
    out = []
    for p in sorted((Path(run) / "drafts").glob("slide-*.md")):
        fm, body = parse_frontmatter(p.read_text(encoding="utf-8"))
        out.append({"path": p, "fm": fm, "body": body,
                    "n": int(fm.get("slide", re.findall(r"\d+", p.stem)[0]))})
    return sorted(out, key=lambda d: d["n"])
