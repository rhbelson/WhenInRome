# Inputs:
# chords: will be chords from main.py
# num_transposition_steps: <int> that will ONLY be 1, or -1
# where 1 is transposition up a half step, and -1 is transposition down a half step
# Outputs:
# Transposed chords <list>
# transposition chroma


def transpose(pitch, num_transposition_steps):
    note = pitch
    if num_transposition_steps == 1:
        # Move whole harmonic progression up half step to remove all double flats

        # naturals
        if note == "C":
            note = "C#"
        elif note == "D":
            note = "D#"
        elif note == "E":
            note = "E#"
        elif note == "F":
            note = "F#"
        elif note == "G":
            note = "G#"
        elif note == "A":
            note = "A#"
        elif note == "B":
            note = "B#"
        # single sharps
        elif note == "C#":
            note = "D"
        elif note == "D#":
            note = "E"
        elif note == "E#":
            note = "F"
        elif note == "F#":
            note = "G"
        elif note == "G#":
            note = "A"
        elif note == "A#":
            note = "B"
        elif note == "B#":
            note = "C"
        # single flats
        elif note == "Cb":
            note = "C"
        elif note == "Db":
            note = "D"
        elif note == "Eb":
            note = "E"
        elif note == "Fb":
            note = "F"
        elif note == "Gb":
            note = "G"
        elif note == "Ab":
            note = "A"
        elif note == "Bb":
            note = "B"

        # double flats
        elif note == "Cbb":
            note = "Cb"
        elif note == "Dbb":
            note = "Db"
        elif note == "Ebb":
            note = "Eb"
        elif note == "Fbb":
            note = "Fb"
        elif note == "Gbb":
            note = "Gb"
        elif note == "Abb":
            note = "Ab"
        elif note == "Bbb":
            note = "Bb"

        # double sharps
        elif note == "C##":
            note = "D#"
        elif note == "D##":
            note = "E#"
        elif note == "E##":
            note = "F#"
        elif note == "F##":
            note = "G#"
        elif note == "G##":
            note = "A#"
        elif note == "A##":
            note = "B#"
        elif note == "B##":
            note = "C#"

        return note

    if num_transposition_steps == -1:
        # Move whole harmonic progression up half step down remove all double sharps

        # naturals
        if note == "C":
            note = "C#"
        elif note == "D":
            note = "D#"
        elif note == "E":
            note = "E#"
        elif note == "F":
            note = "F#"
        elif note == "G":
            note = "G#"
        elif note == "A":
            note = "A#"
        elif note == "B":
            note = "B#"
        # single sharps
        elif note == "C#":
            note = "D"
        elif note == "D#":
            note = "E"
        elif note == "E#":
            note = "F"
        elif note == "F#":
            note = "G"
        elif note == "G#":
            note = "A"
        elif note == "A#":
            note = "B"
        elif note == "B#":
            note = "C"
        # single flats
        elif note == "Cb":
            note = "C"
        elif note == "Db":
            note = "D"
        elif note == "Eb":
            note = "E"
        elif note == "Fb":
            note = "F"
        elif note == "Gb":
            note = "G"
        elif note == "Ab":
            note = "A"
        elif note == "Bb":
            note = "B"

        # double flats
        elif note == "Cbb":
            note = "Cb"
        elif note == "Dbb":
            note = "Db"
        elif note == "Ebb":
            note = "Eb"
        elif note == "Fbb":
            note = "Fb"
        elif note == "Gbb":
            note = "Gb"
        elif note == "Abb":
            note = "Ab"
        elif note == "Bbb":
            note = "Bb"

        # double sharps
        elif note == "C##":
            note = "D#"
        elif note == "D##":
            note = "E#"
        elif note == "E##":
            note = "F#"
        elif note == "F##":
            note = "G#"
        elif note == "G##":
            note = "A#"
        elif note == "A##":
            note = "B#"
        elif note == "B##":
            note = "C#"

        return note
