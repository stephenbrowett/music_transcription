# split_instruments.py

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

from pydub import AudioSegment

from scipy import signal
from scipy.io import wavfile


#def convert_to_mono():

path_to_music = "C:\\Users\\User\\Music\\The Verve\\Urban Hymns\\"
song = "09 Lucky Man.wav"
mono_song = "99 mono_lucky_man.wav"

sound = AudioSegment.from_wav('{0}{1}'.format(path_to_music, song))
sound = sound.split_to_mono()
sound_left = sound[0]
sound_right = sound[1]
sound_left.export('{0}{1}'.format(path_to_music, mono_song), format="wav")

sample_rate, samples = wavfile.read('{0}{1}'.format(path_to_music, mono_song))
frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)

plt.pcolormesh(times, frequencies, spectrogram,
	norm=colors.LogNorm(vmin=spectrogram.min(), vmax=spectrogram.max())
	)
#plt.imshow(spectrogram)
#plt.yscale('log')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()
