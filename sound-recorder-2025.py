"""
Created 2025
Followed a tutorial from https://www.geeksforgeeks.org/
Author: Piotr M
"""


import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv


def main():
    """Main function."""
    # Sampling frequency
    freq = 44100

    # Recording duration
    duration = 5

    # Start recorder with the given values 
    # of duration and sample frequency
    recording = sd.rec(int(duration * freq), 
                       samplerate=freq, channels=2)

    # Record audio for the given number of seconds
    sd.wait()

    # This will convert the NumPy array to an audio
    # file with the given sampling frequency
    write("recording0.wav", freq, recording)

    # Convert the NumPy array to audio file
    wv.write("recording1.wav", recording, freq, sampwidth=2)

if __name__ == "__main__":
    main()
    print('Finished ok.')
