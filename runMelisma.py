import os
import time


def get_chords_and_pitches(midifile):
    os.system('melisma2003/mftextNEW/mftext ' + midifile + ' > new.notes')
    time.sleep(1)
    os.system('melisma2003/meter/meter new.notes | melisma2003/harmony/harmony > output.txt')
    time.sleep(1)

    ignore = ['Beat', 'Finished', 'Chord', 'TPCNote', 'Analysis:']

    nums = [str(x) for x in range(1, 10)]
    last_chord = None
    chords_and_pitches = []

    prev_chord = None
    chords_start_and_end = []
    chords_start_and_end_dict = {}
    dict_not_initialized = True
    lowest_note_in_chord = []

    with open('output.txt') as f:
        content = f.readlines()
        for row in content:
            chunks = row.split()
            chunks_c = row.split()
            chunks_n = row.split()

            if len(chunks_c) > 0 and chunks_c[0] == 'Chord':
                chunks_c = chunks_c[1:]

                if prev_chord is None or chunks_c[2] != prev_chord:
                    chords_start_and_end.append((int(chunks_c[0]), int(chunks_c[1])))
                    prev_chord = chunks_c[2]
                else:
                    tup = chords_start_and_end[-1]
                    chords_start_and_end = chords_start_and_end[:len(chords_start_and_end) - 1]
                    new_tup = (tup[0], int(chunks_c[1]))
                    chords_start_and_end.append(new_tup)

            if len(chunks_n) > 0 and chunks_n[0] == 'TPCNote':

                if dict_not_initialized:
                    for t in chords_start_and_end:
                        chords_start_and_end_dict[t] = 99999
                    dict_not_initialized = False

                chunks_n = chunks_n[1:]

                for t in chords_start_and_end:
                    # if start time of note is at/after start of chord and end time of note is at/before end of chord
                    # then it was played during the segment of that chord
                    # check if it's the lowest midi value for that chord
                    if int(chunks_n[0]) >= t[0] and int(chunks_n[1]) <= t[1]:
                        if int(chunks_n[2]) < chords_start_and_end_dict[t]:
                            chords_start_and_end_dict[t] = int(chunks_n[2])

            if len(chunks) > 0 and chunks[0] not in ignore:
                # ----->>>>> added the dash to strip because of weird melisma output <<<<<----------
                chunks = [x.strip('>-x*<') for x in chunks]
                chunks = [x for x in chunks if
                          (x != '<' and x != '+' and x != 'x' and x != '|' and x != '' and x not in nums)]
                chunks = chunks[1:]

                # now first item is chord label, all items after that are pitches from that segment
                if last_chord is None or chunks[0] != last_chord:
                    if len(chunks) > 1:
                        chords_and_pitches.append((chunks[0], chunks[1:]))
                    else:
                        chords_and_pitches.append((chunks[0], []))
                    last_chord = chunks[0]
                else:
                    if len(chunks) > 1:
                        tup = chords_and_pitches[-1]
                        chords_and_pitches = chords_and_pitches[:len(chords_and_pitches) - 1]
                        new_tup = (tup[0], tup[1] + chunks[1:])
                        chords_and_pitches.append(new_tup)

    start_times = []
    for t in chords_start_and_end:
        lowest_note_in_chord.append(chords_start_and_end_dict[t])
        start_times.append(t[0])

    return chords_and_pitches, lowest_note_in_chord, start_times
