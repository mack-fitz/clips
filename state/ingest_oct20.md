# Ingest checkpoint — Oct 20 golfclips batch (68 reels)

Read this first after a container restart. Update after every step.

## Done
- [x] Both repos re-cloned blobless + sparse (no *.mp4/*.mov/*.part checked out) to free disk (was 913 MB free -> 27 GB).
      Re-clone recipe: `git clone --depth 1 --filter=blob:none --no-checkout URL; git sparse-checkout init --no-cone;`
      `.git/info/sparse-checkout` = `/*  !*.mp4 !*.mov !*.MOV !*.MP4 !*.part[0-9][0-9] !*.m4v`; `git checkout main`.
      tools/build_media_map.py now lists dirs via `git ls-files` too (lsdir), output unchanged.

## Next
- [ ] 1 list /golfclips
