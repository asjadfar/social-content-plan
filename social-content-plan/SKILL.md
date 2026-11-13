---
name: social-content-plan
description: End-to-end Instagram and Facebook content planning for a store — Claude produces a complete one-week plan (14 articles + 7 reels) with captions in Facebook and Instagram versions, standalone photographic image prompts carrying the text-overlay rule, and 7pm reel briefs, with live price verification, a mandatory approval gate, and live verification after posting. Modeled on Fragrance Empire's real week plans (Nov 6–15, 2026) — rhythm 12pm article, 3pm article, 7pm reel (MYT), captions in English, Facebook direct shop link, Instagram "Link in bio", knowledge posts end with a question. Use when the user asks to plan, write or schedule a week of social posts, captions, image prompts or reels for a store's Instagram or Facebook.
---

# Instagram / Facebook Content Plan

## When to use

Use this skill when the user asks to plan a week of social content, write captions, write image prompts, brief a reel, or schedule posts for a store's Instagram and Facebook. The end result is a complete, approval-ready week plan — not a single draft post.

Do not use it for a one-off post without the week structure (use the caption template directly instead), for paid ads (that is a different workflow — ad copy, budget and publishing are the owner's in Ads Manager), or for any platform other than Instagram and Facebook, unless the user explicitly asks to adapt it.

## Who does what — Claude handles all the work end to end

Claude runs every step of the workflow below — brief, topics, captions, image prompts, reel briefs, price checks, approval gate, posting checklist and week review. The owner is involved only at three points:

1. **Week decisions only the owner can make** — the current offer and sale dates, which products or bundles to push, the week's goals, and what is NOT allowed this week (for example a claim the owner does not want made). Claude drafts everything; the owner supplies the facts and approves them.
2. **Rendering** — the owner generates the article images in ChatGPT from Claude's prompts and the reel clips in Flow, because image/video generation is region-unavailable on the owner's Muse account. Claude writes the prompts; the owner renders and sends the finished files back.
3. **Approval gate** — the owner approves the exact text, image and time of every post before it is posted or scheduled (see Step 7). Nothing goes out without that approval.

Two device-bound exceptions, stated honestly so the "end to end" claim is not overstated:

- **Posting sign-in:** posting happens through the owner's connected Instagram/Facebook accounts (connector, IG app, or a timed publish job the owner set up). Claude never handles the owner's password or tokens.
- **Images and reel clips:** Claude writes the image plan (which prompt goes with which post, in which order) and the reel briefs. The images and clips themselves come from the owner. Claude never invents a product photo and never attaches the wrong image to a post — if an image does not match its prompt, say so plainly and flag it for the owner.

Everything else — research, topics, captions, prompts, briefs, price checks, checklists — is Claude's work. Do not hand any of it back to the owner as homework.

## Store and account facts (do not invent others)

- **Store:** Fragrance Empire, https://fragranceempire.my — a Shopify store selling designer perfumes in Malaysia, free delivery across Malaysia, cash on delivery available. 155 products, 18 brands, 13 His & Her bundles.
- **Instagram:** @fragranceempire.my — all posts in English; captions carry NO URLs, they say "Link in bio"; feed images portrait 4:5 (1080×1350); every video needs a matching cover image.
- **Facebook Page:** Fragrance Empire, https://www.facebook.com/people/Fragrance-Empire/61596175737426/ — captions carry the direct shop link (https://fragranceempire.my or the collection link); Page post text limit is 1,024 characters via the connector.
- **Rhythm (Malaysia time, MYT):** 12:00pm article + picture, 3:00pm article + picture, 7:00pm reel. That is 14 articles + 7 reels = 21 posts per week. (12pm MYT = 9am PKT; 3pm MYT = 12pm PKT; 7pm MYT = 4pm PKT.)
- **Daily habits:** invite everyone who reacts to a post to Like the Page; reply to every comment the same day.
- **Seller services (Fiverr gig https://www.fiverr.com/s/L34yBpA):** the same weekly plan can be offered as a service — Basic $80, Standard $180, Premium $350, unlimited revisions.

## Hard limits — state them honestly, do not work around them

- **Photographic images only — never tip-cards.** Article-post images are photographic images, never tip-cards (title + key points on a branded background). The owner corrected this on Nov 6, 2026 and it is a standing rule. If a draft says "tip-card", remove it and write a photographic image prompt instead.
- **Text-overlay rule on EVERY image prompt.** Every image prompt must include: the caption headline in large bold metallic gold 3D text at the TOP, "CHOOSE LUXURY" in large bold metallic gold 3D text at the BOTTOM, and "fragranceempire.my" in small elegant white text at the VERY BOTTOM — no other text. A prompt missing any of the three is not ready. (Owner's rule, Nov 12, 2026.)
- **Prices verified live — never from memory.** Every price in a caption is checked on the store's own product page in the same week the plan is written. A price not verified live is a blocker, not a guess. If a price changed since the last check, use the live price and say so.
- **No "100% original" claims unless the owner explicitly approves them.** Never write "100% original", "original perfumes" or any authenticity promise into a caption, image prompt or reel on Claude's own initiative. If the owner approves the claim for a specific post, record the approval in the plan.
- **Never invent product notes, prices or claims.** Every product fact, note and price comes from the store's own product page. If a fact is missing, ask — do not fill it in.
- **Approval gate is mandatory.** Nothing is posted or scheduled until the owner approves the exact text, image and time. A changed caption, price or image needs fresh approval. Approval covers only exactly what was shown.
- **Instagram scheduling is NOT available via the connector.** It returns HTTP 403 — do not retry it. Schedule in the Instagram app or with a timed publish job. Timed jobs can run late; verify live before reporting a post as done.
- **Facebook post text limit is 1,024 characters via the connector.** A Facebook caption longer than that cannot be posted as written — shorten it before the approval gate, not after.
- **A publish call that returns only an ID (or times out) may still have published.** After any uncertain result, verify via the post lookup before retrying or reporting. Never post the same post twice.
- **No credentials in the skill.** Never put an API key, password, access token or secret in a skill file, in chat, or in a repo. Logins happen on the owner's own device.
- **Do not post sale prices after the sale ends.** Prices set for a sale have no auto-expiry on the store — if the sale ended and the owner has not decided to revert, extend or keep a smaller discount, do not write sale prices into new captions. Ask first.

## Topic bank — what actually went live (Nov 6–12, 2026)

These topics were written, approved and posted for Fragrance Empire. Reuse them as the starting bank; do not repeat a topic within the same week, and prefer a fresh angle over repeating last week's exact post.

**Knowledge articles (each ends with a question):**
1. "EDP, EDT, Parfum — what do they mean?"
2. "How to apply perfume the right way"
3. "5 tips to make your perfume last longer"
4. "What is a His & Her Bundle?"
5. "Perfume notes: top, heart, base"
6. "How to choose a perfume gift"
7. "How to choose a perfume for yourself"
8. "How to store your perfume"
9. "Summer scent or winter scent?"
10. "How to know if your perfume is original or not?" (caption: practical checks only — sealed box, batch code, clear printing, trusted store — no authenticity promise)
11. "What are oud, amber and musk?"
12. "Office scent or party scent?"
13. "Why does perfume smell different on two people?"
14. "How to test a perfume before you buy it"
15. "Best perfumes for Malaysian heat"
16. "How many sprays is enough?"
17. "Perfume on skin or clothes?"

**Offer / closing articles:**
18. "4 bestsellers at 50% off" (prices listed, one line each)
19. "Sale ends tonight" (last-day urgency, no new claims)
20. "Still deciding? Start with a bestseller" (hero prices, one line each)

**Reels (7pm slot, one product or bundle each):**
- Hero product reel (for example Dior Sauvage EDP)
- His & Her Bundle reel (for example Invictus & Olympéa, Armani Code & Sì)
- Sale reel (banner slideshow + music + end card)
- Festive / gift reel (for example Deepavali gift bundle)

## Workflow

### Step 1 — Brief (decisions first, no writing before this)

Collect and write down, in `templates/week-plan.md`:

1. Week dates (Friday to Thursday, or the days the owner chooses) and the time zone (MYT).
2. The current offer, exactly as the owner states it — discount, code if any, free delivery, card-payment extra, and the sale end date. If there is no offer this week, write "no offer" — do not carry last week's offer forward.
3. Products and bundles in focus this week (names + which slots they go in).
4. The week's goals (for example followers 2 → 10+, first comments, first link clicks, bundles posted 4/13 → 6/13).
5. What is NOT allowed this week (for example no "100% original" claims, no price for a product whose price is not verified, no repeat of last week's topics).
6. Anything that changed since last week (a deleted code, a price change, a sale ending) — the plan must not carry stale offers.

Do not start Step 2 until the brief is filled in and the owner has confirmed it.

### Step 2 — Topics for the week

1. Pick 14 article topics + 7 reel topics from the topic bank above, or new topics the owner approves. No topic repeats within the week.
2. Alternate the article types across the week: knowledge, knowledge, offer, knowledge, knowledge, offer — so the feed teaches more than it sells. Do not put two offer articles on the same day unless the owner asks for it (sale-closing days are the exception).
3. Assign each reel to one product or bundle only. A reel about "everything on sale" is a sale reel, not a product reel — keep the two separate.
4. Write the week plan table in `templates/week-plan.md`: day, slot, topic, product/bundle, caption status, image status, approval status, live link.

### Step 3 — Captions (Facebook + Instagram versions, every post)

Write every caption twice, using `templates/caption-template.md`:

**Both versions:**
- English only. Short sentences, one idea per line. One emoji at most per paragraph — the caption is a shop post, not a chat message.
- Knowledge posts end with a question (for example "Which one do you wear most? Tell us below 👇"). The question is how the Page gets its first comments — never drop it to save space.
- Hashtags at the end, 3–4 only: `#FragranceEmpire #PerfumeTips #PerfumeMalaysia #LuxuryPerfume`, plus sale tags (`#1111Sale #MegaSale`) on offer posts, plus a product tag (`#DiorSauvage #PacoRabanne`) on reel posts. Never more than 5 hashtags.
- Offer block (only when the brief has an offer): discount + free delivery + card extra + sale end date, in one block, identical wording on both platforms. Example (11.11 sale, Nov 2026): "11.11 MEGA SALE — 50% OFF + FREE delivery across Malaysia, EXTRA 10% OFF with card payments. Sale ends 15 November."
- Never write a price from memory — see Step 6.

**Facebook version only:**
- Direct shop link in the caption: `https://fragranceempire.my` or the collection link (`https://fragranceempire.my/collections/bundles` for bundles). "Link in bio" does not work on Facebook.
- Total length must be 1,024 characters or fewer (connector limit). Check with `scripts/check_captions.py` before the approval gate.

**Instagram version only:**
- NO URLs anywhere in the caption. Replace the link with "Link in bio".
- Feed images are portrait 4:5 (1080×1350) — the article image must be cropped/padded to 4:5 before posting, and every video needs a matching cover image.

**Caption shape (knowledge post):**
```
[Hook line — the question the post answers] [emoji]
[2–4 short lines or bullet points with the answer]
[Question to the reader] 👇
[Offer block, only if the brief has an offer]
[Shop link (FB) / Link in bio (IG)]
[Hashtags]
```

**Caption shape (offer post):**
```
[Offer headline] [emoji]
[Product + price + was-price, one line each — all verified live]
[Offer block: discount + free delivery + card extra + sale end date]
[Question to the reader] 👇
[Shop link (FB) / Link in bio (IG)]
[Hashtags]
```

### Step 4 — Image prompts (one per article post, standalone copyable)

Write one image prompt per article post, using `templates/image-prompt-template.md`. Each prompt is sent to the owner as a standalone copyable message — the owner renders it in ChatGPT and sends the image back.

Every prompt must:

1. **Be photographic.** Start with "Photographic luxury perfume image" and describe a real photo scene: the product, the setting, the light, the mood. Never a tip-card, never a graphic, never text-heavy design.
2. **Carry the text-overlay rule, word for word:** the caption headline in large bold metallic gold 3D text at the TOP, "CHOOSE LUXURY" in large bold metallic gold 3D text at the BOTTOM, and "fragranceempire.my" in small elegant white text at the VERY BOTTOM. End with "No other text."
3. **Match the product.** The bottle in the prompt must be the product in the caption. If the caption is about a bundle, the image shows the bundle pair. Never use a photo that shows a different variant (for example a bottle showing "200ml" on a 100 ML listing).
4. **Name the headline exactly.** The headline text in the prompt is the post's headline, in capitals — the same words as the caption's first line.

Worked examples from the real week-2 plan are in `templates/image-prompt-template.md` — copy their structure, change only the scene and the headline.

When the owner sends an image back, check it against its prompt before scheduling: headline at the top, CHOOSE LUXURY at the bottom, website at the very bottom, no other text, photographic (not a tip-card), product matches the caption. If anything is wrong, say so plainly and ask for a re-render — do not post a wrong image.

### Step 5 — Reel briefs (7pm slot, one per day)

Write one reel brief per day, using `templates/reel-brief-template.md`:

1. **One product or bundle only** (or the sale itself for a sale reel). Name it exactly.
2. **15 seconds, 9:16 portrait, 720×1280, with music.** (Real builds ranged 10–18 seconds; the end card is always exactly 2 seconds.)
3. **Hook in the first 5 seconds** — an unskippable opening: the product, the offer, or the question, on screen in the first 5 seconds. A reel with a slow opening is not ready.
4. **End card: "SHOP NOW AT FRAGRANCEEMPIRE.MY" for exactly 2 seconds** — the last 2 seconds of the reel, nothing after it.
5. **Caption** written the same way as Step 3 (FB + IG versions), with the verified price and the offer block.
6. **Cover image** for Instagram — one still frame, portrait 4:5, product clearly visible.

If the owner sends a Flow render, check it frame by frame before scheduling: duplicated end-card bars, wrong bottle text, or a cut-off headline are all re-render or fix jobs — do not post a flawed reel. (Real example: a Flow reel arrived with a duplicated "SHOP NOW" bar in the final frames; the fix was to trim at the last clean frame and freeze it for the remainder.)

### Step 6 — Price verification (before any caption is final)

1. For every price that will appear in any caption, check the store's own product page live (or the bundles collection page for bundle prices) in the same week the plan is written.
2. Record in the plan: product, live price, live compare-at price, date checked. A price with no check date is not verified.
3. If the live price differs from the brief, use the live price and tell the owner what changed.
4. Never write a price from memory, from last week's plan, or from a competitor's site.

Worked example of verified prices (11.11 sale, checked live 10–12 Nov 2026 — re-verify before reuse, do not treat as current): Dior Sauvage EDP RM 120 (was RM 240), Paco Rabanne 1 Million RM 105 (was RM 210), Versace Eros RM 115 (was RM 230), YSL Black Opium RM 110 (was RM 220), Armani Code & Sì His & Her Bundle RM 218.70 (was RM 437.40).

### Step 7 — Approval gate (mandatory)

Complete `templates/week-plan.md` for the week and run `scripts/check_captions.py` until it passes. Then stop and get the owner's approval for the exact text + image + time of every post.

Approval covers only exactly what was shown: the caption text (FB and IG versions), the image, the reel file, and the slot time. A changed caption, price, image or time needs fresh approval. Do not post a post whose image has not arrived yet — schedule it only after the image is in hand and checked.

### Step 8 — Posting + live verification

**Facebook (Page posts via connector):**
- Post or schedule with the exact approved text + image + time. Only `state: published` confirms a post went live; `state: scheduled` + a scheduled post ID confirms a schedule.
- To change a scheduled post's media or text: cancel the schedule, edit the draft, then publish or re-schedule. Record the post ID in the plan either way.

**Instagram (app or timed publish job):**
- Scheduling is NOT available via the connector (HTTP 403 — do not retry). Post in the IG app, or use a timed publish job at the slot time. Feed images must be the 4:5 version (1080×1350); every video needs its cover image.
- Timed jobs can run late — do not report a post as done until it is verified live.

**After every post:**
- Verify it live (open the post, check the text, image, link and hashtags match the approved version) and record the live link + post ID in the plan. A post with no live link recorded is not done.
- If a publish result is uncertain (only an ID returned, or a timeout), verify via the post lookup BEFORE retrying — never post the same post twice.
- If a post is declined on its approval card, stop and wait for the owner to say so — a decline is not necessarily a refusal of the post itself; the owner may want a different image first.

### Step 9 — Week review (after the last post)

1. Record in the plan: followers at start vs end, comments received, link clicks, reels posted vs planned, bundles posted so far (for example 4/13 → 6/13).
2. Note what worked (best post by views, first comment, first link click) and what did not.
3. Pick ONE change for next week (for example a new topic angle, a different reel hook, or a different slot time) — one change only, so the result shows what made the difference.
4. Carry forward anything unfinished honestly: a missed slot stays missed, a lapsed reel is not revived without fresh approval.

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
