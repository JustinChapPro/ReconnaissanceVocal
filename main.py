import re
import pyaudio
import queue
from google.cloud import speech
from google.oauth2 import service_account
import os

# Audio recording parameters
RATE = 32000
CHUNK = int(RATE / 10)  # 100ms

class MicrophoneStream(object):
    def __init__(self, rate, chunk):
        self._rate = rate
        self._chunk = chunk
        self.closed = True
        self._buff = queue.Queue()  


    def __enter__(self):
        self._audio_interface = pyaudio.PyAudio()
        self._audio_stream = self._audio_interface.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=self._rate,
            input=True,
            frames_per_buffer=self._chunk,
            stream_callback=self._fill_buffer,
            input_device_index=2,  
        )
        self.closed = False
        return self

    def __exit__(self, type, value, traceback):
        self._audio_stream.stop_stream()
        self._audio_stream.close()
        self.closed = True
        self._audio_interface.terminate()

    def _fill_buffer(self, in_data, frame_count, time_info, status_flags):
        """Continuously collect data from the audio stream, into the buffer."""
        self._buff.put(in_data)
        return None, pyaudio.paContinue

    def generator(self):
        while not self.closed:
            chunk = self._buff.get()
            if chunk is None:
                return
            data = [chunk]

            while True:
                try:  
                    chunk = self._buff.get(block=False)
                    if chunk is None:
                        return
                    data.append(chunk)
                except queue.Empty:
                    break

            yield b''.join(data)

def listen_print_loop(responses, keyword):
    compteur = 0  
    for response in responses:
        if not response.results:
            continue

        result = response.results[0]
        if not result.alternatives or not result.is_final:
            continue

        transcript = result.alternatives[0].transcript
        if re.search(r'\b{}\b'.format(keyword), transcript, re.I):
            compteur += 1
            print(f"Detected keyword '{keyword}': {compteur}")
    print(f"Keyword '{keyword}' detected {compteur} times.") 

def main():
    # !!! IMPORTANT Veuillez mettre votre .json pour utilliser Google api SpeechRecognition sinon cela ne marchera pas !!!
    credentials = service_account.Credentials.from_service_account_file("Mettre fichier .json ici!")
    client = speech.SpeechClient(credentials=credentials)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=RATE,
        language_code='en-US',
        max_alternatives=1,
    )

    streaming_config = speech.StreamingRecognitionConfig(
        config=config,
        interim_results=True,
    )

    with MicrophoneStream(RATE, CHUNK) as stream:
        compteur = 0
        audio_generator = stream.generator()
        requests = (speech.StreamingRecognizeRequest(audio_content=content)
                    for content in audio_generator)

        responses = client.streaming_recognize(streaming_config, requests)

        listen_print_loop(responses, "Hello")  # Specify the keyword to detect
        

if __name__ == '__main__':
    main()
