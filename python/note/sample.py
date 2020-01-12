#!/usr/local/bin/python3

import pprint
import stream

s = stream.create(48, 120)

t1 = s.track("guitar", 8, 4)
t2 = s.track("drum", 8, 12)

b1 = t1.bar()
b2 = t1.bar()

bend = '{"root": "C", "form": "1", "range": "2" }'
slide = '{"range": "4"}'

b1.sound('bend', bend)
b1.sound('slide', slide)

print(b1.sounds[0])
print(b1.sounds[1])
