import notes_to_chroma


# Inputs
# chord_name: string of chord name output by melisma (e.g., C)
# notes_in_segment: list of strings of notes in segment(e.g., C D E F G E C B D C)
# lowest midi_note: int
# Outputs:
# Inversion <int>: root=0, 1st_inv=1, 2nd_inv=2, 3rd_inv=3

def inversion_calc(chord_name, lowest_midi_note):
    midi_chroma = int(lowest_midi_note) % 12
    # Base Case: Root inversion (if we don't know)
    if (chord_name[1] != "b") and (chord_name[1] != "#"):
        bass_note_chroma = notes_to_chroma.ntc(chord_name[0])
    else:
        bass_note_chroma = notes_to_chroma.ntc(chord_name[0:1])
    # Calculate inversion based on "distance" from bass note

    # Normalize so we don't have any "wrapping around" issues with modulo arithmetic
    midi_chroma = int(midi_chroma)
    bass_note_chroma = int(bass_note_chroma)
    # print "Midi Chroma:"+str(midi_chroma)
    # print "Lowest chroma:" +str(bass_note_chroma)

    if (midi_chroma - bass_note_chroma) == 0:
        return "0"

    if (midi_chroma - bass_note_chroma) == 4 or (midi_chroma - bass_note_chroma) == -8:
        return "1"

    if abs(midi_chroma - bass_note_chroma) == 7 or (midi_chroma - bass_note_chroma) == -5:
        return "2"

    if abs(midi_chroma - bass_note_chroma) == 10 or (midi_chroma - bass_note_chroma) == -2:
        return "3"

    if abs(midi_chroma - bass_note_chroma) == 11 or (midi_chroma - bass_note_chroma) == -1:
        return "3"

    return "0"  # Default to root inversion

    # print inversion_calc('Fmaj',0)
