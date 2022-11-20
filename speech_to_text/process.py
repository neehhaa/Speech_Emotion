"""

STEPS :
I. UPLOAD
II. TRANSCRIBE
III. POLLING
IV. SAVE TRANSCRIPT

"""

import requests
from api_config import API_KEY_ASSEMBLYAI
import time
import json

upload_endpoint = "https://api.assemblyai.com/v2/upload"
transcript_endpoint = "https://api.assemblyai.com/v2/transcript"

headers = {'authorization':API_KEY_ASSEMBLYAI}

# I. UPLOAD

def upload(filename):
    def read_file(filename, chunk_size=5242880):
        with open(filename,'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

    upload_response = requests.post(upload_endpoint, headers=headers, data=read_file(filename))

    audio_url = upload_response.json()['upload_url']
    return audio_url


# II. TRANSCRIBE

def transcribe(audio_url,sentiment_analysis):
    transcript_request = {"audio_url":audio_url,'sentiment_analysis':sentiment_analysis}
    transcript_response = requests.post(transcript_endpoint, json = transcript_request, headers=headers)
    job_id = transcript_response.json()['id']
    return job_id


# III. POLLING

def poll(transcript_id):
    polling_endpoint = transcript_endpoint + '/' + transcript_id
    polling_response = requests.get(polling_endpoint, headers=headers)
    return polling_response.json()

def get_transcription_result_url(audio_url,sentiment_analysis):
    transcribe_id = transcribe(audio_url,sentiment_analysis)
    while True:
        data = poll(transcribe_id)
        if data['status'] == 'completed':
            return data, None
        elif data['status'] == 'error':
            return data, data['error']
                                   
        print("waiting for 30 seconds")
        time.sleep(30)


# IV. SAVE TRANSCRIPT

def save_transcript(audio_url, filename,sentiment_analysis=False):
    data,error = get_transcription_result_url(audio_url)

    if data:
        text_filename = filename + ".txt"
        with open(text_filename,"w") as f:
            f.write(data['text'])
        if sentiment_analysis:
            sen_filename = filename + "_sentiment.json"
            with open(sen_filename,"w") as f:
                sentiment = data["sentiment_analysis_results"]
                json.dump(sentiment,f,indent=4)

        print('saved')
    elif error:
        print("Error",error)

