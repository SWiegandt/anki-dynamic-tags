from aqt import mw
from .NoteTagger import NoteTagger
from anki.collection import _Collection
from anki.hooks import wrap


def init_tagger():
    config = mw.addonManager.getConfig(__name__)
    deck = config['deck']
    patterns = config['patterns']
    _tagger = NoteTagger(deck)

    for pattern in patterns:
        _tagger.register_pattern(pattern['pattern'], pattern['tag'])

    return _tagger


tagger = init_tagger()
_Collection.addNote = wrap(_Collection.addNote, lambda _, note: tagger.apply_tags(note), "before")
