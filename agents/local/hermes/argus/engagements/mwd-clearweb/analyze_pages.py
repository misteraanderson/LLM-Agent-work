import json, glob, re, hashlib, os, sys

base = sys.argv[1]
os.chdir(base)

print("== HEADERS (final response per URL)")
for h in sorted(glob.glob("hdr_*.txt")):
    txt = open(h, encoding="utf-8", errors="replace").read()
    blocks = [b for b in re.split(r"\r?\n\r?\n", txt) if b.strip()]
    last = blocks[-1]
    print("--", h)
    for line in last.splitlines():
        if re.match(r"(?i)^(HTTP/|server|content-type|content-length|last-modified|date|strict-transport|content-security|x-frame|x-content-type|referrer-policy|permissions-policy|set-cookie|cf-ray|cf-cache|alt-svc|x-powered|via|location)", line):
            print("  ", line[:220])
    print("   all header names:", sorted({l.split(":")[0].lower() for l in last.splitlines() if ":" in l}))

print("\n== BODIES")
for b in sorted(glob.glob("body_*.html")):
    data = open(b, "rb").read()
    text = data.decode("utf-8", errors="replace")
    print("--", b, "bytes:", len(data), "sha256:", hashlib.sha256(data).hexdigest())
    t = re.search(r"<title[^>]*>(.*?)</title>", text, re.S | re.I)
    print("   title:", (t.group(1).strip() if t else None))
    print("   meta generator:", re.findall(r'<meta[^>]+name="generator"[^>]+content="([^"]+)"', text, re.I)[:3])
    print("   script src hosts:")
    hosts = {}
    for m in re.finditer(r'<script[^>]+src="(https?:)?//?([^/"]+)', text, re.I):
        hosts[m.group(2)] = hosts.get(m.group(2), 0) + 1
    for h, c in sorted(hosts.items(), key=lambda x: -x[1])[:20]:
        print("     ", c, h)
    print("   inline <script> count:", len(re.findall(r"<script(?![^>]+src)", text, re.I)))
    print("   iframes:", re.findall(r'<iframe[^>]+src="([^"]+)"', text, re.I)[:10])
    print("   forms actions:", re.findall(r'<form[^>]+action="([^"]+)"', text, re.I)[:10])
    print("   meta refresh:", re.findall(r'<meta[^>]+http-equiv="refresh"[^>]*>', text, re.I)[:3])
    print("   canonical:", re.findall(r'<link[^>]+rel="canonical"[^>]+href="([^"]+)"', text, re.I)[:2])
    print("   external href domains (top 15):")
    doms = {}
    for m in re.finditer(r'href="https?://([^/"]+)', text, re.I):
        doms[m.group(1)] = doms.get(m.group(1), 0) + 1
    for d, c in sorted(doms.items(), key=lambda x: -x[1])[:15]:
        print("     ", c, d)
    print("   base64/eval/atob hits:", len(re.findall(r"atob\(|eval\(|base64", text, re.I)))
    print("   hidden elements:", len(re.findall(r'style="[^"]*display\s*:\s*none', text, re.I)))

print("\n== CERTSPOTTER")
for f in sorted(glob.glob("baseline_latest_cs_*.json")):
    pass
