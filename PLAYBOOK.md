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
- Hook text: 2 short lines, white on black box, placed in the top fifth of the
  frame — LOW enough to clear the reel's audio info bar (not at the very top).
- Keep Mack's captions untouched (they sit mid-frame).
- Target length: tight, usually 30–70s depending on the story.
- Cover: strongest frame (action or reaction, never suggestive out of context),
  1–3 blunt words in big text inside the center square (grid crop).
- Export H.264 1080x1920, keep files small (~4–5 Mbps) so publishing is fast.

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
  built from the original, no top hook text.

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
- **Bad content:** anything that breaks the rules here (AI tells, wrong crop, cut mid-word, hook
  under the audio bar) gets replaced or re-edited before it goes out.
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
   `tools/render.sh src segs.json "hook line 1" "hook line 2" out.mp4` (segments
   `[start,end,zoom]`, zoom=1 punches in 15%). Make the cover (strongest frame + 1–3 blunt words,
   Poppins Bold 120px, white with black outline, y≈1150-1200). Make the uncut X/TikTok version
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
   post ID + tags to the clips file (opening, length_s, version, hook, posted_mt) and refresh the
   queue file (unposted clips, days left at 2/day). Upload the new JSON as an asset, then update
   `datasets/clips` / `datasets/queue` url+updated (read the dataset first for if_version).
   **Up next:** every slot in state/schedule.json keeps `caption` (and `hook`, `note` when there's
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
