# Ingest checkpoint — Oct 20 golfclips batch (68 reels)

Read this first after a container restart. Update after every step.

## Done
- [x] Both repos re-cloned blobless + sparse (no *.mp4/*.mov/*.part checked out) to free disk (was 913 MB free -> 27 GB).
      Re-clone recipe: `git clone --depth 1 --filter=blob:none --no-checkout URL; git sparse-checkout init --no-cone;`
      `.git/info/sparse-checkout` = `/*  !*.mp4 !*.mov !*.MOV !*.MP4 !*.part[0-9][0-9] !*.m4v`; `git checkout main`.
      tools/build_media_map.py now lists dirs via `git ls-files` too (lsdir), output unchanged.

## Next
- [ ] 1 list /golfclips
- [x] 1 Listed /golfclips (83 files, 1 page): 68 new (all modified 2026-10-20, none in processed.json). Listing: state/golfclips_listing_oct20.tsv
- [x] 2a Byte dedupe by Dropbox content_hash: 13 within-batch twins, 4 identical to existing sources -> 51 new unique contents
      (state/ingest_twins_oct20.json). All 55 reps size-match files fingerprinted earlier from Dropbox /Golf (whole /Golf folder
      was copied in). Not using those /Golf fingerprints (off-limits folder); re-fingerprinting the /golfclips copies.
- [~] Runner: .github/workflows/ingest.yml (clips) pushed with inbox/ingest.txt (55 reps) -> state/ingest/{info,fp,transcripts,sheets,frames}
- [x] COORDINATOR (Oct 20): step 7 CANCELLED. Nothing from /golfclips (old or new) ever goes to @mackygolfs/@mackthegolfer.
      Don't touch main-account schedule or the review page (another agent owns them). HARD RULE 12 added to both PLAYBOOKs;
      processed.json clip_pages_only; sources.json clip_pages_only flag; inventory.py --free skips; check_repeats --candidates fails.
      No-proof clips are skipped for @moremackygolfs too -> list them in the report.
- [x] posted_index refreshed (3 new posts fingerprinted, Oct 19-20).
- [x] WORK DIR MOVED: another agent edits /home/claude/clips + /home/claude/mackygolfs-mackthegolfer concurrently (main
      accounts, 30-day window). All ingest work happens in /home/claude/ingest/{clips,mackygolfs-mackthegolfer} (same sparse
      recipe); export CLIPS_REPO=/home/claude/ingest/clips MG_REPO=/home/claude/ingest/mackygolfs-mackthegolfer.
      Always `git pull --rebase` before commit; never touch the other agent's files.
- [x] Tooling: tools/captions.py (Mack caption style -> .ass), render.sh SUBS=, relay.yml (scratch/relay branch).
- [x] 2b Fingerprints (runner, ingest.yml -> state/ingest/fp) matched locally vs 332 posts + all sources:
      68 files = 55 unique contents (13 byte twins) = 40 distinct reels (4 contents byte-identical to existing
      sources; fingerprint same-reel groups at >= 60 % overlap). 20 reels brand-new to the library, 20 = alt files
      of reels already in the library. Registry: state/golfclips_oct20_sources.json (+ state/ingest_groups_oct20.json).
- [x] 4 Proof posts (Mack's own posts, posted_index refreshed Oct 20): 28 reels with proof, 12 without.
- [x] 5 Captions: only 3 batch files carry Mack's captions (all byte twins of existing GC files). Style documented in
      PLAYBOOK "CAPTION STYLE (Oct 20)"; tools/captions.py. Parakeet (/home/claude/tools/stt) used as 2nd opinion.
- [x] Fixed check_repeats external_uses: only walks GC top level + golfclips (Golf/ fp overwrote GC '9 02 57 AM.mp4');
      dropped the wrong cached match (DeW6yirRVE_ "absolutely brutal") from external_sources.json.
- [~] 6 Edits (work dir /home/claude/ingest/work/edits, sources /home/claude/ingest/orig):
      Oct 20: 022 hole-in-one-day (G4) | 023 malibu-bet (G22) | 024 gorgeous-day (G29)  + X-only originals
      Oct 21: 025 amarillo-missing-flag (G1) | 029 cart-path-only (G3) | 027 singing-par-5 (G28)
      Oct 22: 028 san-angelo-par-3 (G14) | 026 chili-cheese-dog (G21) | 030 soaking-wet-par-5 (G2) + X+TikTok originals
      FB: Oct20 am G18 orig (8 36 20), pm comp2_delusional_r6 | Oct21 lunch G19 orig (5 01 57), pm shorties/hero-shot_r3 |
          Oct22 am G20 orig (5 07 02), lunch G34 orig (10 51 47), pm comp13_asmr-golf_r3
      (G33 seven-iron 52 s: can't reach a 25 % cut without cutting shots -> spare FB original.)
- [x] Scheduled (ids in /home/claude/ingest/work/posted.json): FB x7 (Oct 20-22); IG 022 023 024 (Oct 20), 029 (Oct 21 12:04),
      028 026 030 (Oct 22). Still to do: IG 025 (Oct 21 08:28) + 027 (Oct 21 17:36) after render; stories x9; X-only Oct 20
      (022/023/024 _x); X+TikTok Oct 22 (028/026/030 _x; TikTok 026 = original .mov); processed.json; schedule.json; sync;
      Base Camp; Up next; scratch/relay branch delete.
- [x] All posts scheduled (IG 9 + stories 9, X 6, TikTok 3, FB 7; ids /home/claude/ingest/work/posted.json); schedule.json slots added.
      scratch/relay deleted. Trials 045/046/048/050/051 flagged by the guard came from the morning pull; coordinator confirms
      they are no longer in Zernio -> a fresh pull clears them (no code change).
- [ ] BLOCKED (approval prompt unanswered for reading the saved Zernio pull): sync_schedule.py, Base Camp schedule
      (golf, facebook) + queues (golf-page, facebook-page), Up next. Next run: pull posts_list_posts (every page) -> sync -> upnext.
