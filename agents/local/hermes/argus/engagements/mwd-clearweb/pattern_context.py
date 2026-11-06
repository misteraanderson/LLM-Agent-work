import re, sys
path = sys.argv[1]
text = open(path, encoding="utf-8", errors="replace").read()
pat = re.compile(r"atob\(|eval\(|base64", re.I)
seen = 0
for m in pat.finditer(text):
    s = max(0, m.start() - 90)
    e = min(len(text), m.end() + 90)
    ctx = text[s:e].replace("\n", " ").replace("\r", " ")
    print(f"[{m.group(0)}] @{m.start()}: {ctx}")
    print("---")
    seen += 1
    if seen >= 25:
        break
print("total matches:", len(pat.findall(text)))
