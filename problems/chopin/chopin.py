import sys

d = {
    "Ab": "G#",
    "G#": "Ab",
    "F#": "Gb",
    "Gb": "F#",
    "D#": "Eb",
    "Eb": "D#",
    "C#": "Db",
    "Db": "C#",
    "A#": "Bb",
    "Bb": "A#",
}

for i,line in enumerate(sys.stdin):
    a, b = line.split()
    if a in d:
        print(f'Case {i+1}: {d[a]} {b}')
    else:
        print(f'Case {i+1}: UNIQUE')