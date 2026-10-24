# RULES — Mack's golf accounts (the ONE current rulebook)

Written Oct 24 2026 from both PLAYBOOK.md files (clips + mackygolfs-mackthegolfer), keeping only what is still in force.
**This file wins over both PLAYBOOKs.** The PLAYBOOKs stay as history and for how-to detail (tool commands, idea lists,
old pool notes). If something here and a PLAYBOOK disagree, this file is right.

RULE CHANGES: Mack batches new rules and they get applied on one day a week. Whoever applies them edits THIS file
(change the rule in place, add the date in the line; never append a new "overrides everything above" section), then
commits. Don't copy rules into task prompts: prompts say "read RULES.md" so there is only one copy.

---------------------------------------------------------------------------------------------------------------------

## 1. Accounts (Zernio) — always post by exact account id
| what | handle | Zernio profile | account id |
|---|---|---|---|
| Trial reels A | IG @mackygolfs | 6acce3f0662265cf261fca4a | 6acce837f3bd55021dad245f |
| Trial reels B | IG @mackthegolfer | 6acce6402daf1733722343d0 | 6accea22c485191e985aa1cb |
| Clip page IG | IG @moremackygolfs | 6acc27b455143ae1324c8bda | 6acc2885bac230e9d1133105 |
| Clip page X | X @mackygolfs | 6acc27b455143ae1324c8bda | 6acc3edbda858fbeab423c5a |
| Clip page TikTok | TikTok @mackygolfs | 6acc27b455143ae1324c8bda | 6acc3fd31ce18dfecf0a2249 |
| Facebook Page | macky.golfs | 6acc27b455143ae1324c8bda | 6ad052a5a442d9968f306c31 |
| AI photo account | X @heyymackyy | 6acc65bd97b2d869b209c7c9 | (own repo + rules; never mixed with golf) |

