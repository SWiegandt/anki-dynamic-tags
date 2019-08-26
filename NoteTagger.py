import re

from anki.notes import Note
from aqt import mw


class TagPattern:
    def __init__(self, pattern, tag):
        self.pattern = pattern
        self.tag = tag

    def match(self, note: Note):
        if 'Notes' in note and re.search(self.pattern, note['Notes']):
            return True

        return False


class NoteTagger:
    def __init__(self, deck):
        self.patterns = []
        self.deck_name = deck

    def register_pattern(self, pattern, tag):
        self.patterns.append(TagPattern(pattern, tag))

    def get_deck_id(self):
        deck = mw.col.decks.byName(self.deck_name)

        if deck:
            return deck['id']
        else:
            return None

    def apply_tags(self, note: Note):
        if not note.model()['did'] == self.get_deck_id():
            return

        for pattern in self.patterns:
            if pattern.match(note):
                note.addTag(pattern.tag)
