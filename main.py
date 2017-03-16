import chord_quality_identifier
import chroma_to_notes
import convert_labels_to_roman_numerals
import csv
import notes_to_chroma
import os
import runMelisma
import sys
import transposition

if len(sys.argv) != 2:
    print "usage: python main.py [midifile]"
    quit()

args = sys.argv
midifile = args[1]
keys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

highest_score = 0
correct_key = ""
correct_romanNumerals = []
chordsAndPitches, lowestNotesInChord, start_times = runMelisma.get_chords_and_pitches(midifile)

# print start_times

# for i in chordsAndPitches:
#     print i

# Check if Transposition is Necessary: Get rid of funky chords
num_transposition_steps = 0
for l in range(len(chordsAndPitches)):
    if "bb" in chordsAndPitches[l][0]:
        num_transposition_steps = 1
        new_chords = []
        for i in range(len(chordsAndPitches)):
            new_chord_label = transposition.transpose(chordsAndPitches[i][0], num_transposition_steps)
            new_notes = []
            for note in chordsAndPitches[i][1]:
                new_notes.append(transposition.transpose(note, num_transposition_steps))
            new_chords.append((new_chord_label, new_notes))
        chordsAndPitches = new_chords
        break  # leave function
    if "##" in chordsAndPitches[l][0]:
        num_transposition_steps = -1
        new_chords = []
        for i in range(len(chordsAndPitches)):
            new_chord_label = transposition.transpose(chordsAndPitches[i][0], num_transposition_steps)
            new_notes = []
            for note in chordsAndPitches[i][1]:
                new_notes.append(transposition.transpose(note, num_transposition_steps))
            new_chords.append((new_chord_label, new_notes))
        chordsAndPitches = new_chords
        break  # leave function

# print chords

# update chordsAndPitches to reflect transposition
# if len(chords) > 0:
#     chordsAndPitches1 = []
#     for m in range(len(chordsAndPitches)):
#         chordsAndPitches1.append((chords[m], chordsAndPitches[m][1]))
#     chordsAndPitches = chordsAndPitches1

# for i in chordsAndPitches:
#     print i

for i in range(len(keys)):

    chordsWithQuality = []

    for j in range(len(chordsAndPitches)):
        chordsWithQuality.append(
            chord_quality_identifier.chord_quality_identifier(chordsAndPitches[j][0], chordsAndPitches[j][1]))

    # romanNumerals = convert_labels_to_roman_numerals.label_to_rn(chordsWithQuality, lowestNotesInChord, 'C')
    romanNumerals = convert_labels_to_roman_numerals.label_to_rn(chordsWithQuality, lowestNotesInChord, keys[i])
    # print 'key: ' + keys[i] + ';Roman Numerals: ',
    # print romanNumerals

    # Scoring Is Calculated Here
    num_minor_tonic = 0
    num_major_tonic = 0
    score = 0
    if romanNumerals[0]=="I":
        score+=5
    for k in range(len(romanNumerals)):
        if romanNumerals[k] is None:
            continue
        if romanNumerals[k][0] == "I":
            if len(romanNumerals[k]) > 1:
                if romanNumerals[k][1] != "I" and romanNumerals[k][1] != "V":
                    score += 1
                    num_major_tonic += 1
            else:
                score += 1
                num_major_tonic += 1

        if romanNumerals[k][0] == "i":
            if len(romanNumerals[k]) > 1:
                if romanNumerals[k][1] != "i" and romanNumerals[k][1] != "v":
                    score += 1
                    num_major_tonic += 1
            else:
                score += 1
                num_major_tonic += 1

        if romanNumerals[k][0] == "V" or romanNumerals[k][0] == "v":
            if len(romanNumerals[k]) > 1:
                if romanNumerals[k][1] != "i" and romanNumerals[k][1] != "I":
                    score += 1
            else:
                score += 1
        if romanNumerals[k][0:1] == "IV" or romanNumerals[k][0:1] == "iv":
            score += 1
        if romanNumerals[k][0:1] == "IV" or romanNumerals[k][0:1] == "iv":
            score += 1
        if k >= 0 and romanNumerals[k - 1] is not None and romanNumerals[k] is not None:
            if romanNumerals[k - 1][0] == "V" and romanNumerals[k][0] == "I":
                actuallyV = False
                if len(romanNumerals[k - 1]) > 1:
                    if romanNumerals[k - 1][1] != "I":
                        actuallyV = True
                else:
                    actuallyV = True
                actuallyI = False
                if len(romanNumerals[k]) > 1:
                    if romanNumerals[k][1] != "I" and romanNumerals[k][1] != "V":
                        actuallyI = True
                else:
                    actuallyI = True
                if actuallyV and actuallyI:
                    score += 2
            elif romanNumerals[k - 1][0] == "V" and romanNumerals[k][0] == "i":
                actuallyV = False
                if len(romanNumerals[k - 1]) > 1:
                    if romanNumerals[k - 1][1] != "I":
                        actuallyV = True
                else:
                    actuallyV = True
                actuallyI = False
                if len(romanNumerals[k]) > 1:
                    if romanNumerals[k][1] != "i" and romanNumerals[k][1] != "v":
                        actuallyI = True
                else:
                    actuallyI = True
                if actuallyV and actuallyI:
                    score += 2
    # print keys[i], score, romanNumerals
    if score > highest_score:
        highest_score = score
        correct_romanNumerals = romanNumerals
        correct_key = keys[i]

        # Check Transposition
        if num_transposition_steps == 1:
            orig_key = notes_to_chroma.ntc(correct_key)
            orig_key = int(orig_key + 1)
            correct_key = chroma_to_notes.ctn(orig_key)

        elif num_transposition_steps == -1:
            orig_key = notes_to_chroma.ntc(correct_key)
            orig_key = int(orig_key - 1)
            correct_key = chroma_to_notes.ctn(orig_key)

        if num_major_tonic > num_minor_tonic:
            correct_key += ' major'
        else:
            correct_key += ' minor'

