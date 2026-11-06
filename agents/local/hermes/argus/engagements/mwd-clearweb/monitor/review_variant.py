import difflib
import glob
import hashlib
import re
import subprocess
import sys
from pathlib import Path

ENG = Path("/home/tribune2563/.hermes/profiles/argus/cache/engagements/mwd-clearweb")
BASE = sorted(glob.glob(str(ENG / "baseline_20*")))[-1]
baseline_html = Path(BASE, "body_www_mwdh2o_com_.html").read_bytes()


def visible(html_bytes):
    t = html_bytes.decode("utf-8", "replace")
    t = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", t)
    t = re.sub(r"(?s)<!--.*?-->", " ", t)
    t = re.sub(r"<[^>]+>", "\n", t)
    lines = [re.sub(r"\s+", " ", x).strip() for x in t.splitlines()]
    return [x for x in lines if x]


out = Path("/tmp/mwd_review_new.html")
url = sys.argv[1] if len(sys.argv) > 1 else "https://www.mwdh2o.com/"
subprocess.run(["curl", "-sS", "-m", "30", "-A", "Mozilla/5.0", "-L", "-o", str(out), url], check=True)
new_html = out.read_bytes()

old_lines = visible(baseline_html)
new_lines = visible(new_html)
print("visible-text sha (new):", hashlib.sha256("\n".join(new_lines).encode()).hexdigest()[:16])
print("visible lines baseline/new:", len(old_lines), len(new_lines))
print("== unified diff of visible text (baseline 2026-10-21 -> now)")
diff = list(difflib.unified_diff(old_lines, new_lines, "baseline", "now", n=0, lineterm=""))
print("\n".join(diff[:200]) if diff else "(no visible-text differences)")
print("== script/iframe/form hosts in new HTML")
t = new_html.decode("utf-8", "replace")
hosts = sorted(set(re.findall(r'(?:src|href|action)="https?://([^/"]+)', t)))
print(hosts)
print("inline script count new/baseline:", len(re.findall(r"<script(?![^>]*src)", t, re.I)),
      len(re.findall(r"<script(?![^>]*src)", baseline_html.decode("utf-8", "replace"), re.I)))
