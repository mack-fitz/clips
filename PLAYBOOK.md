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

## Phase 2 (trial reels)
- When IG follower count passes 200, try trial reels (retry up to 1,000).
- Then: 3 trials/day; next morning repost the best (watch time, shares, saves)
  as a regular reel with a new caption and cover.

## Files
- Finished clips: queue/NNN_slug.mp4, queue/NNN_slug_cover.jpg, queue/NNN_slug_full.mp4
- Stories: stories/story_NNN.mp4
- Media is served to Zernio from raw.githubusercontent.com/mack-fitz/clips/main/...

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
4. **Schedule:** 2 reels per day, one midday (11:30–1:00 MT) and one evening (6:00–8:00 MT),
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
