"""

STEPS :
I. UPLOAD
II. TRANSCRIBE
III. POLLING
IV. SAVE TRANSCRIPT

"""

import requests
from api_config import API_KEY_ASSEMBLYAI
import sys

# I. UPLOAD

upload_endpoint = "https://api.assemblyai.com/v2/upload"

#filename = "/audio_process/output.wav"      # From Directory
filename = sys.argv[1]      # From Terminal

def read_file(filename, chunk_size=5242880):
    with open(filename,'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data

headers = {'authorization':API_KEY_ASSEMBLYAI}
response = requests.post(upload_endpoint,
                        headers=headers,
                        data=read_file(filename))

print(response.json())