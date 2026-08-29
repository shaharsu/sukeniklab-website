#!/usr/bin/env bash
# Re-download every image from the original Wix CDN.
# scripts/images.tsv maps "local path <TAB> source URL". Crops from the Wix
# layout are preserved in the URL; sizes are upscaled ~3x from what Wix served.
# Existing files are skipped, so this is safe to re-run.
set -uo pipefail
cd "$(dirname "$0")/.."
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
ok=0; skip=0; fail=0
while IFS=$'\t' read -r dest url; do
  [ -z "$dest" ] && continue
  if [ -s "$dest" ]; then skip=$((skip+1)); continue; fi
  mkdir -p "$(dirname "$dest")"
  if curl -sfL -A "$UA" "$url" -o "$dest" && [ -s "$dest" ]; then
    ok=$((ok+1))
  else
    rm -f "$dest"; fail=$((fail+1)); echo "FAILED: $dest  <-  $url" >&2
  fi
done < scripts/images.tsv
echo "downloaded=$ok skipped=$skip failed=$fail"
