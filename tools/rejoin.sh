#!/bin/bash
# usage: tools/rejoin.sh DIR [OUTDIR]
# Rejoins files the fetch-inbox workflow split byte-for-byte (<name>.part00, .part01 ... +
# <name>.sha256) back into the untouched original <name>, verifies the sha256, then removes the
# parts. OUTDIR defaults to DIR. Exits non-zero if any checksum does not match.
set -e
DIR="$1"; OUT="${2:-$1}"; mkdir -p "$OUT"; rc=0
for sha in "$DIR"/*.sha256; do
  [ -f "$sha" ] || continue
  base="${sha%.sha256}"; name=$(basename "$base")
  ls "$base".part* >/dev/null 2>&1 || { echo "no parts for $name" >&2; rc=1; continue; }
  cat $(ls "$base".part* | sort) > "$OUT/$name"
  if [ "$(sha256sum "$OUT/$name" | cut -d' ' -f1)" = "$(cat "$sha")" ]; then
    echo "rejoined $name ($(stat -c %s "$OUT/$name") bytes, sha256 ok)"
    [ "$OUT" = "$DIR" ] && rm -f "$base".part* "$sha"
  else
    echo "SHA256 MISMATCH $name" >&2; rc=1
  fi
done
exit $rc
