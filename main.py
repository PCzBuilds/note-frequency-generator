
# 🎵 Note to Frequency Converter – Now supports sharps and flats

# Step 1: Get user input
note = input("Enter a note (like A4, Bb3, D#5): ")

# Step 2: Define all notes, including enharmonic equivalents
note_names = {
    'C': 0, 'C#': 1, 'Db': 1,
    'D': 2, 'D#': 3, 'Eb': 3,
    'E': 4,
    'F': 5, 'F#': 6, 'Gb': 6,
    'G': 7, 'G#': 8, 'Ab': 8,
    'A': 9, 'A#': 10, 'Bb': 10,
    'B': 11
}

# A4 is the reference note (440 Hz)
a4_index = 9 + 12 * 4  # A = 9, octave 4

# Step 3: Extract note and octave using regex
import re
match = re.match(r'^([A-Ga-g][#b]?)(\d)$', note.strip())

if not match:
    print("❌ Invalid note format. Use A4, Bb3, D#5, etc.")
else:
    name, octave = match.groups()
    name = name.capitalize()
    octave = int(octave)

    if name not in note_names:
        print("❌ Invalid note name.")
    else:
        note_index = note_names[name] + 12 * octave
        semitone_diff = note_index - a4_index
        frequency = 440 * (2 ** (semitone_diff / 12))
        print(f"✅ The frequency of {note.upper()} is {round(frequency, 2)} Hz")
import numpy as np
from scipy.io.wavfile import write

# Generate 1 second of sound at the calculated frequency
duration = 1.0  # seconds
sample_rate = 44100  # how many samples per second
t = np.linspace(0, duration, int(sample_rate * duration), False)

# Create a sine wave (the shape of the note’s sound)
waveform = 0.5 * np.sin(2 * np.pi * frequency * t)

# Convert waveform to 16-bit audio
audio = np.int16(waveform * 32767)

# Save it as a .wav file
write("note.wav", sample_rate, audio)

print("🎧 Saved your note as note.wav – click it on the left to hear it.")