- Facebook posts go ONLY to 6ad052a5a442d9968f306c31 (never Mack's personal profile). More than one FB account listed = stop and ask Mack.
- A B edit must never land on A, and the other way round.
- Times are Mountain (MT = UTC-6 until Nov 1, UTC-7 after). Messages to Mack may add Central.

## 2. Sources (Dropbox)
- **Weekly folders** (POSTING RULES v2, Oct 23): /Golf/for claude/mackygolfs/week N and /Golf/for claude/mackthegolfer/week N
  (ns:3302941984//Golf/for claude/<account>/week N), 7+ new reels each. File names/order are just her counting.
  Loose files directly in /Golf/for claude/<account>/ are NOT used (list them for Mack). Registry: clips state/weekly_sources.json.
  Mack ADDS files to existing week folders too (Oct 23: 4 extra PM files landed in week 1 that afternoon): every morning run
  compares EVERY week folder's files (Dropbox file id) with the registry, not just new folders, and registers anything new.
  Any file whose name starts with "PM"/"pm" (e.g. "PM (1).MOV", "PM - never post as a bounce.mov") is a PM file.
- **/Golf Captions**: older captioned reels; @mackygolfs/@mackthegolfer may use these (afternoon bounces, comps, shorties).
- **/golfclips**: CLIP PAGES ONLY (@moremackygolfs, X, TikTok, Facebook). Never anything from /golfclips on @mackygolfs/@mackthegolfer
  (no reels, re-edits, comp or shorty bits).
- No other Dropbox folder, ever (tracer folders, /Golf, batches...).
- Copies of the same clip (byte twins, alt takes of the same hole) count as ONE video (clips state/sources.json).
- Workspace can't download Dropbox or reach Zernio storage directly: relay via clips inbox/relay_links.tsv (links mode,
  scratch branch, never main); uploads > 100 MB via Zernio presigned URL + clips "zupload" workflow.

## 3. Hard rules (every account, every run — nothing overrides these, not even Mack's approval)
1. NEVER cut out shots (every tee shot, approach, chip, putt, drop stays). Only cut dead air, walking, waiting, ball-searching, pauses.
2. NEVER cut or bleep swearing.
3. NEVER cut mid-word or mid-sentence; cut only at real gaps (transcript word times / tools/snap.py).
4. The same media file (same bytes) never posts twice on the same account.
5. Run the GUARD (section 9) before scheduling, moving, promoting a draft or putting anything on The Reviewer. FAIL = leave the slot empty and say why.
6. Nothing posts on @mackygolfs/@mackthegolfer unless Mack approved that exact item (video, caption, cover) on The Reviewer.
7. A clip never posted anywhere debuts on @mackygolfs or @mackthegolfer, never on @moremackygolfs.
8. Leave a slot empty rather than break a rule. Report it.

## 4. Shirt wipe
- Everything opens on Mack's shirt wipe EXCEPT @mackthegolfer, which NEVER shows it (reels, comps, shorties, covers).
- @mackygolfs: weekly uploads as-is (wipe first). @moremackygolfs reels + stories: wipe, her first sentence, then the edit.
  X/TikTok/FB originals: her untouched file (just confirm it opens on the wipe).
- @mackthegolfer: cut out ONLY the wipe (right after the shirt is down, before her first word; check the first second at 10 fps). Nothing else changes for a weekly reel.
- Compilations and shorties: don't add a wipe; one already in them stays.
- Source with no wipe: open on the strongest action and say so in the report.

## 5. Trial reels — @mackygolfs (A) and @mackthegolfer (B)
- **Mornings 7:00–8:30 MT:** ONE reel per account per day, new footage from THAT account's own weekly folder (debut only).
  Vary the minute day to day; A and B at different times.
- **Afternoons 2:00–3:30 MT** (varied). Priority: PM files > turn dog reels > YouTube promos > bounces > comps/shorties.
  Extras beyond 7 in a weekly folder also go to afternoons. Comps/shorties only fill afternoons nothing else took.
- **PM files** ("pm.MOV"/"PM.MOV", any case): afternoon only, own account only, never bounce.
- **Bounces (back and forth):** a reel can go to the OTHER account in an afternoon slot 30 days after its MOST RECENT post
  (to @mackygolfs = with the wipe / original upload; to @mackthegolfer = without). Back on its original account only 60 days
  after its first post there, again afternoons. Every bounce gets a NEW caption, a NEW cover and light edits (different trim/end,
  different opening beat after the wipe, punch-ins). Old /Golf Captions reels follow the same rule.
- **Trial posting:** Zernio trial reel, platformSpecificData {trialParams {graduationStrategy:"MANUAL"}, instagramThumbnail}.
  NEVER SS_PERFORMANCE (Mack shares to followers herself).
- **No added text** on trial reel videos (shorties' one line is the only exception). Mack's own burned-in captions stay.
- @mackthegolfer stays clean: no innuendo, nothing suggestive on covers, no OF tie-in, no links to other accounts.

## 6. Clip pages — @moremackygolfs, X, TikTok, Facebook
- **@moremackygolfs:** only footage Mack has truly already posted herself (name the exact post with >= 15 s of it, from
  mackygolfs-mackthegolfer state/posted_index.json; our trial posts and comp bits don't count). And only 30 days after the most
  recent time that footage posted ANYWHERE on IG (@mackygolfs, @mackthegolfer, @moremackygolfs). Every video is a clearly
  different edit: wipe first, then restructured order, 25–40 % cut, >= 3 punch-ins (alternate 1.0 / ~1.15), different ending,
  her-style burned captions only if the source has none (none during the wipe). Story teaser (15 s, wipe first) with each reel.
  Cover = frame one. Cadence 2.5/day: 3-post days (Oct 23, 25, 27...: 8:00–9:30, 11:30–1:00, 5:00–7:00 MT) alternate with
  2-post days (Oct 24, 26...: morning + evening only). Never more than 3 a day.
- **X @mackygolfs:** Mack's uncut original (H.264 export if HEVC), same caption idea; 2.5/day with the IG reels. Max 2:20.
- **TikTok @mackygolfs + Facebook Page:** weekly-folder reels (PM files included) post as-is (wipe kept, cover = first frame)
  once their IG version is approved; later Mack prefers after IG, not the same day. FB on the same schedule as TikTok.
  Plan in clips state/schedule.json "weekly_plan". Other TikTok/FB slots: Mack's already-posted originals (TikTok should
  eventually get every original); never-posted videos only after their IG post is published.
- **Facebook extras:** Reels 3–60 s only; never the same video on the Page within 30 days; captions may add ONE #golf; a
  question works well. TikTok: PUBLIC_TO_EVERYONE, comments/duet/stitch on, commercial none, cover = first frame (videoCoverTimestampMs 0).
- Bought engagement on @moremackygolfs (Oct 12: 442 followers counted as bought, 1,000 views, 100 likes) is excluded from all analytics.

## 7. Making things
- **Quality (Oct 23):** @mackygolfs and TikTok/FB originals = her file untouched whenever the platform takes it (IG limit 300 MiB).
  Otherwise ONE conversion: H.264 High, level 4.2, 1080x1920, CRF 17, maxrate ~25 Mbps (bufsize 50M), AAC 256k 48 kHz,
  +faststart, source frame rate. Edits (@mackthegolfer wipe cuts, re-edits, comps, shorties) = ONE CRF-17 encode from the TRUE
  original (source < 8 Mbps at 1080x1920 = a shrunk copy, re-fetch). Never downscale, never double-encode. IG transcoding
  error = re-encode once at level 4.2 ~20 Mbps (never 5 Mbps). Record source vs export bitrate in the notes file.
  Full-quality files > 100 MB live on scratch branches, never main.
- **Covers:** full-res JPEG q95, 3+ options. @mackygolfs = wipe frames; @mackthegolfer = smiling/talking frames, never the
  wipe; @moremackygolfs and TikTok = frame one. Cover text styles (grid reference covers/grid-reference.png): mostly
  "Macky vs. ___" pill, some typewriter note, rarely the big red question, sometimes no words. Cover text NEVER over her
  chest or face and never high: mid-frame between face and chest or low below the chest, inside the centered 3:4 grid crop
  (12.5–87.5 % of height). Use tools/cover_a.py --guide and an explicit COVER_Y. Check at grid-thumbnail size AND full size.
- **Captions:** short, dry, lowercase, her voice; ask for help / pick a fight about the score / name the stakes. No hashtags
  (FB: one #golf allowed), no links, no OnlyFans, no innuendo on @mackthegolfer. Don't shorten videos just to get under a minute.
- **Compilations:** her talking while playing, 2–7 s bits, ~30–45 s, open on the strongest bit, never back-to-back bits from
  the same shirt/day, even loudness, no added text (except a theme line where Mack asked for one), 3+ covers. Every comp a new
  theme that actually fits. Idea list + method: mackygolfs-mackthegolfer PLAYBOOK "COMPILATIONS" + compilations/comp1_notes.md.
- **Shorties:** ONE continuous clip, ONE shot (setup -> that shot -> result), 10–15 s, from footage Mack already posted (name
  the post). One meme line: Inter Bold 46 px, white, thin dark outline + soft shadow, top of the ink at y >= 400 of 1920, never
  over her face (lower band 1150–1300 if her head is in 400–700); tools/ontext.py. No moment reused within 2 weeks.
- **Mack picks the account** for every comp and shorty on The Reviewer: leave account/post_account "" on new docs.
- Reviewer previews: 720 px, < 20 MB. Never cut a 0.6 s wipe by accident: check the first second at 5–10 fps.

## 8. The Reviewer (approval flow)
- Page https://claude.ai/artifact/KFJoqNkDr6kpxYDkpniAZ7, ArtifactData collections "reels" (id YYYY-MM-DD_{A|B}_{am|pm})
  and "compilations" (comps + shorties, type "shorty").
- Everything for @mackygolfs/@mackthegolfer goes on it first. Unapproved = Zernio DRAFT (trialParams MANUAL) so approval -> schedule is instant.
- Keep the next 5–7 days of morning slots for both accounts on it; a new week folder goes on it the day it appears.
- Approved (decision "approved", decided_round == round): schedule at the planned time (late = next sensible time in the same
  window; a morning may shift up to 30 min). Use chosen_cover (default opt1) and the doc's current caption. Comps/shorties:
  post_account + post_when ("now" = publish now; "next" = next open afternoon on that trial account; @moremackygolfs = its next open slot).
- Notes (decision "changes"): apply exactly as written, re-upload preview + covers, round +1, decision null, history entry, update the draft, tell Mack "Your notes are done: <title>".
- "Send me to download" notes: send her the full-quality file, decision "self_post", status "sent_to_mack", never schedule it.
- Cards whose slot passed with no decision: drop them (status "dropped"); footage goes back to the pool.

## 9. GUARD (repeat check) — ONE copy: /home/claude/clips/tools/check_repeats.py
- Clone both repos side by side in /home/claude (section 11). Always run the clips copy (it has the v2 rules R1–R6); the copy in
  mackygolfs-mackthegolfer may be older.
- Inputs: every page of Zernio call_tool posts_list_posts (from today-60d to today+30d, limit 100, sort_by scheduled-asc; big
  results auto-save to files: pass those files) + analytics_get_analytics for 6acce837f3bd55021dad245f and 6accea22c485191e985aa1cb
  (source all, from today-60d).
  `python3 tools/check_repeats.py --zernio p*.txt --analytics an_*.txt` (whole schedule) and `... --candidates cands.json`
  (cands = [{"label","account":"ig:mackygolfs|ig:mackthegolfer|ig:moremackygolfs|fb:macky.golfs","media":"<repo>:<path>","time":"<ISO>"}]).
- Exit 0 OK; 1 violation (don't schedule; leave empty); 2 unknown media (map it first: state/media_manual.json, then
  tools/build_media_map.py; Zernio-hosted uploads map as "zernio:<file name>").
- Comps and shorties are exempt from the 30-day windows (not from rule 4).

## 10. Zernio mechanics
- Create: call_tool posts_create_post (media_items with pinned raw.githubusercontent.com/mack-fitz/<repo>/<commit sha>/<path>
  URLs, never /main/; > 100 MB = Zernio presigned upload).
- Moving a post: set BOTH top-level scheduled_for AND the platform entry's scheduledFor (posts_update_post with platforms[]).
- Draft -> scheduled: posts_update_post is_draft false + scheduled_for. Pull a post off the schedule: is_draft true.
- posts_list (simple) hides drafts and times; use call_tool posts_list_posts for real data.
- Failed post: find the cause, fix it (re-encode, swap a broken URL for a pinned one, shorten caption), reschedule into the
  next open slot; retry transient errors once, then change approach.

## 11. Repos, cloning, records
- mack-fitz/clips (clip pages, RULES.md, guard, schedule.json, weekly_sources.json, runlog) and
  mack-fitz/mackygolfs-mackthegolfer (trial reels, comps, shorties, notes, trials.json, posted_index.json, claims).
- Clone blobless + sparse ONLY (repos hold ~8 GB of video):
  `git clone --filter=blob:none --no-checkout https://github.com/mack-fitz/<repo>; cd <repo>; git sparse-checkout init --no-cone;
  printf '/*\n!*.mp4\n!*.mov\n!*.MOV\n!*.MP4\n!*.m4v\n!*.part[0-9][0-9]\n' > .git/info/sparse-checkout; git checkout main`
  Never a plain/--depth 1 clone, never `git ls-tree -l` (it downloads blobs), fetch single videos only when needed
  (`git show <sha>:<path> > file`), commit with `git add --sparse <path>`.
- If a push is refused because the repo isn't authorized for this task, don't retry in loops: finish the work in Zernio/The
  Reviewer, write what you couldn't save in the run log line, and tell Mack once that the task needs that repo added.
- Claims: before editing an item commit state/claims/<doc>.md in mackygolfs-mackthegolfer; skip items claimed < 60 min ago by
  another job; delete your claim in your final commit.
- Base Camp (https://claude.ai/artifact/NkJnRhgLLfSWz1XXfHbQ79, collection "schedule", docs mackygolfs / mackthegolfer / golf /
  facebook): rebuild from a fresh Zernio pull only (never from memory); drafts show "(waiting on review)". Pinned writes (if_version).

## 12. Who does what (scheduled tasks, Oct 24)
| task | when (MT) | job | heavy work? |
|---|---|---|---|
| Golf trials morning run | 4:38am | approvals; weekly folders onto The Reviewer; Reviewer notes older than 12 h; Sunday note | yes |
| Clip page daily run | 12:24pm | approvals; all Reviewer notes; @moremackygolfs/X/TikTok/FB; then 1 comp + 1 shorty only if time allows | yes |
| Hourly approvals check | :23, 7am–9pm | approvals only; stops in < 2 min when nothing is approved | no |
| Nightly post check | 10:07pm | approvals; failed posts, account health, rule breaks in the next 3 days; tomorrow's mornings covered | light only |
| heyymackyy daily run | 6:24am | AI photo account only (its own repo/rules) | — |
- Time budget: a run that passes ~35 minutes finishes the item in hand, records it, and leaves the rest for the next run.
  Order inside a run = approvals first, then fixes, then new content.

## 13. Run log (every golf task, every run)
- Last step of every run (even "nothing to do" runs of the nightly/morning/clip tasks; the hourly check logs only when it did
  something): append ONE line to clips state/runlog.tsv and push:
  `<start UTC ISO>\t<end UTC ISO>\t<task name>\t<ok|partial|failed>\t<one plain line: what it did / what failed>`
- The nightly check on Sundays reads the last 7 days of runlog.tsv and tells Mack about patterns (repeated failures, runs over
  30 min, things it couldn't save), not one-offs.
