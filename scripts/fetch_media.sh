#!/usr/bin/env bash
# Download and unpack the full media bundle into ./media (~1.4 GB).
set -euo pipefail
cd "$(dirname "$0")/.." && mkdir -p media && cd media
B=https://d2ol7oe51mr4n9.cloudfront.net/user_3Kn2gmXeWEZVSCnsDtwLIgqwM2S
while read -r id sum; do
  f=$id.tar
  [ -f "$f" ] || curl -fL --retry 4 -o "$f" "$B/$f"
  echo "$sum  $f" | (sha256sum -c - 2>/dev/null || shasum -a 256 -c -)
  tar -xf "$f" && rm "$f"
done <<'LIST'
eeedaf59-1e80-4d57-8a8f-cdacfabb311e 60f3923172a14b3d03bdd28cce87ab098342f0dfd3e0a48fca55d09e984c985f
031b2e1a-5ad4-4654-ba70-469967ce39f0 c6a2acdb0e2882abc8350c00cf848da6f4d801d5f6330fe8b67cc4ebdc9066e5
4584566b-2421-46fb-b224-3dc0eb8add84 3eb32db1f522340b2751dbd9acd529fcbdab332b3bc1cebecb834f6fdb63345a
LIST
echo "Done. Media is in $(pwd)"