os.system('midicsv-1.1/midicsv ' + midifile + ' > output.csv')

with open('output.csv') as midiCsv:
    csvReader = csv.reader(midiCsv, delimiter=',')
    outputFile = open('labeled_output.csv', 'wb')
    trackNumber = 0
    tempo = 0
    ppqn = 24
    endTime = 0
    start_times_in_ticks = []
    current_start_time = 0
    for row in csvReader:
        row = [x.strip(' ') for x in row]
        if row[0] == '0' and row[1] == '0' and row[2] == 'Header':
            trackNumber = int(row[4])
            ppqn = int(row[5])
            string_to_write = str(row[0]) + ', ' + str(row[1]) + ', ' + str(row[2]) + ', ' + str(row[3]) + ', ' + str(
                trackNumber + 1) + ', ' + str(row[5])
            outputFile.write(string_to_write + '\n')
        elif row[0] == '1' and row[1] == '0' and row[2] == 'Tempo':
            tempo = int(row[3])
            string_to_write = str(row[0]) + ', ' + str(row[1]) + ', ' + str(row[2]) + ', ' + str(row[3])
            outputFile.write(string_to_write + '\n')
            for i in range(len(correct_romanNumerals)):
                bpm = int(60000000. / tempo)
                start_time_in_ticks = int(start_times[i] / ((1./float(ppqn)) * (1./bpm) * (1000*60)))
                start_times_in_ticks.append(start_time_in_ticks)
            # print len(start_times_in_ticks)
            # print len(correct_romanNumerals)
        elif row[0] == str(trackNumber):
            while current_start_time < len(start_times_in_ticks) and \
                            start_times_in_ticks[current_start_time] < int(row[1]):
                string_to_write = ""
                if current_start_time == 0:
                    string_to_write = str(row[0]) + ', ' + str(
                        start_times_in_ticks[current_start_time]) + ', Text_t, \"' + correct_key + ': ' + str(
                        correct_romanNumerals[current_start_time]) + '\"'
                else:
                    string_to_write = str(row[0]) + ', ' + str(
                        start_times_in_ticks[current_start_time]) + ', Text_t, \"' + str(
                        correct_romanNumerals[current_start_time]) + '\"'
                outputFile.write(string_to_write + '\n')
                current_start_time += 1
            string_to_write = ""
            for i in range(len(row)-1):
                string_to_write += row[i] + ', '
            string_to_write += row[len(row)-1]
            outputFile.write(string_to_write + '\n')
        else:
            endTime = int(row[1])
            string_to_write = ""
            for i in range(len(row)-1):
                string_to_write += row[i] + ', '
            string_to_write += row[len(row)-1]
            outputFile.write(string_to_write + '\n')
    outputFile.close()

# print midifile
new_file_name = midifile.strip('melisma2003/midifiles/kp/')
# print new_file_name
os.system('midicsv-1.1/csvmidi labeled_output.csv > ' + str(new_file_name) + 'mid')

print 'This excerpt is in the key of: ' + correct_key
print correct_romanNumerals
