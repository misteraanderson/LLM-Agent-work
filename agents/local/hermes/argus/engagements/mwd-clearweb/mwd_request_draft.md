# MWD request draft (not sent)

**Status:** Draft. Operator reviews and sends. Placeholders in brackets.
**Prepared:** 2026-11-06 (UTC)

---

**Subject:** Request for information to support clear-web monitoring of mwdh2o.com and bewaterwise.com

Hello [MWD contact],

As part of CAI's SOC monitoring contract with MWD, we run an automated check of MWD's public web assets for defacement and domain takeover. The check covers mwdh2o.com and bewaterwise.com. It uses public information only: DNS lookups, certificate transparency logs, and routine requests to the public sites.

We would appreciate the following:

1. **Homepage content rotation.** The mwdh2o.com homepage changes between runs, including a news carousel and the document-library search list. Could you share the list of current carousel slides and any sort or filter states the document list can show, so we can recognize them as expected?

2. **Change calendar.** Please share planned website changes, releases, and maintenance windows for these sites, so we can match alerts against known changes.

3. **Nameserver zone transfer (time-sensitive).** Our checks show that ns2.mwdh2o.com is serving older zone data than ns1.mwdh2o.com, for both zones:
   - bewaterwise.com: ns1 serial 2026020506, ns2 serial 2026020504 (checked 2026-11-06 14:21 UTC)
   - mwdh2o.com: ns1 serial 2026110424, ns2 serial 2026110403 (checked 2026-11-06 14:21 UTC)

   The public resolver currently returns the ns2 values for bewaterwise.com. This has persisted for several days, and the serial moves backward between queries. Please have your DNS team check the zone transfer from ns1 to ns2 and the NOTIFY settings. Records may differ depending on which server answers.

4. **Domain ownership.** Please confirm which of the following domains belong to MWD and should be included in monitoring:
   - mwdh20.com (operator states MWD-owned; we'd like MWD's confirmation as well)
   - bewaterwise.net, bewaterwise.org, bwaterwise.com, bwaterwise.net, bwaterwise.org
   - dvlake.com, mwdinnovates.com, mwdwatertomorrow.com
   - socalwaterdialogue.com, socalwaterdialogue.org
   - surveys.bewaterwise.com
   - the mwdsc.net names that appear in certificate transparency logs (owa, exchowa, esowa, nvowa, manage)

   We will monitor only the domains you confirm.

Please send a point of contact for follow-up. Thank you.

[Name]
[Title], CAI SOC, on contract to MWD
