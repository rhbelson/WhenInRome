import notes_to_chroma


# Inputs:
# chord_name: string of chord name output by melisma (e.g., C)
# notes_in_segment: list of strings of notes in segment(e.g., C D E F G E C B D C)

# Outputs:
# new_chord_name: str with chord name AND quality
# notes_in_segment: list of strings remains unchanged
def chord_quality_identifier(chord_name, notes_in_segment):
    chroma_segment = []
    new_chord_name = chord_name
    # print new_chord_name
    chord_features = []
    for n in notes_in_segment:
        x = notes_to_chroma.ntc(n)
        chroma_segment.append(x)
    chord_bass = notes_to_chroma.ntc(chord_name)
    # print chroma_segment

    for i in range(len(chroma_segment)):
        if (chroma_segment[i] - chord_bass == 3) or (chroma_segment[i] - chord_bass == -9):
            chord_features.append('me')

        if (chroma_segment[i] - chord_bass == 10) or (chroma_segment[i] - chord_bass == -2):
            chord_features.append('te')
        if (chroma_segment[i] - chord_bass == 6) or (chroma_segment[i] - chord_bass == -6):
            chord_features.append('se')
        if (chroma_segment[i] - chord_bass == 4) or (chroma_segment[i] - chord_bass == -8):
            chord_features.append('mi')
        if (chroma_segment[i] - chord_bass == 11) or (chroma_segment[i] - chord_bass == -1):
            chord_features.append('ti')
        if (chroma_segment[i] - chord_bass == 8) or (chroma_segment[i] - chord_bass == -4):
            chord_features.append('si')
        if (chroma_segment[i] - chord_bass == 7) or (chroma_segment[i] - chord_bass == -5):
            chord_features.append('sol')

        # print chord_features

    # Major/Augmented triads
    if 'mi' in chord_features:

        # Case 1: Clear Major Chords
        if 'sol' in chord_features:
            if 'ti' in chord_features:
                new_chord_name += 'maj7'
                return new_chord_name
            elif 'te' in chord_features:
                new_chord_name += '7'
                return new_chord_name
            else:
                new_chord_name += 'maj'
                return new_chord_name

        # Case 2: Augmented triads
        elif 'si' in chord_features:
            new_chord_name += 'aug'
            return new_chord_name

        # Case 3: Ambiguous Major Chords
        else:
            if 'ti' in chord_features:
                new_chord_name += 'maj7'
                return new_chord_name
            elif 'te' in chord_features:
                new_chord_name += '7'
                return new_chord_name
            else:
                new_chord_name += 'maj'
                return new_chord_name

    # Minor/Diminished triads
    elif 'me' in chord_features:

        # Case 1: Clear Minor Chords
        if 'sol' in chord_features:
            if 'te' in chord_features:
                new_chord_name += 'min7'
                return new_chord_name
            else:
                new_chord_name += 'min'
                return new_chord_name

        # Case 2: Diminished triads
        elif 'se' in chord_features:
            new_chord_name += 'dim'
            if 'te' in chord_features:
                new_chord_name += '7'
                return new_chord_name
            else:
                return new_chord_name

        # Case 3: Ambiguous Minor Chords
        else:
            if 'te' in chord_features:
                new_chord_name += 'min7'
                return new_chord_name
            else:
                new_chord_name += 'min'
                return new_chord_name

    elif 'sol' in chord_features:
        new_chord_name += 'maj'
        return new_chord_name
    else:  # <<<<<<<<<<---------- this is bad but i put it in just so it would run
        new_chord_name += 'maj'
        return new_chord_name

    # return new_chord_name
