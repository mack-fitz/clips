# RULES — Mack's golf accounts (the ONE current rulebook)

Written Oct 24 2026 from both PLAYBOOK.md files (clips + mackygolfs-mackthegolfer), keeping only what is still in force.
**This file wins over both PLAYBOOKs.** The PLAYBOOKs stay as history and for how-to detail (tool commands, idea lists,
old pool notes). If something here and a PLAYBOOK disagree, this file is right.

RULE CHANGES: Mack batches new rules and they get applied on one day a week. Whoever applies them edits THIS file
(change the rule in place, add the date in the line; never append a new "overrides everything above" section), then
commits. Don't copy rules into task prompts: prompts say "read RULES.md" so there is only one copy.

---------------------------------------------------------------------------------------------------------------------

## 0. HOLDS / WHO POSTS WHAT (check first)
- **NEW SYSTEM FROM MON NOV 9 2026 (Mack, Nov 6) — replaces the Oct 29 "Mack posts week 2+ herself" hold.** Claude posts on
  @mackygolfs and @mackthegolfer IG again, straight from her weekly folders, with NO approval step (Mack: "no"):
  section 5 (weekly videos) and section 5b (YouTube promos). Nothing posts on either IG account before Mon Nov 9 00:00 MT.
  Week 2 (Nov 2-8) stays Mack's: never create a Zernio post on either IG account for week-2 content or for any date before Nov 9.
  A run may prepare and schedule a new Week folder as soon as it appears (Week 3 "11-9" exists since Nov 6), as long as every
  post time is on/after that folder's Monday.
- Week 1/week 2 files (lowercase "week 1"/"week 2" folders) keep feeding TikTok + Facebook + YouTube Shorts as before (section 6/5b);
  never post the same file twice on the same platform.
- mackyyaps also switches to weekly folders from Mon Nov 9 (section 14). heyymackyy (X + IG) has its own task/repo: never touch it here.

## 1. Accounts (Zernio) — always post by exact account id
| what | handle | Zernio profile | account id |
|---|---|---|---|
| Trial reels A | IG @mackygolfs | 6acce3f0662265cf261fca4a | 6acce837f3bd55021dad245f |
| Trial reels B | IG @mackthegolfer | 6acce6402daf1733722343d0 | 6accea22c485191e985aa1cb |
| Clip page IG | IG @moremackygolfs | 6acc27b455143ae1324c8bda | 6acc2885bac230e9d1133105 |
| Clip page X | X @mackygolfs | 6acc27b455143ae1324c8bda | 6acc3edbda858fbeab423c5a |
| Clip page TikTok | TikTok @mackygolfs | 6acc27b455143ae1324c8bda | 6acc3fd31ce18dfecf0a2249 |
| Facebook Page | macky.golfs | 6acc27b455143ae1324c8bda | 6ad052a5a442d9968f306c31 |
| YouTube (Shorts) | YouTube fackmitzgerald ("mack fitzgerald") | 6acce6402daf1733722343d0 | 6ae00b478806963c9f324a62 |
| AI photo account | X @heyymackyy | 6acc65bd97b2d869b209c7c9 | (own repo + rules; never mixed with golf) |

