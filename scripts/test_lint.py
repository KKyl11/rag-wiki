"""lint_wiki.py 的自我測試：故意埋入每一種錯誤，確認 lint 真的抓得到。

用法：python scripts/test_lint.py
做法：把 wiki/、raw/、AGENTS.md、lint_wiki.py 複製到暫存資料夾，每個案例改壞一處，跑 lint，檢查輸出含對應代號。
"""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def setup(tmp):
    shutil.copytree(ROOT / "wiki", tmp / "wiki")
    shutil.copytree(ROOT / "raw", tmp / "raw")
    shutil.copy(ROOT / "AGENTS.md", tmp / "AGENTS.md")
    (tmp / "scripts").mkdir()
    shutil.copy(ROOT / "scripts" / "lint_wiki.py", tmp / "scripts" / "lint_wiki.py")


def append(path, text):
    p = Path(path)
    p.write_text(p.read_text(encoding="utf-8") + text, encoding="utf-8")


def replace(path, old, new):
    p = Path(path)
    t = p.read_text(encoding="utf-8")
    assert old in t, old
    p.write_text(t.replace(old, new, 1), encoding="utf-8")


CASES = {
    "(a) 斷連結": ("(a)", lambda t: append(t / "wiki/concepts/rag.md", "\n- [壞連結](nope.md) [src: lewis2020, p.1]\n")),
    "(b) 孤兒頁": ("(b)", lambda t: (
        (t / "wiki/concepts/orphan.md").write_text(
            "---\ntype: concept\ntitle: x\nsources: [lewis2020]\nupdated: 2026-11-23\n---\n\n句子。[src: lewis2020, p.1]\n", encoding="utf-8"),
        append(t / "wiki/index.md", "\n- [orphan](concepts/orphan.md) — x\n"))),
    "(c) 無出處段落": ("(c)", lambda t: append(t / "wiki/concepts/rag.md", "\n這是一段沒有出處的句子。\n")),
    "(d) key 不存在": ("(d)", lambda t: append(t / "wiki/concepts/rag.md", "\n- 句子。[src: nobody2099, p.1]\n")),
    "(d) 頁碼超出": ("(d)", lambda t: append(t / "wiki/concepts/rag.md", "\n- 句子。[src: lewis2020, p.999]\n")),
    "(d) 網頁小節不存在": ("(d)", lambda t: append(t / "wiki/concepts/rag.md", "\n- 句子。[src: anthropic2024, §不存在的小節]\n")),
    "(e) 未列入 index": ("(e)", lambda t: replace(t / "wiki/index.md", "(concepts/chunking.md)", "(concepts/rag.md)")),
    "(f) 矛盾區塊單一來源": ("(f)", lambda t: append(t / "wiki/concepts/rag.md", "\n> ⚖️ 矛盾：測試\n> - A [src: lewis2020, p.1]\n> - B [src: lewis2020, p.2]\n")),
    "(g) frontmatter 缺欄位": ("(g)", lambda t: replace(t / "wiki/concepts/rag.md", "updated: 2026-11-23\n", "")),
    "(h) 教學比喻含數字": ("(h)", lambda t: append(t / "wiki/concepts/rag.md", "\n> 🎓 教學比喻（非來源內容）：像一間有 3 層樓的圖書館\n")),
    "(j) 數字不在 raw 頁": ("(j)", lambda t: append(t / "wiki/concepts/rag.md", "\n- 檢索 9876 篇文件。[src: lewis2020, p.4]\n")),
    "(i) AGENTS.md 太長": ("(i)", lambda t: append(t / "AGENTS.md", "x" * 13000)),
}


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    failed = 0
    # 基準：未改動時應 PASS
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        setup(tmp)
        r = subprocess.run([sys.executable, str(tmp / "scripts/lint_wiki.py"), "--report", str(tmp / "r.md")],
                           capture_output=True, text=True, encoding="utf-8")
        ok = r.returncode == 0
        print(f"{'OK ' if ok else 'BAD'} 基準（未改動）應 PASS → exit {r.returncode}")
        failed += not ok
    for name, (code, mutate) in CASES.items():
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            setup(tmp)
            mutate(tmp)
            r = subprocess.run([sys.executable, str(tmp / "scripts/lint_wiki.py"), "--report", str(tmp / "r.md")],
                               capture_output=True, text=True, encoding="utf-8")
            ok = r.returncode == 1 and f"| {code} |" in r.stdout
            print(f"{'OK ' if ok else 'BAD'} {name} → exit {r.returncode}, 抓到 {code}: {f'| {code} |' in r.stdout}")
            failed += not ok
    print(f"\n{len(CASES) + 1 - failed}/{len(CASES) + 1} 通過")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
