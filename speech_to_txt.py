import sounddevice as sd
import numpy as np
import speech_recognition as sr

import speech_recognition as sr
import sounddevice as sd
import numpy as np

def speech_to_txt():
    r = sr.Recognizer()

    # Record audio using sounddevice
    print("Recording... Speak now!")
    duration = 5  # Duration of recording in seconds
    sample_rate = 16000  # Sample rate for recording

    try:
        # Capture audio
        audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
        sd.wait()  # Wait until recording is finished
        print("Recording complete. Processing...")

        # Convert audio to recognizer-compatible format
        audio = sr.AudioData(audio_data.tobytes(), sample_rate, 2)

        # Recognize speech
        voice_data = r.recognize_google(audio)
        print(voice_data)
        return voice_data
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError:
        print("RequestError: Could not request results from Google Speech Recognition service.")
    except Exception as e:
        print(f"An error occurred: {e}")

#speech_to_txt()


