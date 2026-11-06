# Engagement: MWD clear-web monitoring

**Date recorded:** 2026-10-27 (as stated by operator)
**Operator:** Anthony, Technical Team Lead (CAI job title; functions as SOC Manager for the MWD SOC team), CAI, under contract to Metropolitan Water District of Southern California (MWD)

## Purpose (operator statement, verbatim)

> ARGUS is authorized to monitor MWD's public-facing web assets for signs of defacement and domain takeover using publicly available information ONLY (OSINT). This is to assist the operator in his duties as Technical Team Lead for CAI's SOC team on contract to Metropolitan Water District of Southern California. ARGUS is to monitor MWD's domains only and none other. If ARGUS finds a new domain via publicly available means, it is to notify the operator and wait for approval before monitoring it.

## Approved domains (monitoring)

- mwdh2o.com (apex and www)
- bewaterwise.com (apex and www)

## Pending approval (do not monitor until operator approves)

- mwdh20.com (operator states MWD-owned; ownership not independently verified)
- Certificate-SAN domains found on bewaterwise.com and mwdh2o.com certificates: bewaterwise.net, bewaterwise.org, bwaterwise.com, bwaterwise.net, bwaterwise.org, dvlake.com, mwdinnovates.com, mwdwatertomorrow.com, socalwaterdialogue.com, socalwaterdialogue.org, surveys.bewaterwise.com, and the mwdsc.net names
- Any other domain or subdomain discovered during monitoring

## Authorized actions

- Passive lookups: DNS, RDAP, certificate transparency (certspotter), public search indexes.
- Routine unauthenticated HTTP GET requests to the approved domains' public pages, and TLS handshake to port 443 (daily check).

## Not authorized without separate approval

- Port scans, crawling, form submissions, login attempts, authenticated access.
- On-demand scans or submissions to Shodan, Censys, or similar services.
- Any request to MWD staff, systems, or contacts (the operator makes all contact).
- Dark web collection (tabled).
- Use of leaked or discovered credentials, purchases, or contact with threat actors.

## Clarification (operator, 2026-10-27)

Routine unauthenticated requests to MWD's public sites (HTTP GET, TLS handshake) and standard DNS queries are treated as publicly available information. Any member of the public can reach these sites at any time, so they are within "publicly available information ONLY." They remain limited to the approved domains and the authorized actions above.

## Data handling

- Engagement data stays in this folder. No copies leave the host without written approval for the destination service.
- Credentials (Shodan key) are held only in the profile's `.env` file.

## Monitoring policy change (operator-approved, 2026-11-06)

- Visible-text hash changes on the mwdh2o.com and bewaterwise.com homepages are informational only (carousel and document-library state).
- Alerting is keyed on the external host set and inline-script count referenced by each page, plus DNS, RDAP, TLS, CT, and status/final-URL changes.
- The first run after this change shows the new host and script fields as ALERT because the previous snapshot predates them. Expect no alert from the next run if the host set is unchanged.

## Visual review policy (operator-approved, 2026-11-06)

- Routine daily checks are script-based (HTTP, DNS, RDAP, TLS, CT, host set). They do not use the Bot Screen.
- Bot Screen visual review (Firefox on the bot display, captures and scrolling) runs only when a daily check reports an ALERT, to see exactly what changed.
- Bot Screen review uses only the approved domains. Stop and ask the operator on any login, CAPTCHA, or 2FA prompt.
- Captures are saved to monitor/screens/ with SHA-256 entries in hashes.txt.
