import wave
import matplotlib.pyplot as plt
import numpy as np

obj = wave.open("gettysburg.wav","rb")

sample_freq = obj.getframerate()
n_sample = obj.getnframes()
signal_wave = obj.readframes(-1)
obj.close()

time_audio = n_sample/sample_freq
print(time_audio)

signal_array = np.frombuffer(signal_wave,dtype=np.int16)
times = np.linspace(0,time_audio,num=n_sample)

plt.figure(figsize=(15,5))
plt.plot(times,signal_array)
plt.title("Audio Signal")
plt.ylabel("signal")
plt.xlabel("Time(s)")
plt.xlim(0,time_audio)
plt.show()
