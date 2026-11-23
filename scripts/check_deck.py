"""渲染檢查（graph 節點 G4 的程式檢查部分）。

用法：python scripts/check_deck.py <run_dir> [--no-browser] [--screenshots]
檢查：
  1. 頁數 8–15
  2. 每頁頁尾有 wiki 出處（data-wiki）、出處頁存在、有頁碼「n / total」
  3. 忠於逐頁稿：每頁標題＋內文的文字與 drafts/ 完全一致（渲染節點不能改字）
  4. 無文字溢出：用 headless Chrome 以 1280×720 實際排版，量測 .content 的 scrollHeight/scrollWidth
     與每個子元素是否超出內容框（Chrome 找不到時退回字數／行數上限，並在輸出註明）
  5. 鍵盤翻頁：在 headless Chrome 內送出 ArrowRight / ArrowLeft，確認頁碼真的改變
  --screenshots：另外把每一頁截圖存到 <run_dir>/screenshots/，供人工與 AI 檢視
exit code：0 = PASS，1 = FAIL
"""
import argparse
import html
import json
import os
import re
import shutil
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import parse_drafts, wiki_path  # noqa: E402

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "/usr/bin/google-chrome", "/usr/bin/chromium", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
]
FALLBACK_MAX_CHARS = 260  # 無瀏覽器時的字數上限（標題＋內文）
FALLBACK_MAX_LINES = 12

MEASURE_JS = r"""
<script>
window.addEventListener('load', function () {
  var res = [], slides = document.querySelectorAll('.slide');
  document.getElementById('deck').style.transform = 'none';
  slides.forEach(function (s, i) {
    slides.forEach(function (x) { x.classList.remove('active'); });
    s.classList.add('active'); s.classList.add('reveal');
    var c = s.querySelector('.content'), cr = c.getBoundingClientRect(), over = [];
    if (c.scrollHeight > c.clientHeight + 1) over.push('內容高度 ' + c.scrollHeight + 'px > 可用 ' + c.clientHeight + 'px');
    if (c.scrollWidth > c.clientWidth + 1) over.push('內容寬度 ' + c.scrollWidth + 'px > 可用 ' + c.clientWidth + 'px');
    c.querySelectorAll('*').forEach(function (el) {
      var r = el.getBoundingClientRect();
      if (r.width && (r.bottom > cr.bottom + 1 || r.right > cr.right + 1))
        over.push(el.tagName.toLowerCase() + (el.className ? '.' + el.className : '') + ' 超出 ' +
                  Math.max(Math.round(r.bottom - cr.bottom), Math.round(r.right - cr.right)) + 'px');
    });
    var f = s.querySelector('footer');
    if (f && f.scrollWidth > f.clientWidth + 1) over.push('頁尾寬度溢出');
    res.push({ n: i + 1, overflow: over.slice(0, 4), used: c.scrollHeight, cap: c.clientHeight });
    s.classList.remove('reveal');
  });
  window.__deck.show(0);
  document.dispatchEvent(new KeyboardEvent('keydown', { key: 'ArrowRight' }));
  var a = window.__deck.current();
  document.dispatchEvent(new KeyboardEvent('keydown', { key: 'ArrowLeft' }));
  var b = window.__deck.current();
  var pre = document.createElement('pre'); pre.id = '__measure';
  pre.textContent = JSON.stringify({ slides: res, key: { afterRight: a, afterLeft: b } });
  document.body.appendChild(pre);
});
</script>
"""


