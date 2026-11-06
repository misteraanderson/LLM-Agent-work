import json, sys, glob

def vcard_val(ent, key):
    va = ent.get("vcardArray")
    if not va or len(va) < 2:
        return None
    for item in va[1]:
        if item[0] == key:
            return item[3] if key != "adr" else item[3]
    return None

for path in sorted(glob.glob(sys.argv[1])):
    j = json.load(open(path))
    print("==", path)
    print("ldhName:", j.get("ldhName"))
    print("status:", j.get("status"))
    for e in j.get("events", []):
        print("event:", e.get("eventAction"), e.get("eventDate"))
    print("nameservers:", [n.get("ldhName") for n in j.get("nameservers", [])])
    print("dnssec:", j.get("secureDNS", {}).get("delegationSigned"))
    for ent in j.get("entities", []):
        print("entity roles:", ent.get("roles"), "| fn:", vcard_val(ent, "fn"), "| org:", vcard_val(ent, "org"))
        for sub in ent.get("entities", []):
            print("   sub roles:", sub.get("roles"), "| fn:", vcard_val(sub, "fn"), "| org:", vcard_val(sub, "org"))
    for ent in j.get("entities", []):
        if "registrar" in ent.get("roles", []):
            for p in ent.get("publicIds", []):
                print("registrar IANA id:", p.get("identifier"))
    print("handle:", j.get("handle"))
