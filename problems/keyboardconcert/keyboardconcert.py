import functools
n, m = map(int, input().split())


note_to_instrument = {}
    
for i in range(n):
    notes = list(map(int, input().split()))
    for note in notes[1:]:
        if note not in note_to_instrument:
            note_to_instrument[note] = set()
        note_to_instrument[note].add(i)


music_notes = list(map(int, input().split()))

# loop through every instrument looking for instruments that could play the first loop
# for each one you call a function: find_instrument(curr_inst_idx: int, music_pos: int) -> int
# this function returns the minimum amount of changes needed to play the song

# I am going to store a 2d array where the first index is the music position and the 2nd is the current instrument
# that way i can store the best thing to do at that current moment

prev_results = []

for i in range(m):
    l = []
    for j in range(n):
        l.append(-1)
    prev_results.append(l)


def find_instrument(curr_inst_idx: int, music_pos: int) -> int:
    if music_pos >= len(music_notes):
        return 0
    

    if prev_results[music_pos][curr_inst_idx] != -1:
        return prev_results[music_pos][curr_inst_idx]
    
    note = music_notes[music_pos]
    stay = float('inf')

    if curr_inst_idx in note_to_instrument[note]:
        stay = find_instrument(curr_inst_idx, music_pos + 1)

    # if stay == 0:
    #     prev_results[music_pos][curr_inst_idx] = 0
    #     return 0
         
    move_on = float('inf')
    for instrument in note_to_instrument[note]:
        if instrument != curr_inst_idx:
            move_on = min(move_on, 1 + find_instrument(instrument, music_pos + 1))
    
    prev_results[music_pos][curr_inst_idx] = min(move_on, stay)
    return prev_results[music_pos][curr_inst_idx]


m = float('inf')
for instrument in note_to_instrument[music_notes[0]]:
    m = min(m, find_instrument(instrument, 1))

print(m)
