import sys
from process import *

#filename = "audio_process/output.wav"     # From Directory
filename = sys.argv[1]                      # From Terminal

audio_url = upload(filename)
save_transcript(audio_url, filename)