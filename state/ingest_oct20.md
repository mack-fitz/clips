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
