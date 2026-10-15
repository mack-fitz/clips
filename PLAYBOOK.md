# Clip page playbook — @moremackygolfs (IG) + @mackygolfs (X, TikTok)

Operating rules for every edit and post. Scheduled runs read this file first.

## Accounts (Zernio)
- Instagram @moremackygolfs — account ID 6acc2885bac230e9d1133105 (edited clips)
- X @mackygolfs — account ID 6acc3edbda858fbeab423c5a (uncut)
- TikTok @mackygolfs — account ID 6acc3fd31ce18dfecf0a2249 (uncut)
- Posting times: Mountain time. Analytics/reminders: push + email summary.

## Source videos
- Mack uploads videos into the chat in batches (my workspace can't download from Dropbox).
- Videos come with Mack's own burned-in captions.
- Assume every video has already been posted on Mack's other accounts.

## Instagram edit (always edit — duplicate-content risk)
- Open on the attention moment if there is one (e.g. the shirt wipe) and keep it,
  then the first full sentence. Otherwise open on the strongest action.
- Never start or end a cut mid-word or mid-sentence. Cut only on measured audio
  pauses (no transcription available — snap cuts to the quietest point nearby).
- Tighten: remove filler talk, dead air, waiting between shots. Keep every shot
  with its tracer fully visible (strike to landing), and every payoff line.
- Punch in ~15% on reaction moments.
- NO hook text or any added text on the video (Mack, Oct 12) — render with "" "".
- Keep Mack's captions untouched (they sit mid-frame).
- Target length: tight, usually 30–70s depending on the story.
- Cover: always a shirt-wipe frame (Mack, Oct 12), from early in the wipe with the face
  covered. Cover text styles rotate per the grid reference
  (/home/claude/mackygolfs-mackthegolfer/covers/grid-reference.png and the "Cover text style"
  section of that repo's PLAYBOOK.md): mostly "Macky vs. ___" pill / some typewriter note /
  occasional big red question / sometimes no words. No two consecutive posts with the same style;
  mid-frame (45–70% down), inside the center square.
- Export H.264 1080x1920, keep files small (~4–5 Mbps) so publishing is fast.
- **Must be CLEARLY different from Mack's original (Mack, Oct 12).** Every @moremackygolfs edit
  needs ALL of: a restructured order (not just trims of the original timeline — move a later
  moment or payoff earlier, or open on a different beat than Mack's version); 25–40% of the
  runtime removed; at least 3 punch-ins (alternate 1.0 and ~1.15 zoom, not one long zoom);
  a different ending point than the original; a different cover than Mack's. Keeping the shirt wipe is fine, but it must not open the reel the same way Mack's
  post does if Mack's post opened on it — put a later payoff moment or a 1–2 s teaser before it.
  Before scheduling, make a side-by-side contact sheet (original vs edit, one frame every 3 s)
  and Read it. If the edit still reads as the same video, re-edit. Log `diff_check` in
  state/schedule.json for the slot (what changed). Never reduce length just to be different
  beyond the 25–40% cut.

## X and TikTok
- Post Mack's original, uncut (shirt wipe kept). Light trims only.
- X: max 2:20 unless Premium — trim if longer.
- TikTok: PUBLIC_TO_EVERYONE, comments/duet/stitch on, commercial content none.

## Captions (all platforms)
- Dumb, short, lowercase, Mack's voice. Reference style: "golf is so easy guys",
  "6 is basically par".
- NO hashtags. No links. No OnlyFans mentions or innuendo.

## Stories
- Post a 15s teaser story with each new IG reel ("full disaster on my page" style),
  built from the original, no added text.

## Account safety
- No bio link (Mack's choice). No fake engagement, no automated scrolling.
- Watch for: failed posts, account health issues, sudden non-follower reach drops.
- Remind Mack to check Instagram Account Status weekly.

## Trial reels: @mackygolfs (A) and @mackthegolfer (B) on Instagram
Two Zernio profiles, one per account: "mackygolfs" (6acce3f0662265cf261fca4a) holds A (account 6acce837f3bd55021dad245f),
"mackthegolfer trials" (6acce6402daf1733722343d0) holds B (account 6accea22c485191e985aa1cb). Get account IDs with accounts_list
filtered by profile, and always post by exact account ID: a B edit must never land on A. Trial reels ONLY on these two accounts; @moremackygolfs keeps posting
regular reels as above. X and TikTok setups are not touched by any of this.

- **Source:** Dropbox trial folder (name in the line below once Mack gives it), captioned reels
  only. Pull in random order. Relay via `inbox/want_trials.txt` (names only), files land in
  `inbox/trials/`. Track in `state/trials.json` (per reel: Dropbox ID, A version + date + post ID,
  B version + date + post ID, opening style, views/shares/saves/watch time when available).
  Trial folder: Dropbox `/Golf Captions` (secret DROPBOX_TRIALS_URL).
- **NO burned-in text on any A or B video.** Render with `tools/render.sh src segs.json "" "" out.mp4`
  (empty hooks = nothing drawn). Don't add hook text, subtitles, captions or labels to
  the picture. Mack's own captions already in the video stay as they are. Covers: strongest frame,
  no text.
- **A (@mackygolfs):** post the original, unedited, opening on the shirt wipe ALWAYS. If the reel
  looks like it was already posted on A (compare against A's existing reels), make a different edit
  for A instead: new cut points and punch-ins, still opening on the shirt wipe.
- **B (@mackthegolfer):** its own clean edit. NEVER the shirt wipe. Open either on the first spoken
  line right after the wipe, or on a 1-2 s teaser of a later payoff moment then cut back to Mack
  talking. Alternate the two and track which holds better. Fully clean: no innuendo in captions,
  nothing suggestive in covers, no OF tie-in, no story shares or links to A or the other accounts.
- **Every IG account gets its own version.** If a reel has also gone out on @moremackygolfs (or
  the other trial account), make sure cuts and cover differ from those versions. Never skip a reel
  for being a duplicate: re-edit it.
- **Timing:** post a reel to A first; B's version goes up 2-4 days later, never the same day.
- **Pace:** start at 3 trial reels a day per account (A ~9:30-10:30am, 1-2pm, 6:30-7:30pm MT;
  B offset by ~45 min). Raise to 4-5 a day only if reach holds and no Account Status warnings.
  Stay under 10 a day.
- **Posting:** Zernio posts_create_post, instagram, platformSpecificData
  `{"trialParams": {"graduationStrategy": "SS_PERFORMANCE"}}` (Instagram auto-shares strong
  trials to followers), `instagramThumbnail` for the cover. Captions: same dumb lowercase voice,
  no hashtags or links.
- **Weekly review:** compare A vs B and the two B openings; say which trials graduated.

### Trial pipeline (daily task "Golf trial reels daily run")
1. List `/Golf Captions`; new = file IDs not in state/trials.json. Relay a few at a time (only what
   the next 3 days need, plus 2 spare) via `inbox/want_trials.txt`; wait for "Fetch inbox videos";
   copy files out of inbox/trials, `git rm -r inbox/trials`, commit, push.
2. Check against A's existing reels: try pulling A's Instagram media (analytics_get_analytics for
   A's account, source "all", or posts_list for that profile) and compare thumbnails/captions/
   length. If it can't be checked, treat the reel as new for A.
3. Make the versions: A = original (scale 1080x1920, ~4.5 Mbps, shirt wipe first) or, if already
   on A, a different edit that still opens on the wipe. B = clean edit, no wipe (opening per rules).
   Covers: plain strongest frame, no text. Save to trials/NNN_slug_{a,b}.mp4 + _{a,b}_cover.jpg.
4. Schedule: keep 3 days of slots filled on each account (A now, B 2-4 days after that reel's A
   post). posts_create_post with the account's exact ID and trialParams. Record in
   state/trials.json.
5. Fix it yourself rules apply. Then message Mack in the same short format as the main run.

## Files
- Finished clips: queue/NNN_slug.mp4, queue/NNN_slug_cover.jpg, queue/NNN_slug_full.mp4
- Stories: stories/story_NNN.mp4
- Media is served to Zernio from raw.githubusercontent.com/mack-fitz/clips/main/...

## Fix it yourself (Mack's standing rule)
Mack should never have to tell you to circle back. Every run, before messaging him:
- **Failed posts:** find them (posts_list_failed, and any post in this account's schedule whose
  status is failed/error). Fix the cause (re-encode or shrink media, swap a broken media URL for a
  pinned-commit raw URL, re-crop, shorten a caption) and reschedule into the next open slot, or the
  same slot if it hasn't passed. Retry transient errors once; if it fails again, change approach.
- **Empty slots:** every slot for the next 3 days must have a post. Fill any gap.
- **Bad content:** anything that breaks the rules here (AI tells, wrong crop, cut mid-word, any
  added text on the video) gets replaced or re-edited before it goes out.
- **Disconnected account / expired token:** this is the one thing you can't fix — tell Mack
  exactly what to reconnect.
- In the message, report fixes as done ("Thursday 8pm was empty — filled it with X"), not as
  questions. Only ask Mack for things you truly can't do.

## Mack's review
Everything scheduled shows on the dashboard's "Up next" queue. Mack may look and ask for changes
in chat; if he says nothing, proceed as planned. Never wait on his approval to post.

## Daily pipeline (what the scheduled task does, in order)
1. Clone this repo (add_repo mack-fitz/clips with push access, then git clone).
2. **Pull new videos:** list Dropbox folder `/golfclips` (Dropbox connector). Skip file IDs in
   `state/processed.json`. Photos (selfies) go to the story queue, videos to the reel queue.
   My workspace can't download from Dropbox directly, so relay through GitHub: write the new
   file NAMES (one per line, names only, never URLs) to `inbox/want.txt`, commit, push. The
   `fetch-inbox` workflow downloads the shared folder using the DROPBOX_FOLDER_URL repo secret and
   puts those files in `inbox/videos/` (re-encodes >95 MB). Never commit Dropbox links (GitHub
   blocks the push). Poll `git fetch` until the "Fetch inbox videos" commit lands, pull, check
   `inbox/failed.txt`, copy the files out, then `git rm -r inbox/videos inbox/failed.txt`, commit,
   push (don't leave raw videos in the public repo).
3. **Edit each new video** (rules above). Look at a 1 fps contact sheet + a speech map
   (RMS per 0.1s) to plan cuts; snap cuts with `tools/snap.py`; render with
   `tools/render.sh src segs.json "" "" out.mp4` (segments `[start,end,zoom]`, zoom=1 punches
   in 15%; no text on the video). Make the cover (shirt-wipe frame + rotating grid text style,
   see the Cover bullet above). Make the uncut X/TikTok version
   (scale 1080x1920, ~4 Mbps). Make a 15s story teaser from the original (shirt wipe if present)
   with a dumb one-liner at y≈1450. Save to queue/NNN_slug{.mp4,_cover.jpg,_full.mp4},
   stories/story_NNN.mp4; commit + push. Add each Dropbox ID to state/processed.json.
4. **Schedule:** 2 reels per day, one midday (11:30–1:00 MT) and one evening (5:00–7:00 MT),
   varied minutes. Instagram = edited clip + cover + caption; X + TikTok = uncut + same caption
   (TikTok settings in the X/TikTok section). Story teaser at the same time as each IG reel
   (platformSpecificData.contentType "story"). Use Zernio `posts_create_post` with
   `scheduled_for` in UTC (MT = UTC−6 during daylight time, UTC−7 after Nov 1).
   Never schedule more than 2 reels on one day; extra clips wait for the next open slots.
   Keep a schedule list in `state/schedule.json` (date, slot, clip, Zernio post IDs).
5. **Dashboard** (https://claude.ai/artifact/WJAWEJC8DtJ9gipbhFCGbe): add each new post's Zernio
   post ID + tags to the clips file (opening, length_s, version, posted_mt) and refresh the
   queue file (unposted clips, days left at 2/day). Upload the new JSON as an asset, then update
   `datasets/clips` / `datasets/queue` url+updated (read the dataset first for if_version).
   **Up next:** every slot in state/schedule.json keeps `caption` (and `note` when there's
   something to say, e.g. "re-edited: cut was mid-word"). After any scheduling change run
   `python3 tools/upnext.py /tmp/upnext.json`, upload it as an asset to the dashboard, and update
   `datasets/upnext` source.url + updated (read it first for if_version).
6. **Daily summary** (send with SendUserMessage so it's delivered): yesterday per platform
   (views, avg watch, follows), best + worst post, what's scheduled today, queue days left,
   anything wrong (failed posts, disconnected account, reach drop). Warn when < 7 days of
   content remain. Keep it short and plain.
7. **Sundays:** also write the weekly review (good / bad / changes / 3–5 content ideas based on
   what's performing + current golf content formats), add it to the reviews file on the
   dashboard, and include it in the message. Remind Mack to check Instagram Account Status.

Already processed before the task existed: clips 001–002 (from chat uploads).

## YouTube promo clips
- Mack (she/her) will send new YouTube golf videos to cut into vertical promo clips.
- REMINDER to send her (in the daily message) whenever a long or horizontal YouTube video shows up
  in Dropbox without a matching .srt: upload the clean video to YouTube with no burned-in captions,
  let YouTube auto-caption it, fix the captions in Studio, then download the .srt and drop it in
  Dropbox next to the video. Use the .srt to burn captions into the promo clips in reel style.
- Promo text on clips: "full video on my yt" style. Still no links in captions.

## Macky To Do page
**Macky To Do** (https://claude.ai/artifact/NkJnRhgLLfSWz1XXfHbQ79): every run, ArtifactData `update` this account's doc in collection `queues` with `days_left` (number), `detail` (one plain line: what is left and the pace) and `updated` ("Mon D"). Sundays: add 2-3 new docs to `ideas` (fields order, title, where, effort, what, why) that fit Mack's masc/dry/silly vibe. Doc id(s) for this repo: golf-page.

Base Camp schedule (same page): every run, ArtifactData `set` collection `schedule`, doc id(s) golf, to `{items: [{date: "YYYY-MM-DD" (Mountain), time: "HH:MM" 24h Mountain, caption, where?}]}` covering today and tomorrow for that account. The page is now named "Base Camp".

## @moremackygolfs only posts footage Mack has ALREADY posted (Mack's rule, Oct 12)
Never give @moremackygolfs a video Mack hasn't posted himself. Unused footage is reserved for the
trial accounts (@mackygolfs / @mackthegolfer). Before scheduling any clip, confirm it matches a post
on @mackygolfs or @mackthegolfer (analytics_get_analytics with profile_id 6acce3f0662265cf261fca4a
and 6acce6402daf1733722343d0, source "all", paginate: compare videoDurationSeconds within 2 s plus
the content/caption). No match = treat as unused: don't post it here, add its Dropbox ID to
state/processed.json with note "unused -> trials", and tell Mack in the summary.
(Oct 12: 010_wrong-clubs had no match and was pulled from Oct 14.)

## Bought engagement — exclude from analytics (Mack, Oct 12)
Mack bought engagement for Instagram @moremackygolfs on Oct 12 (night): 300 followers, 1,000 views, 100 likes, arriving gradually over roughly Oct 13–17. None of it counts as real performance:
- Followers: on the next run, record the follower count in state/bought.json as the baseline (date + count) if not already there. UPDATE: all 300 bought followers landed at once on Oct 12 ~10:40pm Mountain. Mack had 0 followers before buying, and the count was 442 right after (Oct 12 ~10:40pm MT) — the seller over-delivered. Treat all 442 as bought: real followers = current count − 442. If the count drops in later days, that's Instagram purging bought accounts, not lost fans — say so. Label it "real growth (excl. bought)". Never cite the raw jump as a win.
- Views/likes: the 1,000 views and 100 likes may land on one or several posts. Any @moremackygolfs post published before Oct 13 whose views or likes jump unusually between runs during Oct 13–17 is marked `inflated: true` in state/schedule.json (note how much). Subtract up to 1,000 views and 100 likes total across those posts. Leave inflated posts out of best/worst post, averages, and any "what's working" conclusions; mention them as "excluded (bought)".
- Dashboards (Clip Page Stats): same exclusions; add a note line "Excludes bought engagement (Oct 12: 300 followers, 1,000 views, 100 likes)".
- Applies only to @moremackygolfs. X/TikTok @mackygolfs and the trial accounts are unaffected.

- NEVER cut swearing or profanity out of any edit (Mack, Oct 13).

## Base Camp queue count (Mack, Oct 13)
golf-page days_left = edited clips ready ÷ 3 per day; warn_under_days 2 (the page refills from Mack's ~130 already-posted videos, so it is never "out" — note the source count in detail).

- NEVER CUT OUT SHOTS (Mack, Oct 13): every golf shot/stroke in the source must stay in the edit (tee shots, approaches, chips, every putt, penalty drops). Her comments refer to them, so cutting a shot makes the talking make no sense. Only cut dead air, walking, waiting, ball-searching and pauses between sentences. This applies to every account and every edit, including re-edits and compilations.

## 3 reels a day + untouched originals for X/TikTok (Oct 14 run)
- @moremackygolfs now runs 3 reels/day: morning 8:00–9:30, midday 11:30–1:00, evening 5:00–7:00 MT (varied minutes), never more than 3. Keep 3 days scheduled. Each reel keeps its X/TikTok post + IG story at the same time.
- X/TikTok uncut = Mack's untouched original file (queue/NNN_slug_orig.{mov,mp4}, byte-identical copy of the Dropbox file), set per platform with posts_update_post / posts_create_post `customMedia` on the tiktok entry.
- X doesn't take HEVC, and GitHub raw can't host files over 100 MiB: in those cases use ONE high-quality H.264 export from the original (queue/NNN_slug_x.mp4: libx264 crf 18, maxrate 9.5M, preset slow, source fps, audio copied). X gets _x.mp4 when the original is HEVC; TikTok gets _x.mp4 only when the original is over 100 MiB.
- The workspace can't reach media.zernio.com / R2 presigned uploads (proxy), so media is always served from pinned-commit raw.githubusercontent.com URLs.
- Cover style order must still alternate after any reshuffle (no two consecutive posts with the same style).
- HARD RULE (Mack, Oct 14): @moremackygolfs may only use footage Mack has truly already posted — prove it by naming the exact post (account, date, caption, link) containing >= 15 s of that source, from mackygolfs-mackthegolfer state/posted_index.json. Compilation bits and our own trial posts don't count. If you can't name the post, the video is NEW and is off-limits here.

## FACEBOOK PAGE (Mack, Oct 14) — 3 posts/day, starts Oct 15
- Account: Facebook PAGE "macky.golfs", Zernio account 6ad052a5a442d9968f306c31. HARD RULE: Facebook posts go ONLY to this account id — never any other Facebook account, never Mack's personal profile. Always pass account_id explicitly; if Zernio ever lists more than one Facebook account, stop and ask Mack.
- Format: Facebook Reels (vertical 9:16), clean files, no watermarks, no added text (except shorties, which already carry their one line). Captions short, clean, dry, lowercase; optionally ONE hashtag (#golf); a question ("guess my score", "what would you hit here?") is good on FB. Never mention OnlyFans in captions (the Page bio is Mack's business).
- 3 a day (Mountain): morning 7:30–9:00, lunch 11:30–1:00, evening 6:30–8:30.
  - Morning + lunch = 2 UNEDITED originals (Mack's untouched files — the same ones that go/went to TikTok; same day or a day after is fine). Facebook doesn't penalize cross-platform reposts of clean files.
  - Evening = 1 already-approved EDIT, COMPILATION or SHORTY that has already posted elsewhere (mackygolfs-mackthegolfer review db: decision approved / status posted; or a published @moremackygolfs edit). Never anything Mack hasn't approved.
- Never the same video twice on the Facebook Page within 30 days. Keep 3 days scheduled. Track FB posts in state/schedule.json with platform "facebook".
- Reporting: include Facebook (views, watch time, follows, comments) in the daily summary, Base Camp schedule (doc "facebook") and queues (doc "facebook-page": days of content left; warn under 2), and the Clip Page Stats dashboard.
- SOURCE FOLDERS — HARD RULE (Mack, Oct 14, "EVER"): NEVER pull from, download, relay, fingerprint or post anything from any Dropbox folder other than /Golf Captions and /golfclips. No other folder, for any account (Facebook included), ever. Other folders (tracer folders, batches, /Golf, etc.) are off-limits. The Facebook Page pool = already-posted videos from those two folders + approved edits/compilations/shorties; never-posted videos wait until they've posted on Instagram first.
- Never-posted videos (mackygolfs-mackthegolfer state/never_posted.json) stay off Facebook and TikTok until they've posted on Instagram first.
- TIKTOK GETS EVERY ORIGINAL (Mack, Oct 14): every one of Mack's original videos from /Golf Captions and /golfclips must end up on TikTok (@mackygolfs, uncut original, X alongside as usual). Track which originals have been on TikTok (state/schedule.json + TikTok Studio list) and work through the ones that haven't. Never-posted videos go to TikTok 1–2 days AFTER their Instagram trial posts (not before). This includes the red Hawaiian shirt batch: TikTok on the day after each one's IG post (Sat 17 → Sun 18, Sun 18 → Mon 19, Mon 19 → Tue 20, Tue 20 → Wed 21, Wed 21 → Thu 22, Fri 23 → Sat 24), and the already-posted one (Sep 21 7:24:34 PM, "pent-bogey") can go anytime. Keep TikTok at about 3 a day; when the @moremackygolfs pairing runs short, fill TikTok with originals that haven't been on TikTok yet. Only post a never-posted video to TikTok once its IG post is confirmed published.
- FB mechanics (Oct 15 run): Zernio caps Facebook Reels at 3–60 s, so originals over 60 s can't go as untouched Reels. Schedule with `posts_create_post` (call_tool): platforms [{platform "facebook", accountId 6ad052a5a442d9968f306c31, platformSpecificData {contentType "reel"}}], `scheduled_for` local + `timezone` "America/Denver", media = pinned-commit raw URL (originals: mackygolfs-mackthegolfer inbox/videos at commit 0125bc5, sizes checked against Dropbox). Each original needs a named >= 15 s post (posted_index.json / fp/full_pairs.json); golfclips 004, 008, 012, 015 have no such post in the fingerprint data yet, so they're not used.
- **Facebook Stats** (https://claude.ai/artifact/Gi1E2KeRzd1XpBSVB3jicU, Macky HQ hole 8): the daily run keeps it current — its followers + per-post stats are live Zernio queries on account 6ad052a5a442d9968f306c31 (same mechanism as the stats on Clip Page Stats / Mackygolfs Stats), so there is no file to upload; just confirm it still loads and fix the page if Zernio changes its answer.
