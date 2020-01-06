#!/usr/local/bin/python3

import pprint
import stream

s = stream.create(48, 120)

t1 = s.track("guitar", 8, 4)
t2 = s.track("drum", 8, 12)

b1 = t1.bar()
b2 = t1.bar()

bend = '{"form": "1", "range": "2" }'
slide = '{"range": "4"}'

n1 = b1.note('bend', bend)
n2 = b1.note('slide', slide)

# print(vars(n1))

# print(b1.notes)

print(n2)

