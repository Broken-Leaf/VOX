import requests
from playsound import playsound
import os
from typing import Union
import tempfile

def generate_audio(message: str, voice: str = "Brian"):
    url: str = f"https://api.streamelements.com/kappa/v2/speech?voice={voice}&text={{{message}}}"

    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
    
    try:
        result = requests.get(url=url, headers=headers)
        result.raise_for_status()  # Raises HTTPError for bad responses
        return result.content
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def speak(message: str, voice: str = "Brian", extension: str = ".mp3") -> Union[None, str]:
    try:
        result_content = generate_audio(message, voice)
        if result_content:
            with tempfile.NamedTemporaryFile(delete=False, suffix=extension) as temp_file:
                temp_file.write(result_content)
                temp_file_path = temp_file.name

            playsound(temp_file_path)
            os.remove(temp_file_path)
        else:
            print("Failed to generate audio.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return str(e)

