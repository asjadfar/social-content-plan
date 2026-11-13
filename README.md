# Instagram / Facebook Content Plan Skill

A Claude skill for end-to-end social content planning for a store's Instagram and Facebook — built from Asjad's real week plans for Fragrance Empire. Claude handles all the work end to end — week brief, topics, captions (Facebook + Instagram versions), photographic image prompts, reel briefs, price checks, approval gate and posting checklist — with the owner involved only for approval of the exact text, image and time before anything posts, and for rendering the images and the reel clips on their own device.

## What it does

Takes a week of social content from brief to publish-ready in one repeatable workflow:

1. **Brief** — week dates, the current offer (or no offer), goals, products and bundles in focus, what is NOT allowed this week.
2. **Topics** — 14 article topics + 7 reel topics for the week, from a topic bank of what actually worked, no repeats within the week.
3. **Captions** — every post written twice: a Facebook version (direct shop link in the caption) and an Instagram version ("Link in bio", no URLs). Knowledge posts end with a question.
4. **Image prompts** — one standalone copyable photographic image prompt per article post, carrying the text-overlay rule. The owner renders them in ChatGPT; Claude never generates a tip-card.
5. **Reel briefs** — one per day, 15 seconds, 9:16 portrait, one product or bundle, hook in the first 5 seconds, end card for exactly 2 seconds.
6. **Price check** — every price in a caption verified live on the store before it is written in. No price from memory, ever.
7. **Approval gate** — nothing posts until the owner approves the exact text + image + time. A changed caption, price or image needs fresh approval.
8. **Posting + verification** — post or schedule per platform, then verify live and report the links. A scheduled post and a live post are different states — report which one it is.
9. **Week review** — followers, comments, link clicks, what to change next week.

## Who does what — Claude handles all the work end to end

Claude runs every step — brief, topics, captions, image prompts, reel briefs, price checks, approval gate, posting checklist and week review. The owner is involved only at three points: (1) week decisions only the owner can make (the current offer, sale dates, which products to push, what is not allowed); (2) rendering — the owner generates the article images in ChatGPT from Claude's prompts and the reel clips in Flow, because image/video generation is region-unavailable on the owner's Muse account; and (3) approval of the exact text, image and time for every post before it goes out. Everything else is Claude's work — do not hand it back to the owner as homework.

## The accounts

- **Instagram:** @fragranceempire.my — all posts in English; captions carry no URLs ("Link in bio"); feed images portrait 4:5 (1080×1350); every video needs a matching cover image.
- **Facebook Page:** Fragrance Empire (https://www.facebook.com/people/Fragrance-Empire/61596175737426/) — captions carry the direct shop link; Page post text limit is 1,024 characters via the connector.
- **Store:** Fragrance Empire, https://fragranceempire.my — every price in a caption is verified live here first.

## The rhythm (Malaysia time, MYT)

- **12:00pm MYT (9am PKT) — Article + picture #1**
- **3:00pm MYT (12pm PKT) — Article + picture #2**
- **7:00pm MYT (4pm PKT) — Reel of the day**

That is 14 articles + 7 reels = 21 posts for the week.

## Files

```
social-content-plan/
├── README.md                                  # this file
└── social-content-plan/
    ├── SKILL.md                               # the Claude skill — the workflow itself
    ├── scripts/
    │   └── check_captions.py                  # caption + image-prompt checker (length, links, hashtags, overlay rule)
    └── templates/
        ├── week-plan.md                       # blank one-week plan template
        ├── caption-template.md                # Facebook + Instagram caption templates
        ├── image-prompt-template.md           # photographic image-prompt template + worked examples
        └── reel-brief-template.md             # 7pm reel brief template
```

## Setup

### 1. Accounts first

The Instagram account and Facebook Page must already exist and be connected. The skill cannot create them, and it cannot pick the accounts — that is the owner's decision.

### 2. Choose a posting route (one per platform)

**Facebook — connector (Page posts).** Post or schedule through the Page connector with the owner's approval. Only `state: published` confirms a post went live; `state: scheduled` + a scheduled post ID confirms a schedule. To change a scheduled post's media or text, cancel the schedule, edit the draft, then publish or re-schedule. There is no list-scheduled-posts command — keep the post IDs in the week-plan file.

**Instagram — app or timed publish job.** Instagram scheduling is NOT available via the connector (HTTP 403 — do not retry it). Schedule in the Instagram app, or use a timed publish job that posts at the slot time. Every video needs a matching cover image, and feed images are portrait 4:5 (1080×1350).

Do not use any other posting route. Do not paste API keys, passwords or credentials into the skill files, into chat, or into the repo — credentials live only in the owner's secure storage / sign-in flow.

### 3. Images

Article images are rendered by the owner in ChatGPT from Claude's prompts. The skill writes the prompts as standalone copyable text — one per post — and the owner sends the finished image back. Claude never generates a tip-card image and never asks the owner to use one.

### 4. Use in Claude

Copy the `social-content-plan/` folder into a Claude skills directory (for example a Claude Code skills folder, or a repo Claude is pointed at), or keep this whole repo and point Claude at `social-content-plan/SKILL.md`. Then ask Claude to run the workflow, for example: "Make next week's content plan for Fragrance Empire using the social-content-plan skill."

## Honest limits — read before using

- **No direct Instagram scheduling.** The connector returns HTTP 403 for scheduled Instagram posts. Schedule in the IG app or with a timed publish job. Timed jobs can run late — expect possible lateness and verify live before reporting a post as done.
- **Image and video generation is region-unavailable on the owner's Muse account.** The skill does not promise that Muse/Claude can generate the article images or reel clips itself. Images come from ChatGPT (by the owner, from Claude's prompts) and reel clips from Flow (by the owner), then Claude checks and schedules them.
- **No credentials in the skill.** No API keys, passwords or secrets are stored in these files. If a step needs a login, the owner does it on their own device.
- **Approval gate is mandatory.** Nothing is posted or scheduled until the owner approves the exact text, image and time. A changed caption, price or image needs fresh approval.
- **Prices are verified live, never from memory.** A price in a caption that was not checked on the store that week is a blocker, not a guess.
- **A publish call that returns only an ID (or times out) may still have published.** After any uncertain result, verify via the post lookup before retrying or reporting — never post twice.

## How to run one week

1. Fill in the brief (Step 1) and get the owner to confirm it.
2. Pick the week's 14 article topics + 7 reel topics (Step 2).
3. Write every caption twice — Facebook + Instagram — using `templates/caption-template.md` (Step 3).
4. Write one image prompt per article post (Step 4) and one reel brief per day (Step 5).
5. Verify every price live on the store (Step 6).
6. Run `scripts/check_captions.py` on the plan until it passes.
7. Fill in `templates/week-plan.md` and get the owner's approval for the exact text + image + time of every post (Step 7).
8. Post or schedule per platform, verify each post live, and record the links in the plan (Step 8).
9. At the end of the week, do the week review (Step 9) and note one change for next week.
