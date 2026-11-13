#!/usr/bin/env python3
"""Caption + image-prompt checker for the social-content-plan skill.

Checks captions and image prompts against the skill's hard rules before
the approval gate. Stdlib only.

Usage:
  # One caption file (one caption per file, plain text):
  python3 check_captions.py --caption caption-fb.txt --platform fb
  python3 check_captions.py --caption caption-ig.txt --platform ig --knowledge
  python3 check_captions.py --caption caption-fb.txt --platform fb --sale

  # A whole week-plan file (templates/week-plan.md format):
  python3 check_captions.py --plan week-plan.md [--sale]

  # One image prompt file (one prompt per file, plain text):
  python3 check_captions.py --prompt image-prompt.txt

In --plan mode, captions are read from lines like:
  - **Caption (FB):** <exact caption text>
  - **Caption (IG):** <exact caption text>
and image prompts from lines like:
  - **Image prompt:** <exact prompt text>
Write each caption and each prompt on ONE line in the plan file.

Checks (FAIL = blocks the approval gate, WARN = fix if you can):
  Facebook caption:
    - length <= 1,024 characters (connector limit)           [FAIL]
    - contains the direct shop link (fragranceempire.my)     [FAIL]
    - at least 1 hashtag, at most 5                            [FAIL]
  Instagram caption:
    - contains NO URL (no http/https/www.)                    [FAIL]
    - contains "Link in bio"                                  [FAIL]
    - at least 1 hashtag, at most 5                            [FAIL]
  Both platforms:
    - no "100% original" unless --allow-original is given     [FAIL]
    - knowledge post ends with a question (--knowledge)        [FAIL with flag, WARN without]
    - sale week (--sale): offer block present ("OFF" + end)    [WARN]
  Image prompt:
    - starts with "Photographic" (tip-card guard)             [FAIL]
    - contains "CHOOSE LUXURY"                                [FAIL]
    - contains "fragranceempire.my"                           [FAIL]
    - contains "metallic gold 3D"                             [FAIL]
    - ends with "No other text"                               [FAIL]
    - contains "tip-card" / "tip card"                        [FAIL]

Exit code 0 when everything passes, 1 when any FAIL is found.
"""

import argparse
import re
import sys

FB_MAX_CHARS = 1024
SHOP_DOMAIN = "fragranceempire.my"
URL_RE = re.compile(r"https?://|www\.", re.IGNORECASE)
HASHTAG_RE = re.compile(r"#\w+")
CAPTION_FB_RE = re.compile(r"^\s*-\s*\*\*Caption \(FB\):\*\*\s*(.*)$")
CAPTION_IG_RE = re.compile(r"^\s*-\s*\*\*Caption \(IG\):\*\*\s*(.*)$")
PROMPT_RE = re.compile(r"^\s*-\s*\*\*Image prompt:\*\*\s*(.*)$")


def check_caption(text, platform, knowledge=False, sale=False, allow_original=False):
    """Check one caption. Returns a list of (level, message) tuples."""
    problems = []
    label = f"{platform.upper()} caption"

    if platform == "fb":
        if len(text) > FB_MAX_CHARS:
            problems.append(("FAIL", f"{label}: {len(text)} characters — over the "
                             f"{FB_MAX_CHARS} limit by {len(text) - FB_MAX_CHARS}"))
        if SHOP_DOMAIN not in text:
            problems.append(("FAIL", f"{label}: no direct shop link "
                             f"({SHOP_DOMAIN}) — Facebook captions must link to the shop"))
    elif platform == "ig":
        if URL_RE.search(text):
            problems.append(("FAIL", f"{label}: contains a URL — Instagram captions "
                             "must have no URLs"))
        if "link in bio" not in text.lower():
            problems.append(("FAIL", f"{label}: no 'Link in bio' — Instagram captions "
                             "must say 'Link in bio' instead of a link"))

    tags = HASHTAG_RE.findall(text)
    if not tags:
        problems.append(("FAIL", f"{label}: no hashtags — add 3-4 "
                         "(#FragranceEmpire #PerfumeTips #PerfumeMalaysia #LuxuryPerfume)"))
    elif len(tags) > 5:
        problems.append(("FAIL", f"{label}: {len(tags)} hashtags — at most 5 allowed"))

    if not allow_original and "100% original" in text.lower():
        problems.append(("FAIL", f"{label}: contains '100% original' — never write an "
                         "authenticity promise unless the owner explicitly approved it"))

    # Knowledge posts should end the knowledge part with a question. The
    # question sits before the offer block and the link line, so check that
    # a "?" appears in the text before the link marker — not that the body
    # ends with "?" (the offer block follows the question in real captions).
    body = text
    for marker in ("Shop now:", "Link in bio", "https://"):
        idx = body.find(marker)
        if idx != -1:
            body = body[:idx]
            break
    body = body.strip()
    if body and "?" not in body:
        msg = f"{label}: no question in the caption before the link — knowledge posts end with a question"
        problems.append(("FAIL" if knowledge else "WARN", msg))

    if sale and "OFF" not in text:
        problems.append(("WARN", f"{label}: --sale given but no offer block ('OFF') found"))

    return problems


