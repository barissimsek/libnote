"""This is the music theory module.

This module provides functions related to basic music theory.
"""

__author__ = 'Baris Simsek'

_chromatic = ('A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#')

_scalemap = {
	"maj":  [0, 2, 2, 1, 2, 2, 2, 1], # Major intervals starting from the root note
	"minn": [0, 2, 1, 2, 2, 1, 2, 2], # Natural minor intervals starting from the root note
	"minh": [0, 2, 1, 2, 2, 1, 2, 2], # Harmonic minor intervals starting from the root note
	"minm": [0, 2, 1, 2, 2, 1, 2, 2]  # Melodic minor intervals starting from the root note
}

# Chromatic returns chromatic scale
def chromatic():
	return _chromatic

# Scale returns the scale fomula for a given mode
def _scale_formula(mode):
	if mode in _scalemap:
		return _scalemap[mode]

	return None

# Get returns triads for the given chord
def chord(t, root):
	c = [None]*3
	s = scale(t, root)

	c[0] = s[0]
	c[1] = s[2]
	c[2] = s[4]

	return c

# List returns all chords and triads
def chords():
	m = {}

	for root in _chromatic:
		m[root + 'maj'] = chord('maj', root)
		m[root + 'min'] = chord('minn', root)

	return m

# Get returns the scale for a given note
def scale(s, root):
	scale = []
	i = _chromatic.index(root)

	# Choose interval formula
	formula = _scalemap[s]

	# Generate scale from intervals
	for j in range(8):
		i = (i + formula[j]) % 12
		scale.append(_chromatic[i])

	return scale

# List returns major and minor scales for all notes
def scales():
	m = {}

	for root in _chromatic:
		m[root + 'maj'] = scale('maj', root)
		m[root + 'min'] = scale('minn', root)

	return m
