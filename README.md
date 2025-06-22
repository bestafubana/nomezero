# Random Two‑Word Name Generator

This repository lets you mint quirky GitHub‑style project names using terms drawn from **Ultima Online**, **Dragon Ball**, **Naruto**, several rock bands’ one‑word song titles, and a sprinkling of old Brazilian slang.

## Files

| Path             | Purpose                                             |
| ---------------- | --------------------------------------------------- |
| `word_pool.yaml` | Human‑friendly master list (edit here first).       |
| `name_gen.py`    | Stand‑alone generator script (no third‑party libs). |

> **Note**  `name_gen.py` keeps an *embedded* copy of the word list so it can run with just the Python standard library.  Whenever you add or remove entries in `word_pool.yaml`, remember to **mirror the change** inside `name_gen.py` (or swap the script over to a YAML parser like `pyyaml` in the future).

## Quick start

```bash
# clone / pull repo, then:
python name_gen.py           # → britain-kamehameha (example)
python name_gen.py 5         # prints five random names
```

## How it works

1. Script deduplicates the embedded list at runtime.
2. Picks two **distinct** words uniformly at random.
3. Normalises to lowercase ASCII, strips punctuation, and joins with `-`.

## Extending the pool

1. Open `word_pool.yaml` and add / remove items.
2. Copy the same changes into the `WORDS` list near the top of `name_gen.py`.
3. (Optional) run a quick count:
   ```bash
   python - <<'PY'
   import name_gen, itertools
   n = len(name_gen.WORDS)
   print('total words:', n)
   print('2‑word combos:', n*(n-1))
   PY
   ```

## License

GPL 3.0 - do whatever, but keep it open-source.

