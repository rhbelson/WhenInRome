# Inputs:
# <int> chroma


# Output:
# <str> note
def ctn(chroma):
    if chroma == 0:
        return "C"
    if chroma == 1:
        return "C#/Db"
    if chroma == 2:
        return "D"
    if chroma == 3:
        return "D#/Eb"
    if chroma == 4:
        return "E"
    if chroma == 5:
        return "F"
    if chroma == 6:
        return "F#/Gb"
    if chroma == 7:
        return "G"
    if chroma == 8:
        return "G#/Ab"
    if chroma == 9:
        return "A"
    if chroma == 10:
        return "A#/Bb"
    if chroma == 11:
        return "B"
