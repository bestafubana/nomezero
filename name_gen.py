#!/usr/bin/env python3
"""Simple two‑word GitHub‑style name generator (no external libraries).

Usage:
    python name_gen.py           # prints one name
    python name_gen.py 5         # prints 5 names

The word pool is embedded below.  Edit it or regenerate from `word_pool.yaml`
if you keep that file as the canonical list.
"""

import random
import re
import sys
import unicodedata

# ---------------------------------------------------------------------------
# WORD POOL (flattened to one list for speed and simplicity)
# ---------------------------------------------------------------------------

WORDS = [
    # Ultima Online
    "britain","trinsic","vesper","minoc","moonglow","skara","yew","jhelom",
    "nujelm","felucca","trammel","compassion","honesty","valor","justice",
    "sacrifice","spirituality","humility","hythloth","despise","deceit",
    "covetous","destard","shame","wrong","wisp","lich","balron","reaper",
    "invisibility","explosion","fireball","lightning","heal","resurrect",
    "earthquake","magery","blacksmithing","tailoring","carpentry","alchemy",
    "hiding","stealth","lockpicking","anatomy","swordsmanship","parry",
    "archery","mining","cartography",

    # Dragon Ball (no underscores, master_kai etc. pruned)
    "piccolo","vegeta","krillin","tien","yamcha","chiaotzu","gohan","trunks",
    "bulma","chichi","videl","pan","broly","beerus","whis","frieza","cell",
    "buu","roshi","yajirobe","namek","capsule","nimbus","saiyan","shenron",
    "korin","puar","oolong","kamehameha","goten","senzu","dynocap","kienzan",
    "genkidama","taioken","kaio","kaioken","kibito","kai","saibaman",
    "zarbon","dodoria","guldo","recoome","jeice","burter","ginyu","kefla",

    # Naruto
    "kakashi","sakura","shikamaru","ino","choji","hinata","neji","rocklee",
    "tenten","gaara","temari","kankuro","jiraiya","tsunade","orochimaru",
    "itachi","kisame","pain","nagato","konan","madara","obito","konoha",
    "akatsuki","byakugan","sharingan","chidori","rasengan","shuriken","kunai",
    "chakra","hokage","kazekage","mizukage","raikage","tsuchikage",
    "rasenshuriken","amaterasu","tsukuyomi","susanoo","izanagi","izanami",
    "kamui","raikiri","hiraishin"

    # Songs (Foo Fighters, Beatles, Royal Blood, Decemberists)
    "aurora","generator","resolve","rope","run","walk","low","everlong",
    "razor","doa","congregation","help","yesterday","michelle","something",
    "girl","rain","blackbird","taxman","because","julia","revolution","sun",
    "typhoons","limbo","oblivion","boilermaker","honeybrains","summersong",
    "oceanside","severed",

    # Brazilian slang (regional)
    "bute","cranco","disgrama","disgruda","bobonica","bobatorrero","cafote",
    "minhanha","chaupisco","arrupio","tauba","platirera","ronquifussa",
    "raputenga","sambucelha","apois","falero","fulerage",
]

# Make sure words are unique (safe‑guard if list is edited manually)
WORDS = sorted(set(WORDS))

# ---------------------------------------------------------------------------

_slug_re = re.compile(r"[^a-z0-9]+")


def slugify(word: str) -> str:
    """Lowercase, remove accents, keep alnum only."""
    ascii_word = unicodedata.normalize("NFKD", word).encode("ascii", "ignore").decode()
    return _slug_re.sub("", ascii_word.lower())


def generate_name() -> str:
    """Return a two‑word slug like 'kakashi-reaper'."""
    w1, w2 = random.sample(WORDS, 2)  # unique picks
    return f"{slugify(w1)}-{slugify(w2)}"


def main():
    qty = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    for _ in range(max(1, qty)):
        print(generate_name())


if __name__ == "__main__":
    main()
