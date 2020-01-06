"""This is the stream module.

This module describes a music stream and related data types and objects.

A stream is a data structure that can describe a music from beginning to end.
It's consist of parallel playing tracks. 
"""

__author__ = 'Baris Simsek'

class _note():
    def __init__(self, t, payload):
        self.type = t
        self.payload = payload

    def __str__(self):
        return "type: {}\npayload: {}\n".format(self.type, self.payload)

class _bar:
    def __init__(self):
        self.notes = []

    def __str__(self):
        return "notes: {}".format(self.notes)

    def note(self, t, *args):
        self.notes.append(_note(t, args))
        return self.notes[-1]

class _track:

    def __init__(self, name, start, length):
        self.name = name
        self.start = start
        self.length = length
        self.bars = []

    def __str__(self):
        return "name: {}\nstart: {}\nlength: {}\nbars: {}\n".format(self.name, self.start, self.length, self.bars)

    def bar(self):        
        self.bars.append(_bar())
        return self.bars[-1]

class _stream:

    def __init__(self, length, tempo):
        self.length = length
        self.tempo = tempo
        self.tracks = {}
    def __str__(self):
        return "length: {}\ntempo: {}\ntracks: {}\n".format(self.length, self.tempo, self.tracks)

    def track(self, name, start, length):
        if name in self.tracks:
            print("Track `{}` is already exist. Skipping...".format(name))
        else:
            self.tracks[name] = _track(name, start, length)

        return self.tracks[name]

def create(length, tempo):
    return _stream(length, tempo)