- Facebook posts go ONLY to 6ad052a5a442d9968f306c31 (never Mack's personal profile). More than one FB account listed = stop and ask Mack.
- A B edit must never land on A, and the other way round.
- Times are Mountain (MT = UTC-6 until Nov 1, UTC-7 after). Messages to Mack may add Central.

## 2. Sources (Dropbox)
- **Weekly folders, week 3 on (Mack, Nov 6):** "/Golf/for claude/mackygolfs/Week N <m-d>/" and
  "/Golf/for claude/mackthegolfer/Week N <m-d>/" (ns:3302941984//Golf/for claude/<account>/Week N <m-d>), where <m-d> is the
  Monday the week starts (Week 3 = "Week 3 11-9" = Mon Nov 9-Sun Nov 15). Each holds, for THAT account only:
  - **7 weekly videos** = every video file that isn't a promo. **The file name IS the caption, exactly** (section 5).
  - **Promo reels** for that week's YouTube video, named with her posting order for that account: "#1mackygolfs",
    "#2mackygolfs"... / "#1mackthegolfer"... (match "#<n>" + account name, any case/spacing, extension ignored). Each promo
    in either folder is a different video. Promo caption comes from Mack, not the file name (section 5b).
  - **A thumbnail image** (jpg/png/heic, e.g. "PROMO 1 THUMBNAIL.jpg") = the special cover for that account's #1 promo. Never posted itself.
  Files can be moved in from elsewhere in Dropbox, so a Dropbox file id that is already in a registry under an old path is
  still a new weekly/promo item: re-register it with its new path and role (the GUARD still decides repeats).
  Old weekly folders "week 1"/"week 2" (POSTING RULES v2, Oct 23) keep their old meaning: names are just her counting; a
  name starting "PM"/"pm" is a PM file. Loose files directly in /Golf/for claude/<account>/ are NOT used (list them for Mack).
  Registry: clips state/weekly_sources.json (week-3+ entries add role "weekly"|"promo"|"thumbnail", caption, planned_mt, promo_n).
  Mack ADDS files to existing week folders too (promos usually arrive mid-week): every run that touches golf re-lists EVERY
  week folder (Dropbox file id) against the registry and registers anything new. **Wednesday and Thursday runs must re-check
  both Week folders for newly uploaded promos** (section 5b).
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
5. Run the GUARD (section 9) before creating or scheduling a post, moving one, or putting anything on The Reviewer. FAIL = leave the slot empty and say why.
6. On @mackygolfs/@mackthegolfer, only two kinds of post go out (Mack, Nov 6): (a) her weekly-folder videos and her
   weekly-folder promos (sections 5/5b), scheduled straight from the folder with NO approval, caption = file name (weekly)
   or her given promo caption; (b) anything else (comps, shorties, bounces, Reviewer "promos" extras) ONLY after Mack approved
   that exact item (video, caption, cover) on The Reviewer.
7. A clip never posted anywhere debuts on @mackygolfs or @mackthegolfer, never on @moremackygolfs. (YouTube promos are cuts
   of the long video, which debuts on YouTube: they may launch on TikTok/FB/Shorts at the same 10:00am as IG.)
8. Leave a slot empty rather than break a rule. Report it.
9. Read section 0 (HOLDS / who posts what) before scheduling anything. Nothing on either IG account before Mon Nov 9.

## 4. Shirt wipe
- Everything opens on Mack's shirt wipe EXCEPT @mackthegolfer, which NEVER shows it (reels, comps, shorties, covers).
- @mackygolfs: weekly uploads as-is (wipe first). @moremackygolfs reels + stories: wipe, her first sentence, then the edit.
  X/TikTok/FB originals: her untouched file (just confirm it opens on the wipe).
- @mackthegolfer: cut out ONLY the wipe (right after the shirt is down, before her first word; check the first second at 10 fps). Nothing else changes for a weekly reel.
  Week 3+ (Mack, Nov 6): EVERY file that posts on @mackthegolfer IG (weekly videos AND promos) gets this check and, if a wipe
  is there, ONE CRF-17 encode at full resolution with the wipe cut before posting. @mackygolfs posts keep the wipe (as uploaded).
- YouTube (regular Shorts and promo Shorts): never the wipe (section 5b). TikTok/Facebook: her file as uploaded.
- Compilations and shorties: don't add a wipe; one already in them stays.
- Source with no wipe: open on the strongest action and say so in the report.

## 5. Weekly IG posts — @mackygolfs (A, 6acce837f3bd55021dad245f) and @mackthegolfer (B, 6accea22c485191e985aa1cb) (Mack, Nov 6; from Mon Nov 9)
- **Source:** that account's own "Week N <m-d>" folder (section 2): 7 weekly videos per account per week. Never A's files on B
  or B's on A.
- **Caption = the file name, exactly.** Strip only a real media extension (.mov .MOV .mp4 .MP4 .m4v .hevc); keep her spelling,
  punctuation, capitalization, emoji, "@" mentions and censoring (e.g. "d*cking") exactly as typed. Never rewrite, shorten,
  add hashtags or add anything. **NUMBER PREFIX (Mack, Nov 15, from "Week 4 11-16"):** a leading "<n>-" / "<n> -" (e.g.
  "3- should i try again?") is HER POSTING ORDER, not caption: strip the number, the dash and the following space everywhere
  (IG, TikTok, FB, X, Shorts). Caption of "3- should i try again?" = "should i try again?". Post them in that order:
  1 = Monday, 2 = Tuesday ... 7 = Sunday of that week, on each account (this overrides "order = Claude's choice").
  Only exception: a name that is clearly not a caption (camera default like "IMG_1234",
  "Video Oct 26 2026...", "PM", a bare number) or that mentions OnlyFans/a link: don't post it; ask Mack for the caption in
  the run message and leave that day empty until she answers.
- **NO approval, no Reviewer card:** as soon as a run sees a new Week folder, schedule all 7 videos for each account,
  ONE per day per account, Mon-Sun of that week (order within the week = Claude's choice; spread similar clips apart).
  Create each post already scheduled (never a draft). A day whose time already passed when the folder shows up = post at the
  next sensible time that day, or skip that day and add the leftover video to the end of the week as a second-afternoon post
  only if Mack says so (otherwise tell her it's left over).
- **Times (Zernio best-time data, Mack asked Claude to pick, Nov 6; MG changed Nov 15):** @mackthegolfer about **7:00–7:30am MT**
  (unchanged); @mackygolfs about **3:30–4:30pm MT** — TIME TEST from Week 4 (Mon Nov 16; Mack, Nov 15 "k cool we can test
  those times"): MG's best past posts went out in the afternoon. On a day with an MG IG promo, the MG weekly post goes about
  12:30–1:30pm MT instead and the promo stays 3:30–5:00pm (2+ h apart). Compare Week 4 MG vs Week 3 MG (11:15–12:00) at the
  end of the week and report it to Mack. Vary the minute every day. On a YouTube launch Thursday both move to the afternoon (section 5b).
- **Media:** A = her file untouched (wipe kept; section 7 quality: one conversion only if IG can't take it). B = wipe cut
  (section 4: check the first second at 10 fps, ONE CRF-17 encode at full resolution, nothing else changed).
- **Covers (no text on either, Mack, Nov 6; A updated Nov 10):** A = the video's FIRST FRAME (Mack, Nov 10: "mackygolfs cover
  is supposed to be frame 1"): send NO instagramThumbnail so Instagram uses frame 1. B = an interesting-looking frame Claude
  picks (never the wipe; nothing suggestive). Exception: promo #1 on launch day still uses her special thumbnail (5b).
  ONE-OFF COVER (Mack, Nov 15): @mackygolfs Week 4 "5- took a risk but it worked out!" (Fri Nov 20; Dropbox
  id:etyjxrk_8sAAAAAAAAAFxw) — cover = the frame where Mack and Ally are KISSING (find it by checking frames; full-size, no
  text). Send it as instagramThumbnail (this one post only), and use the same moment as the TikTok cover (videoCoverTimestampMs).
  If no kiss frame can be found, schedule it with frame 1 and tell Mack.
- **BACK TO TRIALS ON A (Mack, Sun Nov 22: "Let's go back to posting mackygolfs on trial reels"):** from Nov 22 on, every
  @mackygolfs IG post (weekly + promos) is a TRIAL reel: platformSpecificData {madeWithAi:false, shareToFeed:true,
  trialParams {graduationStrategy:"MANUAL"}}; NEVER SS_PERFORMANCE. Cover stays frame 1 (no instagramThumbnail) unless Mack
  gives a special cover. Launch-day #1 promo on A: trial too unless Mack says otherwise. W4 A7 "mood swings" (6afaf2af, Sun
  Nov 22 3:33pm) was converted Nov 22. The Nov 10 main-feed test below is OVER; keep it only as history.
- (HISTORY) **Posting type (Mack, Nov 10 — test on A only):** A (@mackygolfs) = REGULAR reel straight to the main feed, NOT a trial:
  platformSpecificData {madeWithAi:false, shareToFeed:true}, no trialParams, no instagramThumbnail. Promos on A too.
  Mack archives flops herself. B (@mackthegolfer) stays a trial reel {trialParams {graduationStrategy:"MANUAL"},
  instagramThumbnail}; NEVER SS_PERFORMANCE. Week 3 A posts from Nov 11 on were converted Nov 10. Review A vs B after a week.
  ONE-DAY EXCEPTION (Mack, Nov 11): on launch day Thu Nov 12 ONLY, B's two posts went out as REGULAR main-feed reels (PopStroke
  promo #1 6af4fe8be11ff29b2b7e417a 10:00 + weekly "at what point do i pick up" 6aef14161f7edebfc3ba7f13 13:42). From Fri Nov 13
  B is back to trial reels; never copy this exception to another day unless Mack says so.
- GUARD (section 9) before scheduling every one; a FAIL leaves that day empty and goes in the run message (rule 4 = same bytes
  never twice on the same account is absolute).
- Record each in weekly_sources.json (planned_mt, zernio id, caption) and clips state/trials.json ("weekly_posts" list; Nov 16:
  live copy moved to clips, section 11).
- **TikTok/FB:** each weekly video also goes on TikTok @mackygolfs + Facebook macky.golfs (section 6) on any day, with NO tie to
  its IG post: it may go before, the same day or after (Mack, Nov 11: she never set an after-IG rule; TikTok/FB are independent of IG).
- **Afternoon slot = promos** (section 5b: 3:30–5:00pm MT). No other afternoon fill on A/B unless Mack approved it on The Reviewer
  (comps/shorties/bounces: next open afternoon 2:00–3:30pm MT on a day without a promo or bumped post on that account).
- **PM files (week 1/2 only)** ("pm.MOV"/"PM.MOV", any case): afternoon only, own account only, never bounce.
  **MACK POSTS PM FILES HERSELF (Mack, Oct 28): NEVER create a Zernio post for a PM file, not even after approval.** On
  approval: send her the full-quality file + final caption + chosen cover the morning of its day (SendUserFile + SendUserMessage
  "PM to post at ~<time>: <caption>"), set the doc decision "self_post", status "sent_to_mack". Same as the "send me to download" flow.
- **Bounces (back and forth, only via The Reviewer approval, no proactive prep):** a reel can go to the OTHER account in an afternoon slot 30 days after its MOST RECENT post
  (to @mackygolfs = with the wipe / original upload; to @mackthegolfer = without). Back on its original account only 60 days
  after its first post there, again afternoons. Every bounce gets a NEW caption, a NEW cover and light edits (different trim/end,
  different opening beat after the wipe, punch-ins). Old /Golf Captions reels follow the same rule.
- **No added text** on trial reel videos (shorties' one line is the only exception). Mack's own burned-in captions stay.
- @mackthegolfer stays clean: no innuendo, nothing suggestive on covers, no OF tie-in, no links to other accounts. (Her own
  file-name captions are posted as she wrote them; only an OnlyFans mention or a link stops a post — ask her.)

## 5b. YouTube Shorts (Mack, Oct 26) and YouTube promos (Mack, Nov 6)
- **Regular Shorts — existing system kept (Mack, Nov 6):** TWO a day from Nov 16 (Mack, Nov 15; see "SHORTS = 2 A DAY" in section 6), ~8:30–9:30am + ~5:30–6:30pm MT (varied), no approvals. The
  4:38am morning run keeps the next 3 days scheduled, picking: (1) week-1 @mackthegolfer reels already posted on IG but not yet
  on YouTube, then (2) week-N @mackthegolfer files as soon as they're registered, wipe ALWAYS cut (one CRF-17 encode; the
  same wipe-cut file as its IG post is fine). Caption: for week 3+ files use her file-name caption when it passes the YouTube
  rules below (no @mentions/links/OnlyFans/suggestive); otherwise write one in her voice. Same file never twice on YouTube.
  On a launch Thursday the regular Short moves to the afternoon (promo #1 takes 10:00am).
- Post: platform "youtube", account 6ae00b478806963c9f324a62, content "<caption>\n\n#golf #shorts", platformSpecificData
  {title: <caption, <=100 chars>, visibility "public", madeForKids false, categoryId "17"}. No custom cover (API can't for Shorts).
  metadata {kind "yt_short", source <file>}.
- YouTube rules: never the shirt wipe — this includes PROMO Shorts and any file Mack hands over for YouTube (Mack, Nov 5:
  the Nov 5 Orlando promo went out with the wipe). Check the first second at 10 fps on EVERY YouTube file and cut the wipe
  (one CRF-17 encode) before scheduling; nothing goes to YouTube untouched. Nothing suggestive in title/description, never any link or mention of OnlyFans or
  other accounts. Same file never twice on YouTube.
- **Weekly YouTube video = Thursdays, live 10:00am MT.** Promo Shorts are IN ADDITION to the regular daily Short.
- **Promos Claude CUTS (Mack, Nov 6: "make them fast and funny. and like 20-40 seconds"; "playing the hole full out wasn't
  good for a reel"):** fast, funny MONTAGES, 20–40 s, quick cuts of about 1–4 s (bad shots, reactions, punchlines, scorecard
  misery), a hook in the first 1–2 s (her best line/reaction, cold open), ending UNRESOLVED (cut right before a payoff, or on a
  punchline that sends people to the full video). NEVER a full hole played out. Every cut keeps whole spoken lines (never cut a
  word; land each punchline; promo.yml "snap" windows + transcript check), swearing kept, original audio only (no music, no
  burned-in text), vertical 1080x1920 cropped below any scorecard bar and tracking Mack. Several montages per video, each a
  different theme so they can post on different days. No captions (Mack gives one promo caption per week).
  **Montage style lessons (Mack's Reviewer notes on PopStroke m02/m03, Nov 8 — apply to every promo cut, 7-iron next):**
  - HOOK = the single funniest self-contained bit, setup + punchline together, even if it happens late in the video
    (m03: "start the reel with that loser on the nose clip" — the "you're a loser, you're right where you're supposed to
    be" / "a little on the nose" pair). Don't open on a plain reaction ("devastating") when a told joke is available.
  - END on a landed punchline, not on a setup/begging line that trails off (m02: "cut the last clip about needing a
    bogey" -> now ends on "What'd I tell ya? 12 was my unlucky number"). "Unresolved" = cut right after a punchline before
    the result shows, not an extra weak line tacked on. When a cut adds nothing, drop it: a shorter reel (~27 s) is fine.
  - Themes she liked enough to fine-tune: running bits/excuses she blames on outside things (putter, fans, sun, unlucky
    number) and self-roasting disaster lines. Her notes are short and literal: apply exactly what she wrote, nothing more.
- **PROMOS, week 3 on (Mack, Nov 6) — from her weekly folders, NO approval:**
  - Source: the promo files in BOTH Week folders (section 2), labeled in posting order per account (#1mackygolfs, #2mackygolfs...,
    #1mackthegolfer...). All different videos. Wednesday and Thursday runs re-check both folders for newly uploaded promos.
  - Caption: Mack gives ONE promo caption per week, the SAME for every promo video on every platform. If she hasn't given it
    (look in RULES/registry notes and the run's context), ask her in the run message ("promo caption for <video>?") and
    don't schedule promos without it. Use her caption EXACTLY, line breaks included (Mack, Nov 6 example: "Orlando has 170+
    golf courses. I went to the worst rated one.\nNew youtube video out NOW!\n🔗 in bio"). Where a platform allows a
    clickable link (Facebook, YouTube description), replace her "🔗 in bio" line with the full-video URL; where it doesn't
    (TikTok, IG), keep "🔗 in bio". No hashtags or anything else added. YouTube Shorts: title = her first line (<=100
    chars), description = her caption with the URL line (the only link ever allowed on YouTube). If the full-video URL isn't known yet, ask Mack in the run
    message (FB/YouTube promo posts can be edited to add it once known).
  - **LIVE BY 10:00 (Mack, Nov 12): "These need to be POSTED at 10, not starting to post."** On Nov 12 the IG posts were
    claimed at 10:00:21 and sat in Instagram "processing" for 4+ minutes (untouched HEVC .mov 1440x2560). From now on: schedule
    every launch #1 post at **9:52am MT** (all platforms), and upload IG/FB launch files as H.264 MP4 1080x1920 high bitrate
    (~16-20 Mbps, CRF ~17, AAC 256k) so Instagram processes fast. Check status at 9:57 and fix anything not live by 10:00.
  - **Launch Thursday, exactly 10:00am MT:** #1mackygolfs posts on IG @mackygolfs AND TikTok @mackygolfs, YouTube Shorts and
    Facebook macky.golfs; #1mackthegolfer posts on IG @mackthegolfer. Both #1 promos use the special cover = the thumbnail image
    Mack put in THAT account's Week folder (IG instagramThumbnail; Facebook custom thumbnail if Zernio allows; TikTok stays
    first frame; Shorts can't take a cover). Any other post that day on the same account (the weekly IG video on A and B, the
    regular Short, TikTok/FB posts) is bumped to the afternoon (after 1:00pm MT, spaced >= 1 h from other posts on that account).
    If #1 shows up after 10:00 Thursday, post it at the next sensible time that day and tell Mack.
  - **The rest, IG:** each account's own remaining promos (#2, #3...) post on that account in her labeled order, ONE per day,
    in the AFTERNOON slot about **3:30–5:00pm MT** (vary the minute; Zernio data shows @mackygolfs' strongest window is late
    afternoon), starting Friday. Covers: @mackygolfs = frame 1 (no custom cover, Nov 10); @mackthegolfer = an interesting frame (wipe cut from the
    video, section 4). Post type as section 5 (A and B = trial reels from Nov 22).
  - **The rest, TikTok + Facebook + YouTube Shorts:** EVERY promo from BOTH folders that hasn't been there yet (incl. #1mackthegolfer)
    posts once on each, any order, ONE promo per day per platform, afternoon slot 3:30–5:00pm MT, starting Friday. Post every one.
    Covers: TikTok first frame (videoCoverTimestampMs 0); Facebook default (special thumbnail ONLY on the launch-day promo);
    Shorts none (API can't; Mack is fine with it). YouTube copies: wipe cut (one CRF-17 encode). TikTok/FB: her file as uploaded.
  - Mack sets the YouTube "related video" herself (tell her which Short -> which video). metadata {kind "yt_short_promo"}.
  - GUARD before every promo post; same file never twice on the same platform/account.
- Video 1 (Nov 5, https://youtu.be/U7DdgA40jXI, live 10:00am MT): promos scheduled (metadata kind "yt_short_promo") Thu Nov 5
  10:20am, then Fri Nov 6-Tue Nov 10 afternoons 2:00-4:30pm MT. Thu's regular Short moved to 3:37pm. Keep scheduling regular
  morning Shorts Nov 6-10 as usual; never move/delete the promo posts.
  **Video 1 leftover promos on IG (Mack, Nov 6; start moved to Mon Nov 9 per Mack, Nov 7 — nothing on MG/MTG Nov 7-8):**
  Mack allowed the leftover Orlando promos on @mackygolfs/@mackthegolfer IG from Mon Nov 9 onward. Each Orlando clip posts
  on IG ONCE TOTAL across both accounts. Already on IG (Mack's own posts, matched by exact duration + frames): trailer
  "worst course in orlando reel" = MTG Nov 5; "reel 2" = MG Nov 5; "reel 5" = MG Nov 6; "reel 6" = MTG Nov 6.
  Scheduled by Claude (trial reels, her caption, no AI label): "wet reel - mackygolfs" = MG Mon Nov 9 4:12pm MT
  (6aeeb6fcf53369239702fea0); "reel 2A" = MTG Mon Nov 9 3:47pm MT (6aeeb700f53369239702feba). All 6 are now used on IG:
  never schedule another Orlando promo on MG/MTG. From the PopStroke video (Nov 12) on, Mack says which promo goes on
  which account.
- Video 3 "Can I Break 50 With Only a 7 Iron?" (Dropbox /Youtube/3. 7iron only/7iron final.mov). VIDEO URL (Mack, Nov 18
  00:00 MT): https://youtu.be/xZh03ZipvX4 . Launch Thu Nov 19 10:00am MT.
  PROMO CAPTION (Mack, Nov 19; she cut "my 7 iron is the club i trust most."): IG/TikTok = "i suck with my driver. so i played
  9 holes with nothing but a 7 iron and a putter. the goal: break 50.\n🔗 in bio"; FB + Shorts description = same first line +
  "\nhttps://youtu.be/xZh03ZipvX4". Shorts title "Can I Break 50 With Only a 7 Iron?". No hashtags.
  Promo files (Week 4 11-16): MG "george w.mov" (id:etyjxrk_8sAAAAAAAAAG4w, launch), MG "mg.mov" (id:etyjxrk_8sAAAAAAAAAG5A),
  MTG "1.mov" (id:etyjxrk_8sAAAAAAAAAG5Q, launch). Cover = "story_7iron_B.jpg" (in both folders). None of the 3 has a shirt
  wipe (checked first 1.5 s at 10 fps), so ONE H.264 encode each (1080x1920 CRF17 High 4.2, AAC 256k, faststart) serves every
  platform incl. YouTube + MTG; media on branch scratch/yt3-promos @ cc12f2c7e9ea717b9f902002258cadc7413a197e.
  Scheduled Nov 19 ~00:35 MT (chat run), times MT:
  | file | account | when | Zernio |
  |---|---|---|---|
  | george w | IG @mackygolfs main feed, cover story_7iron_B | Thu 11-19 9:52 | 6afea63ed38d23467369d2bd |
  | george w | TikTok @mackygolfs | Thu 11-19 9:52 | 6afea6448f51011728e7d5f0 |
  | george w | FB macky.golfs reel, custom thumbnail story_7iron_B | Thu 11-19 9:52 | 6afea6478f51011728e7d609 |
  | george w | YouTube Short | Thu 11-19 9:52 | 6afea64b8f51011728e7d614 |
  | 1.mov | IG @mackthegolfer main feed (not trial), cover story_7iron_B | Thu 11-19 9:52 | 6afea64ed38d23467369d322 |
  | mg.mov | IG @mackygolfs TRIAL reel (MANUAL; Mack, Nov 19), cover story_7iron_B | Fri 11-20 4:17pm | 6afea655e110157f4bc57d2f |
  | mg.mov | TikTok | Fri 11-20 3:47pm | 6afea658d38d23467369d349 |
  | mg.mov | FB reel (default cover) | Fri 11-20 4:08pm | 6afea65aa1a5091d3c2aa43c |
  | mg.mov | YouTube Short | Fri 11-20 4:31pm | 6afea65dfa9873a8a8542ec5 |
  | 1.mov | TikTok | Sat 11-21 3:52pm | 6afea660fa9873a8a8542ecd |
  | 1.mov | FB reel (default cover) | Sat 11-21 4:14pm | 6afea663e110157f4bc57d5f |
  | 1.mov | YouTube Short | Sat 11-21 4:37pm | 6afea665e110157f4bc57d64 |
  Bumped: MTG weekly "you me right now lets go" (6afaf2844703a581a7a31d7c) Thu 7:11am -> 1:43pm. MG weekly "took a risk but it
  worked out!" (6afaf295c6eb019ec2841ed6, kiss cover kept) Fri 3:54pm -> 9:14am (Mack, Nov 19: on this Friday MG weekly goes in
  the MORNING, the mg.mov trial promo in the afternoon, not close together). MG Thu weekly stays 4:21pm. All 3 promo files are
  now used on IG/TikTok/FB/Shorts: never schedule them again. Mack sets the YouTube related video on the 3 Shorts herself.
- Video 2 "I Owe Tiger Woods an Apology" (PopStroke, Thu Nov 12 10:00am MT = 17:00 UTC). Promo caption (Mack, Nov 11):
  "I owe Tiger Woods an apology.\nNew youtube video out NOW!\n🔗 in bio". #1 promos scheduled Nov 11 (chat run): MG "popstroke reel 2.mov"
  on IG @mackygolfs 6af4fe818fb8ec3642cd1680, TikTok 6af4fe93e11ff29b2b7e41b8, FB 6af4fe96e11ff29b2b7e41cd, YouTube Short
  6af4fe998fb8ec3642cd1701; MTG "popstroke reel 1" on IG @mackthegolfer 6af4fe8be11ff29b2b7e417a. Neither file has a shirt wipe
  (all untouched). VIDEO URL (Mack, Nov 11 evening): https://youtu.be/y-Npwvc9F7Y . Added as the 3rd line of the #1 FB caption
  and Short description on Nov 11. Every later Video 2 promo on FB + Shorts: caption line 3 = this URL (no "🔗 in bio").
  Older notes on Video 2 cuts: 10 promo Shorts cut Nov 6 (workflow promo.yml; full files on release
  promo-popstroke-review + scratch/promo-popstroke-clips(2)) are on The Reviewer, collection "promos" (docs yt2_p01..p10).
  **Nov 7: replaced by 4 fast funny MONTAGES** (Reviewer docs yt2_m01..m04; full files on release promo-popstroke-montages +
  scratch/promo-popstroke-montages(2); cut from Mack's re-edited "pop stroke beginning cut.mov" = the old file minus 16.2 s of
  intro; she renamed the old one "zignore.mp4" and the folder to "2. I Owe Tiger Woods an Apology"). p01..p10 are hidden
  (status "dropped", "OLD single-moment cut"); never use them. Same OPTIONAL-EXTRA rules below apply to the montages.
  **Nov 8:** notes applied to m02 + m03 (round 2, files *_r2 on scratch/promo-popstroke-montages3 + same release); Mack
  asked for 6 PopStroke montages, so m05 "the lag master" and m06 "brutally honest" were added (files on scratch/promo-popstroke-montages5 + same release).
  m01 + m04: she's "still thinking" — leave them alone until she notes/decides.
  **Nov 6 change: these Reviewer clips are now OPTIONAL EXTRAS** (Mack supplies her own promo files in the Week folders).
  Use one only if she approves it, never instead of her folder promos, and only in an afternoon promo slot (YouTube/TikTok/FB)
  left free after every folder promo has its day. Never schedule a "promos" doc she hasn't approved.
  Notes (decision "changes") are applied like comp notes: re-cut via promo.yml, new preview, round +1, decision null.

- **TURN DOG ONE-OFFS (Mack, Nov 17 night) — already scheduled, never schedule again:** Week 4 files without a number,
  MG "let's find the best golf glizzy in the world." (id:etyjxrk_8sAAAAAAAAAFcg) and MTG "THE COURT IS NOW IN SESSION. Let's
  find the best dog. .mov" (id:etyjxrk_8sAAAAAAAAAFug), are extra posts Mack asked for: both IG accounts, MAIN FEED (MTG too,
  not a trial), Wed Nov 18 8:52am MT (live by 9:00; Mack moved it from 7am, Nov 18 00:05), caption = file name + line break + "turndogtribunal.com" (Zernio
  6afd44d8a2c0e07c4935bebd MG, 6afd44dad34dd1719548c462 MTG). MTG's weekly "am i right on this" moved to 2:34pm MT that day.
  They are NOT weekly videos: register them as role "special". TikTok @mackygolfs + FB macky.golfs (Mack, Nov 18): MG's goes
  there Wed Nov 18 8:52am MT with its IG (Zernio 6afd4f0058f7e07ad45c2da9); MTG's goes there Thu Nov 19 1:37pm MT, after the
  10am YouTube launch (6afd4f045807d9587f05a333). Nowhere else (no X/Shorts/@moremackygolfs) unless Mack asks.

## 6. Clip pages — @moremackygolfs, X, TikTok, Facebook
- **@moremackygolfs (Mack, Nov 15 — REPLACES the old re-edit rule): "treat it like tiktok but 30 days later".** Post Mack's
  ORIGINAL reels UNTOUCHED (her file as uploaded, wipe kept, no re-edit, no restructure, no punch-ins, no burned captions, no
  story teaser). Eligible = a video Mack already posted on @mackygolfs or @mackthegolfer, and 30+ days since that footage's most
  recent IG post on ANY of the three accounts (clips state, incl. clips state/posted_index.json; the
  "moremackygolfs_eligibility" list there is a snapshot). Caption = the caption it had on TikTok/FB (or its file-name
  caption; number prefix stripped), never OnlyFans. Cover = frame one. Regular reel (not trial). Same file never twice on
  @moremackygolfs. **Cadence (Mack, Nov 16): ONE post a day for now, ~5:00–7:00pm MT** (vary the minute). Keep 3 days scheduled.
  **NO BIG HITS (Mack, Nov 16, new rule):** never post a video that got OVER 100,000 views on @mackygolfs or @mackthegolfer
  when it was posted there (any IG post of that footage on either account; check Zernio analytics). Skip it entirely. Media: reuse the Zernio-hosted URL from its earlier TikTok/FB/IG post when there is one.
- **X @mackygolfs: BACK ON (Mack, Nov 14: "I want you posting mackygolfs stuff on x still").** (It was stopped Oct 29; that stop is over.)
  X @mackygolfs (6acc3edbda858fbeab423c5a), profile 6acc27b455143ae1324c8bda: 2 posts EVERY day, morning 8:00–9:30 MT and
  evening 5:00–7:00 MT (vary the minute). Content = the same pool as TikTok/FB: her already-posted originals and weekly-folder
  reels whose IG post is already published (her file, wipe kept). Never the same video on X within 30 days. Caption = the file
  name / its IG caption, no OnlyFans mention, no hashtags needed; a question works well. X needs H.264 SDR (one CRF-17
  tone-mapped encode for HEVC/HDR files), max 2:20 (longer: cut at a natural gap for the X copy only, or skip that video).
  Every clip-page run keeps X scheduled at least 2 days ahead, like TikTok/FB.
- **SHORTS = 2 A DAY, SHORT CLIPS FIRST (Mack, Nov 15, test ~2 weeks):** regular YouTube Shorts go to TWO a day (~8:30–9:30am
  and ~5:30–6:30pm MT; vary the minute), promo Shorts on top as usual. Prefer clips UNDER ~30 s (the 10 s "i need new clubs"
  got 4.2k vs ~1.3–1.6k for 2-minute holes); longer clips only when no short one is available. Wipe always cut, same file
  never twice on YouTube, no bikini (below). Compare Shorts views after 2 weeks and report to Mack.
- **NO BIKINI ON YOUTUBE (Mack, Nov 15):** the @mackygolfs Week 4 11-16 "bikini reel" = "3- should i try again?" (Dropbox
  id:etyjxrk_8sAAAAAAAAAGmQ; Mack named it) NEVER goes on YouTube Shorts (any
  week, ever). Which file it is: check frames of every MG Week 4 video before it goes to Shorts; any video where Mack is in a
  bikini/swimsuit is excluded from Shorts (it still posts on IG/TikTok/FB/X as normal). If unsure, leave it off Shorts.
- **NEWEST WEEK FIRST (Mack, Nov 15: "are tiktok/facebook/X/shorts not starting with this weeks stuff?"):** on TikTok,
  Facebook, X @mackygolfs and YouTube Shorts, the CURRENT week's folder videos (both accounts, number prefix stripped from
  captions) take the next open slots BEFORE any older original or leftover. Aim: each week's 14 videos are on every one of
  those platforms within that week (same day as its IG post or later is fine; never before Monday of its week). Older
  originals only fill slots after the current week's videos are all placed. Shorts: wipe cut as always.
- **TikTok @mackygolfs + Facebook Page:** weekly-folder reels post as-is (her file, wipe kept, cover = first frame).
  Week 3+ (Mack, Nov 6 update): each weekly video can go there the same day as its IG post (later than the IG post time) or
  any day after, with the same file-name caption (FB may add one #golf). Week 1/2 files: any order, as before. FB on the
  same schedule as TikTok. Usual cadence: about 2–3 posts a day each on TikTok and FB (promos included in that count).
  Plan in clips state/schedule.json "weekly_plan". Other TikTok/FB slots: Mack's already-posted originals (TikTok should
  eventually get every original); never-posted videos only after their IG post is published.
  YouTube promos also go here (section 5b) and WIN over these rules where they conflict (launch-day 10:00am #1, one promo a
  day in the 3:30–5:00pm slot, other posts that launch Thursday bumped to the afternoon).
- **Facebook extras:** 3–60 s videos post as Reels (contentType reel); anything longer posts as a regular Page video (no contentType reel) — Mack, Oct 31: every original is usable on FB; never the same video on the Page within 30 days; captions may add ONE #golf; a
  question works well. TikTok: PUBLIC_TO_EVERYONE, comments/duet/stitch on, commercial none, cover = first frame (videoCoverTimestampMs 0).
- Bought engagement on @moremackygolfs (Oct 12: 442 followers counted as bought, 1,000 views, 100 likes) is excluded from all analytics.

## 7. Making things
- **Quality (Oct 23):** @mackygolfs and TikTok/FB originals = her file untouched whenever the platform takes it (IG limit 300 MiB).
  Otherwise ONE conversion: H.264 High, level 4.2, 1080x1920, CRF 17, maxrate ~25 Mbps (bufsize 50M), AAC 256k 48 kHz,
  +faststart, source frame rate. Edits (@mackthegolfer wipe cuts, re-edits, comps, shorties) = ONE CRF-17 encode from the TRUE
  original (source < 8 Mbps at 1080x1920 = a shrunk copy, re-fetch). Never downscale, never double-encode. IG transcoding
  error = re-encode once at level 4.2 ~20 Mbps (never 5 Mbps). Record source vs export bitrate in the notes file.
  Full-quality files > 100 MB live on scratch branches, never main.
- **Covers:** full-res JPEG q95, 3+ options (weekly/promo posts: Claude just picks one, no options needed). @mackygolfs = frame 1 / no custom cover (Nov 10); @mackthegolfer = interesting/smiling/talking frames, never the
  wipe; weekly videos and promos on @mackygolfs/@mackthegolfer get NO cover text (Mack, Nov 6), #1 promos use her thumbnail; @moremackygolfs and TikTok = frame one. Cover text styles (grid reference covers/grid-reference.png): mostly
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
- Page https://claude.ai/artifact/Ez1N5G9ywcawNCaEjT15qg, ArtifactData collections "reels" (id YYYY-MM-DD_{A|B}_{am|pm}),
  "compilations" (comps + shorties, type "shorty") and "promos" (optional extra promo cuts, section 5b).
- **Nov 6: the approval flow NO LONGER applies to weekly-folder videos or folder promos** (sections 5/5b: scheduled straight
  from the folder, no cards). Don't put weekly videos on The Reviewer and don't keep morning slots on it any more.
  The Reviewer is now only for optional extras Mack asks for: comps, shorties, bounces, "promos" extras, and her notes.
- NO ZERNIO DRAFTS (Mack, Oct 23 — drafts show in her scheduler and confuse her): Never create a Zernio post (draft or
  scheduled) for anything Mack hasn't approved. On approval, create and schedule it in one step (posts_create_post with
  scheduled_for, trialParams MANUAL). Until then keep the full-quality file ready (Zernio temp upload / scratch branch, noted
  on the review doc). Only exception: @moremackygolfs posts parked as drafts by the 30-day rule (GUARD R6) — that unschedules
  a post that already existed.
- Approved (decision "approved", decided_round == round): schedule at the planned time (late = next sensible time in the same
  window). Use chosen_cover (default opt1) and the doc's current caption. Comps/shorties:
  post_account + post_when ("now" = publish now; "next" = next open afternoon 2:00–3:30pm MT on that trial account on a day
  with no promo/bumped post there; @moremackygolfs = its next open slot). Approved "promos" extras: section 5b.
  Old week-1/2 "reels" cards still waiting: leave them (week 2 was Mack's); don't schedule them on A/B.
- Notes (decision "changes"): apply exactly as written, re-upload preview + covers, round +1, decision null, history entry (no Zernio post until she approves), tell Mack "Your notes are done: <title>".
- "Send me to download" notes: send her the full-quality file, decision "self_post", status "sent_to_mack", never schedule it.
- Cards whose slot passed with no decision: drop them (status "dropped"); footage goes back to the pool.

## 9. GUARD (repeat check) — ONE copy: /home/claude/clips/tools/check_repeats.py
- Clone both repos side by side in /home/claude (section 11). Always run the clips copy (it has the v2 rules R1–R6); the copy in
  mackygolfs-mackthegolfer is old and never used. The guard reads clips state/posted_index.json, state/media_sources.json and
  state/trials.json; the mackygolfs-mackthegolfer clone is only READ (old trials/comps/shorties media paths), never pushed.
- posted_index refresh (Nov 16: lives in clips): tools/posted_index.py want <posts.json> -> push clips fp/want_posts.tsv ->
  clips "fingerprint" workflow commits "Fingerprints [skip ci]" (state/fp/) -> pull -> tools/posted_index.py build <posts.json>
  -> commit clips state/posted_index.json + state/never_posted.json (the moremackygolfs_eligibility snapshot is kept on rebuild).
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
- Approved item: create it already scheduled (scheduled_for + timezone "America/Denver"), never as a draft first.
  Pull a post off the schedule (only the @moremackygolfs R6 parking case): posts_update_post is_draft true.
- posts_list (simple) hides drafts and times; use call_tool posts_list_posts for real data.
- Failed post: find the cause, fix it (re-encode, swap a broken URL for a pinned one, shorten caption), reschedule into the
  next open slot; retry transient errors once, then change approach.

## 11. Repos, cloning, records
- mack-fitz/clips = EVERYTHING a run writes (Nov 16: scheduled tasks can push only to clips): RULES.md, guard, schedule.json,
  weekly_sources.json, runlog, trials.json, posted_index.json + never_posted.json, state/fp/ fingerprints + the fingerprint
  workflow (fp/want_*), state/claims/, and new renders/notes (trials, comps, shorties) under clips mg_pending/<trials|compilations|shorties>/.
  mack-fitz/mackygolfs-mackthegolfer = READ-ONLY archive (old trial reels, comps, shorties, notes, PLAYBOOK; its state/ copies
  stopped Nov 16). Runs never push to it and never need to; if a step seems to need it, write the clips path instead.
- Clone blobless + sparse ONLY (repos hold ~8 GB of video):
  `git clone --filter=blob:none --no-checkout https://github.com/mack-fitz/<repo>; cd <repo>; git sparse-checkout init --no-cone;
  printf '/*\n!*.mp4\n!*.mov\n!*.MOV\n!*.MP4\n!*.m4v\n!*.part[0-9][0-9]\n' > .git/info/sparse-checkout; git checkout main`
  Never a plain/--depth 1 clone, never `git ls-tree -l` (it downloads blobs), fetch single videos only when needed
  (`git show <sha>:<path> > file`), commit with `git add --sparse <path>`.
- If a push (to clips) is refused because the repo isn't authorized for this task, don't retry in loops: finish the work in Zernio/The
  Reviewer, write what you couldn't save in the run log line, and tell Mack once that the task needs that repo added.
- Claims: before editing an item commit state/claims/<doc>.md in clips (moved Nov 16); skip items claimed < 60 min ago by
  another job; delete your claim in your final commit.
- Base Camp (https://claude.ai/artifact/NkJnRhgLLfSWz1XXfHbQ79, collection "schedule", docs mackygolfs / mackthegolfer / golf /
  facebook): rebuild from a fresh Zernio pull only (never from memory); drafts (only R6-parked @moremackygolfs posts) show "(parked)". Pinned writes (if_version).

## 12. Who does what (scheduled tasks, updated Nov 6)
| task | when (MT) | job | heavy work? |
|---|---|---|---|
| Golf trials morning run | 4:38am | OWNER of A/B: re-list Week folders; schedule each new Week folder's 7+7 weekly posts (sections 5/4) and its promos (5b, incl. Wed/Thu promo re-check and the Thu 10:00 launch); Shorts 3 days; Reviewer approvals + notes; Sunday note | yes |
| Clip page daily run | 12:24pm | BACKSTOP for anything the morning run left unscheduled on A/B/promos; TikTok/FB ~2–3/day (weekly videos same day as IG or later, promos 1/day), Shorts, @moremackygolfs, mackyyaps (section 14); approvals; notes; then 1 comp + 1 shorty only if time allows | yes |
| Hourly approvals check | :23, 7am–9pm | Reviewer approvals only (comps/shorties/promos extras); on Thursdays 7:23–9:23 also makes sure both #1 promos are scheduled for 10:00; stops in < 2 min when nothing to do | no (Thu #1 promo: one wipe-cut encode allowed) |
| Nightly post check | 10:07pm | approvals; failed posts, account health, rule breaks in the next 3 days; tomorrow's A/B weekly posts (and Thu launch) scheduled in Zernio; tomorrow's mackyyaps post scheduled | light only |
| heyymackyy daily run | 6:24am | AI photo account only (its own repo/rules) | — |
- Time budget: a run that passes ~35 minutes finishes the item in hand, records it, and leaves the rest for the next run.
  Order inside a run = approvals first, then fixes, then new content.

## 13. Run log (every golf task, every run)
- Last step of every run (even "nothing to do" runs of the nightly/morning/clip tasks; the hourly check logs only when it did
  something): append ONE line to clips state/runlog.tsv and push:
  `<start UTC ISO>\t<end UTC ISO>\t<task name>\t<ok|partial|failed>\t<one plain line: what it did / what failed>`
- The nightly check on Sundays reads the last 7 days of runlog.tsv and tells Mack about patterns (repeated failures, runs over
  30 min, things it couldn't save), not one-offs.

## 14. mackyyaps (Mack, Oct 29) — separate from golf
- Accounts: Instagram mackyyaps 6ae39dc291f8e9741c60c5cf, TikTok mackyyaps 6ae39d18bd5929e9a3c9e4df, X mackyyaps
  6ae3a172456a4216e1e0ed17, Facebook Page "Macky Yaps" 6af929b9a1fc6c164172f004 (added Mack, Nov 14). Never cross-post to/from golf accounts or @heyymackyy. Golf-only rules (Golf Captions-only
  Dropbox rule, shirt wipe, trial reels, The Reviewer) don't apply here; no approval step.
- **Source from Mon Nov 9 (Mack, Nov 6): her weekly folder "/Mackyyaps/Week N <m-d>/"** (ns:3302941984//Mackyyaps/Week N <m-d>;
  <m-d> = the Monday it starts; "Week 2 11-9" = Mon Nov 9-Sun Nov 15, 7 files). Always use the NEWEST Week folder: its videos
  fill that week's days, one per day, any order. Registry: clips state/mackyyaps.json (match by Dropbox file id: files are
  moved in from /stash etc., so update the entry's path and keep its group). Re-list every run; relay (links mode,
  scratch/my-*), dedupe as before. Root/stash/"Week 1" are no longer used unless Mack says so; if a week runs short, tell her
  and leave the day empty.
- **Reconcile once (first run that reads this):** every mackyyaps post already scheduled for Nov 9 or later must be a
  Week-folder file with its file-name caption. A scheduled post whose file IS in the Week folder: edit its caption on IG,
  TikTok AND X to the file name (keep its time). One whose file is NOT: delete those Zernio posts (all three platforms) and
  set the registry entry back to "unused". Then fill the open days of that week from the Week folder. Posts before Nov 9 stay.
- ONE post a day: the SAME video at the SAME time on IG (reel, not a trial reel, cover = first frame), TikTok (public, cover
  frame 0), X and the Macky Yaps FACEBOOK Page (Mack, Nov 14: "same rules as tiktok"; from Sun Nov 15; her untouched file,
  same file-name caption; 3–60 s = Reel (contentType reel), longer = regular Page video). Every mackyyaps post = all 4 platforms. Time 5:00–6:30pm MT (best for both platforms; vary the minute daily). No approval step.
- (Mack, Nov 15) If a mackyyaps Week-folder file name starts with "<n>-", that number is her posting order (1 = Monday ...)
  and is stripped from the caption with the dash and space, same as golf (section 5).
- **Caption = the file name, exactly** (strip only a real media extension; keep her spelling/punctuation/caps). Same caption
  on all three. Never write captions for Week-folder files. Only if a name is clearly not a caption (camera default like
  "IMG_0512", hash names) or mentions OnlyFans/a link: skip it and ask Mack. Never mention OnlyFans. Never the Dua Lipa clip.
- NEVER post the same video twice: byte dupes, re-exports AND re-takes of the same bit count as one (registry "group"); one
  per group. Skip clips under 3 s and clips of her singing copyrighted songs (list them for Mack).
- Quality: originals untouched to IG/TikTok; X needs H.264 SDR (one CRF-17 tone-mapped encode for HEVC/HDR files), max 2:20
  (longer: cut at a natural gap for the X copy only, or skip X that day and say so).
- The 12:24pm clip page run schedules the newest Week folder's days from state/mackyyaps.json (status unused -> scheduled ->
  posted) and, from Friday on, warns Mack if next week's folder isn't there yet.
