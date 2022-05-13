#!/usr/bin/env python3

from pathlib import Path


class Corpus:

    def __init__(self, path: Path):
        """
        Load segments from a file, one per line.
        """
        with path.open(encoding='utf-8') as corpus:
            self.segments = [s.strip('\n') for s in corpus]

    def filter(self, min_alpha: float = 0.5):
        """
        Discard all segments with too few alphabetical characters.

        Keep only segments where at least `min_alpha` of the
        characters are alphabetic.

        Examples for min_alpha == 0.5:
            "So."      # keep
            "¡Sí!"     # keep
            "Ja!!!"    # discard
            "123.5"    # discard
        """
        pass  # TODO: Task 1

    def normalize(self):
        """
       import unicodedata

    def unicode_character_name(char):
        try:
            return unicodedata.name(char)
        except ValueError:
            return None

    # Generate all Unicode characters with their names
    all_unicode_characters = []
    for n in range(0, 0x10ffff):    # Unicode planes 0-16
        char = chr(n)               # Python 3
        #char = unichr(n)           # Python 2
        name = unicode_character_name(char)
        if name:
            all_unicode_characters.append((char, name))

    # Find all Unicode quotation marks
    print (' '.join([char for char, name in all_unicode_characters if 'QUOTATION MARK' in name]))
    # " « » ‘ ’ ‚ ‛ “ ” „ ‟ ‹ › ❛ ❜ ❝ ❞ ❟ ❠ ❮ ❯ ⹂ 〝 〞 〟 ＂ 🙶 🙷 🙸

    #  
    # Find all Unicode dashes
    print (' '.join([char for char, name in all_unicode_characters if 'DASH' in name and 'DASHED' not in name]))
    # ‒ – — ⁓ ⊝ ⑈ ┄ ┅ ┆ ┇ ┈ ┉ ┊ ┋ ╌ ╍ ╎ ╏ ⤌ ⤍ ⤎ ⤏ ⤐ ⥪ ⥫ ⥬ ⥭ ⩜ ⩝ ⫘ ⫦ ⬷ ⸺ ⸻ ⹃ 〜 〰 ︱ ︲ ﹘ 💨

        """
        pass  # TODO: Task 1

    def split(self, language: str = 'en'):
        """
        Split up segments containing multiple sentences using an online API.
        Remove any leading and trailing whitespace.

        Example:
            Before: self.segments = ["Wie geht's?", "Ausgezeichnet. Und dir?"]
            After:  self.segments = ["Wie geht's?", "Ausgezeichnet.", "Und dir?"]
        """
        pass  # TODO: Task 2
    


# TODO: Task 3
