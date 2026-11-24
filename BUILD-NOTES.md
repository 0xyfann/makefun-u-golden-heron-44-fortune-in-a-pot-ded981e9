# Build notes — Fortune in a Pot

- Read RULES.txt + competition.yaml first: gate is 1–120 chars of UTF-8
  text in /output/entry.txt, one line; judge is a gardener persona
  weighing (1) fortune for a houseplant, (2) funny for a plant lover,
  (3) kind, (4) fortune cadence, (5) clean single line.
- v1 fortune: "A sunbeam is coming for your favorite leaf, and soon your
  keeper will brag about you to every guest who visits." — 111 chars,
  local test passed.
- v1 -> v2 revision: tightened the fortune cadence ("will land") and made
  it more specific to this plant in this window ("pride of the
  windowsill") instead of generic bragging to guests.
- v2 final: "A sunbeam will land on your favorite leaf, and your keeper
  will tell every guest you are the pride of the windowsill." — 117 chars.
- Local test: `mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py`
  -> out/entry.txt, 117 chars, 1 line, non-whitespace; out/ removed after.
- main.py: Python stdlib only, asserts 1–120 chars before writing.
