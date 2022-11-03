import wave

obj = wave.open("preamble.wav","rb")

#getting data
print("channels",obj.getnchannels())
print("sample width",obj.getsampwidth())
print("frame rate",obj.getframerate())
print("Number of frames",obj.getnframes())
print("parameters",obj.getparams())

#time
time_audio = obj.getnframes()/obj.getframerate()
print(time_audio)

#frames
frames = obj.readframes(-1)
print(type(frames),type(frames[0]))
print(len(frames))
print(len(frames)/2)
obj.close()

#setting data

obj_new = wave.open("preamble_new1812.wav","wb")
obj_new.setnchannels(2)
obj_new.setsampwidth(2)
obj_new.setframerate(22050)
obj_new.writeframes(frames)
obj_new.close()



