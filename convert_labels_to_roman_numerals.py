import csv
import inversion_calculator
import notes_to_chroma
import os
import pickle


# Inputs
# List<String> (Chords)
# String (desired_key)
# Output
# List<String>(Roman Numerals)
def label_to_rn(chords_in_segment, lowest_notes_in_chord, desired_key):
    labels_to_solfege = {}

    if os.path.isfile("labels_to_solfege.dat"):
        f = open("labels_to_solfege.dat", "r")
        u = pickle.Unpickler(f)
        labels_to_solfege = u.load()
        f.close()
    else:
        with open("labels_to_solfege.csv", 'rb') as labelsToSolfegeCsv:
            csv_reader = csv.reader(labelsToSolfegeCsv, delimiter=',')
            output_file = open('labels_to_solfege.dat', 'wb')
            for row in csv_reader:
                k = str(row[0])
                v = []
                for chroma in row[1:]:
                    v.append(int(chroma))
                labels_to_solfege[k] = v
            p = pickle.Pickler(output_file)
            p.dump(labels_to_solfege)
            output_file.close()

    solfege_to_roman_numerals = {}
    if os.path.isfile("solfege_to_roman_numerals.dat"):
        f = open("solfege_to_roman_numerals.dat", "r")
        u = pickle.Unpickler(f)
        solfege_to_roman_numerals = u.load()
        f.close()
    else:
        with open("solfege_to_roman_numerals.csv", 'rU') as solfege_to_roman_numeralsCsv:
            csv_reader = csv.reader(solfege_to_roman_numeralsCsv, delimiter=',')
            output_file = open('solfege_to_roman_numerals.dat', 'wb')
            for row in csv_reader:
                v = row[0]
                k = []
                for chroma in row[1:]:
                    k.append(int(chroma))
                k_tup = tuple(k)
                solfege_to_roman_numerals[k_tup] = v
            p = pickle.Pickler(output_file)
            p.dump(solfege_to_roman_numerals)
            output_file.close()

    chord_inversions = []

    # Pass in chords in segment, lowest notes, and give back inversion
    for i in range(len(chords_in_segment)):
        chord_inversions.append(inversion_calculator.inversion_calc(chords_in_segment[i], lowest_notes_in_chord[i]))

    chord_solfege = []
    # We know have 2 important lists: Chord, and inversion:
    for chord in chords_in_segment:
        chord_solfege.append(labels_to_solfege[chord])

    # Convert to Desired Key
    new_chords = []
    new_solfege = []

    new_key = notes_to_chroma.ntc(desired_key)
    for chord in range(len(chord_solfege)):
        # print chord_solfege[chord]
        for solfege in range(len(chord_solfege[chord])):
            x = chord_solfege[chord][solfege] - new_key
            if x < 0:
                x += 12
            # print x
            new_solfege.append(x)
        new_chords.append(new_solfege)
        new_solfege = []
    chord_solfege = new_chords
    # print chord_solfege

    # Shuffle Solfege
    for i in range(len(chords_in_segment)):
        tmp1 = [0] * len(chord_solfege[i])
        tmp2 = chord_solfege[i]
        inv = int(chord_inversions[i])
        for j in range(len(tmp2)):
            tmp1[(j - inv) % len(tmp2)] = tmp2[j]
        chord_solfege[i] = tmp1

    # #Test Inversions
    # print 'Inversions:'
    # for i in range(len(chords_in_segment)):
    # 	print chords_in_segment[i],chord_solfege[i]

    # Map to Roman Numerals
    roman_numerals = []
    for i in range(len(chord_solfege)):
        # rn = None
        try:
            rn = solfege_to_roman_numerals[tuple(chord_solfege[i])]
        except KeyError:
            rn = None
        roman_numerals.append(rn)
    return roman_numerals
