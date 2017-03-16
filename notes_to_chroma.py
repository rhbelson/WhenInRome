# Inputs:
# note: string (e.g., C)
# Outputs:
# chroma_number: chroma numbers (e.g., 0)


def ntc(note):
    if note == 'C':
        return 0
    elif note == 'D':
        return 2
    elif note == 'E':
        return 4
    elif note == 'F':
        return 5
    elif note == 'G':
        return 7
    elif note == 'A':
        return 9
    elif note == 'B':
        return 11
    elif note == 'C#':
        return 1
    elif note == 'D#':
        return 3
    elif note == 'E#':
        return 5
    elif note == 'F#':
        return 6
    elif note == 'G#':
        return 8
    elif note == 'A#':
        return 10
    elif note == 'B#':
        return 0
    elif note == 'Cb':
        return 11
    elif note == 'Db':
        return 1
    elif note == 'Eb':
        return 3
    elif note == 'Fb':
        return 4
    elif note == 'Gb':
        return 6
    elif note == 'Ab':
        return 8
    elif note == 'Bb':
        return 10
    else:
        return 'Not a note'
