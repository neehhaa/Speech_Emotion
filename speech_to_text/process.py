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


upload_endpoint = "https://api.assemblyai.com/v2/upload"
transcript_endpoint = "https://api.assemblyai.com/v2/transcript"

headers = {'authorization':API_KEY_ASSEMBLYAI}

#filename = "/audio_process/output.wav"     # From Directory
filename = sys.argv[1]                      # From Terminal


# I. UPLOAD

def upload(filename):
    def read_file(filename, chunk_size=5242880):
        with open(filename,'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

    upload_response = requests.post(upload_endpoint,
                            headers=headers,
                            data=read_file(filename))

    audio_url = upload_response.json()['upload_url']
    return audio_url

# II. TRANSCRIBE

def transcribe(audio_url):
    transcript_request = {"audio_url":audio_url}
    transcript_response = requests.post(
        transcript_endpoint,json = transcript_request,
        headers=headers
    )
    job_id = transcript_response.json()['id']
    return job_id

audio_url = upload(filename)
transcript_id = transcribe(audio_url)
print(job_id)