class TextOf(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        cls = dict(attrs).get("class", "")
        if tag in ("footer", "script", "style") or "kicker" in cls or "arrow" in cls or self.skip:
            self.skip += 1

    def handle_endtag(self, tag):
        if self.skip:
            self.skip -= 1

    def handle_data(self, d):
        if not self.skip:
            self.parts.append(d)


def norm(s):
    return re.sub(r"[^\w\u4e00-\u9fff]", "", s).replace("_", "")


def draft_plain(title, body):
    body = re.sub(r"(?m)^```\w*\s*$", "", body)
    body = re.sub(r"(?m)^\s*(?:[-*]|\d+\.)\s+", "", body)
    body = re.sub(r"(?m)^\s*Q[:：]\s*", "", body)
    body = re.sub(r"\|\|\s*A[:：]\s*", " ", body)
    return norm(title + body)


def find_chrome():
    for c in CHROME_CANDIDATES:
        if Path(c).exists():
            return c
    return shutil.which("chrome") or shutil.which("google-chrome") or shutil.which("chromium")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("run")
    ap.add_argument("--no-browser", action="store_true")
    ap.add_argument("--screenshots", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    run = Path(a.run).resolve()
    deck = (run / "deck.html").read_text(encoding="utf-8")
    sections = re.findall(r'<section class="slide[^"]*" data-n="(\d+)" data-wiki="([^"]*)">(.*?)</section>', deck, re.S)
    errs, info = [], []
    total = len(sections)
    info.append(f"頁數：{total}")
    if not 8 <= total <= 15:
        errs.append(f"頁數 {total} 不在 8–15")

    drafts = {d["n"]: d for d in parse_drafts(run)}
    for n, wiki, inner in sections:
        n = int(n)
        wl = [w for w in html.unescape(wiki).split(",") if w]
        if not wl:
            errs.append(f"slide {n}: 頁尾沒有 wiki 出處")
        for w in wl:
            if not wiki_path(w).exists():
                errs.append(f"slide {n}: 頁尾出處 wiki/{w} 不存在")
        if f"{n} / {total}" not in inner:
            errs.append(f"slide {n}: 沒有頁碼「{n} / {total}」")
        d = drafts.get(n)
        if not d:
            errs.append(f"slide {n}: 找不到對應的 drafts/slide-{n:02d}.md")
            continue
        p = TextOf()
        p.feed(inner)
        if norm("".join(p.parts)) != draft_plain(d["fm"].get("title", ""), d["body"]):
            errs.append(f"slide {n}: 渲染後文字與逐頁稿不一致（渲染節點不能改字）")
        if set(wl) != set(d["fm"].get("wiki") or []):
            errs.append(f"slide {n}: 頁尾出處與逐頁稿 frontmatter 不一致")
    if set(drafts) != {int(s[0]) for s in sections}:
        errs.append(f"逐頁稿頁碼 {sorted(drafts)} 與簡報頁碼不一致")

    chrome = None if a.no_browser else find_chrome()
    work = run / ".check"
    if chrome:
        work.mkdir(exist_ok=True)
        m = work / "measure.html"
        m.write_text(deck.replace("</body>", MEASURE_JS + "</body>"), encoding="utf-8")
        prof = work / "profile"
        cmd = [chrome, "--headless=new", "--disable-gpu", f"--user-data-dir={prof}", "--window-size=1320,760",
               "--virtual-time-budget=4000", "--dump-dom", m.as_uri()]
        r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", timeout=120)
        mm = re.search(r'<pre id="__measure">(.*?)</pre>', r.stdout, re.S)
        if not mm:
            errs.append("headless Chrome 量測失敗（沒有取得量測結果）")
        else:
            data = json.loads(html.unescape(mm.group(1)))
            info.append("溢出量測：headless Chrome，1280×720 實際排版")
            for s in data["slides"]:
                info.append(f"  slide {s['n']:2d}: 內容高度 {s['used']}/{s['cap']}px")
                for o in s["overflow"]:
                    errs.append(f"slide {s['n']}: 溢出 — {o}")
            k = data["key"]
            info.append(f"鍵盤翻頁：→ 後在第 {k['afterRight'] + 1} 頁、← 後回到第 {k['afterLeft'] + 1} 頁")
            if not (k["afterRight"] == 1 and k["afterLeft"] == 0):
                errs.append("鍵盤左右鍵翻頁沒有作用")
        if a.screenshots:
            shots = run / "screenshots"
            shots.mkdir(exist_ok=True)
            # headless 的實際 viewport 與 --window-size 不一致，截圖時把簡報固定在左上角、縮放 1
            shot = work / "shot.html"
            shot.write_text(deck.replace("</head>", "<style>#stage{position:static;display:block}"
                                         "#deck{transform:none!important;position:absolute!important;left:0;top:0}"
                                         "body{overflow:hidden}.slide{border-radius:0;box-shadow:none}"
                                         "#hint,#progress{display:none}</style></head>"), encoding="utf-8")
            for n, _, _ in sections:
                out = shots / f"slide-{int(n):02d}.png"
                subprocess.run([chrome, "--headless=new", "--disable-gpu", f"--user-data-dir={prof}",
                                "--window-size=1280,720", "--hide-scrollbars", "--virtual-time-budget=2000",
                                f"--screenshot={out}", shot.as_uri() + f"#{int(n)}"],
                               capture_output=True, timeout=120)
            info.append(f"截圖：{shots}（{len(sections)} 張）")
        shutil.rmtree(prof, ignore_errors=True)
    else:
        info.append(f"⚠️ 找不到 Chrome/Edge，改用字數（≤{FALLBACK_MAX_CHARS}）與行數（≤{FALLBACK_MAX_LINES}）上限近似溢出檢查")
        for n, d in drafts.items():
            chars = len(draft_plain(d["fm"].get("title", ""), d["body"]))
            lines = len([x for x in d["body"].splitlines() if x.strip()])
            if chars > FALLBACK_MAX_CHARS or lines > FALLBACK_MAX_LINES:
                errs.append(f"slide {n}: {chars} 字、{lines} 行，超過上限")
        if "ArrowRight" not in deck or "ArrowLeft" not in deck:
            errs.append("deck.html 沒有左右鍵翻頁")

    print("\n".join(info))
    if errs:
        print(f"FAIL（{len(errs)}）")
        for e in errs:
            print(f"- {e}")
        sys.exit(1)
    print("PASS")


if __name__ == "__main__":
    main()
