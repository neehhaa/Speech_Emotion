from pydub import AudioSegment

audio = AudioSegment.from_wav("output.wav")

audio = audio + 6 #volume

audio = audio * 2 #repeat

audio = audio.fade_in(5000)

audio.export("output.mp3",format="mp3")
audio2 = AudioSegment.from_mp3("output.mp3")
print("DONE")