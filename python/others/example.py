from music21 import note,stream
s = stream.Stream()  # sorry, your instinct to use a stream was probably good

n = note.Note('C5',quarterLength = 0.5)
s.append(n)
n = note.Note('A4',quarterLength = 0.5)
s.append(n)
n = note.Note('C5',quarterLength = 0.5)
s.append(n)
n = note.Note('A4',quarterLength = 0.5)
s.append(n)
n = note.Note('C5',quarterLength = 0.5)
s.append(n)
n = note.Note('A4',quarterLength = 0.5)
s.append(n)
n = note.Note('C5',quarterLength = 0.5)
s.append(n)
n = note.Note('A4',quarterLength = 0.5)
s.append(n)
c = note.Note('E4',quarterLength = 8)
s.insert(0, c)
out1 = s.makeVoices()
out2 = out1.makeNotation()
out2.show('lily.pdf')