def check_prompt(text):
    """Check one image prompt. Returns a list of (level, message) tuples."""
    problems = []
    label = "Image prompt"

    if not text.startswith("Photographic"):
        problems.append(("FAIL", f"{label}: does not start with 'Photographic' — "
                         "article images are photographic, never tip-cards"))
    if "tip-card" in text.lower() or "tip card" in text.lower():
        problems.append(("FAIL", f"{label}: mentions a tip-card — never write tip-card prompts"))
    if "CHOOSE LUXURY" not in text:
        problems.append(("FAIL", f"{label}: missing 'CHOOSE LUXURY' (text-overlay rule)"))
    if SHOP_DOMAIN not in text:
        problems.append(("FAIL", f"{label}: missing '{SHOP_DOMAIN}' (text-overlay rule)"))
    if "metallic gold 3D" not in text:
        problems.append(("FAIL", f"{label}: missing 'metallic gold 3D' (text-overlay rule)"))
    if not text.rstrip().endswith("No other text."):
        problems.append(("FAIL", f"{label}: must end with 'No other text.' (text-overlay rule)"))
    return problems


def check_plan(path, sale=False, allow_original=False):
    """Scan a week-plan file for captions and image prompts. Returns problems."""
    problems = []
    try:
        lines = open(path, encoding="utf-8").read().splitlines()
    except OSError as exc:
        return [("FAIL", f"Cannot read plan file {path}: {exc}")]

    found = 0
    for lineno, line in enumerate(lines, 1):
        m = CAPTION_FB_RE.match(line)
        if m:
            found += 1
            text = m.group(1).strip()
            if text.startswith("["):
                problems.append(("WARN", f"Line {lineno}: FB caption is still a "
                                "placeholder — fill it in before the approval gate"))
                continue
            for level, msg in check_caption(text, "fb", sale=sale,
                                            allow_original=allow_original):
                problems.append((level, f"Line {lineno}: {msg}"))
            continue
        m = CAPTION_IG_RE.match(line)
        if m:
            found += 1
            text = m.group(1).strip()
            if text.startswith("["):
                problems.append(("WARN", f"Line {lineno}: IG caption is still a "
                                "placeholder — fill it in before the approval gate"))
                continue
            for level, msg in check_caption(text, "ig", sale=sale,
                                            allow_original=allow_original):
                problems.append((level, f"Line {lineno}: {msg}"))
            continue
        m = PROMPT_RE.match(line)
        if m:
            found += 1
            text = m.group(1).strip()
            if text.startswith("["):
                problems.append(("WARN", f"Line {lineno}: image prompt is still a "
                                "placeholder — fill it in before the approval gate"))
                continue
            for level, msg in check_prompt(text):
                problems.append((level, f"Line {lineno}: {msg}"))

    if found == 0:
        problems.append(("FAIL", f"No captions or image prompts found in {path} — "
                         "use the templates/week-plan.md line format"))
    return problems


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--caption", help="File with one caption (plain text)")
    parser.add_argument("--platform", choices=["fb", "ig"],
                        help="Platform for --caption (fb or ig)")
    parser.add_argument("--prompt", help="File with one image prompt (plain text)")
    parser.add_argument("--plan", help="Week-plan markdown file to scan")
    parser.add_argument("--knowledge", action="store_true",
                        help="Caption is a knowledge post: ending question is required")
    parser.add_argument("--sale", action="store_true",
                        help="Sale week: warn if the offer block is missing")
    parser.add_argument("--allow-original", action="store_true",
                        help="Owner explicitly approved a '100% original' claim")
    args = parser.parse_args(argv)

    if not args.caption and not args.prompt and not args.plan:
        parser.error("Give one of --caption, --prompt or --plan")
    if args.caption and not args.platform:
        parser.error("--caption needs --platform fb or ig")

    problems = []
    if args.caption:
        try:
            text = open(args.caption, encoding="utf-8").read().strip()
        except OSError as exc:
            problems.append(("FAIL", f"Cannot read caption file: {exc}"))
        else:
            problems += check_caption(text, args.platform, knowledge=args.knowledge,
                                      sale=args.sale, allow_original=args.allow_original)
    if args.prompt:
        try:
            text = open(args.prompt, encoding="utf-8").read().strip()
        except OSError as exc:
            problems.append(("FAIL", f"Cannot read prompt file: {exc}"))
        else:
            problems += check_prompt(text)
    if args.plan:
        problems += check_plan(args.plan, sale=args.sale,
                               allow_original=args.allow_original)

    fails = [m for lvl, m in problems if lvl == "FAIL"]
    warns = [m for lvl, m in problems if lvl == "WARN"]
    for level, msg in problems:
        print(f"{level}: {msg}")
    print(f"\n{len(fails)} FAIL, {len(warns)} WARN")
    if fails:
        print("FAIL: plan is not ready for the approval gate.")
        return 1
    print("PASS: all checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
