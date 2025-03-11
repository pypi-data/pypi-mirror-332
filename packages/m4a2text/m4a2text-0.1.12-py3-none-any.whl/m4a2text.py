import ffmpeg
import threading
import azure.cognitiveservices.speech as speechsdk


class M4A2Text:
    def __init__(self, subscription_key, region="eastus"):
        """Azure Speech Sevice Initializer"""
        self.speech_config = speechsdk.SpeechConfig(
            subscription=subscription_key,
            region=region)

    def convert_m4a_to_wav(self, m4a_file, wav_file):
        """M4A to WAV Transformation"""
        try:
            (
                ffmpeg
                .input(m4a_file)
                .output(wav_file, format="wav", acodec="pcm_s16le", ar="16000")
                .run(overwrite_output=True)
            )
            print(f"{m4a_file} → {wav_file} Transformation Success!")
            return wav_file
        except Exception as e:
            print(f"Error: {e}")
            return None

    def transcribe_audio(self, audio_file):
        """WAV to Text Transcription"""
        audio_config = speechsdk.audio.AudioConfig(filename=audio_file)
        recognizer = speechsdk.SpeechRecognizer(
            speech_config=self.speech_config,
            audio_config=audio_config)

        results = []
        done = threading.Event()

        def handle_final_result(evt):
            print(f"Text: {evt.result.text}")
            results.append(evt.result.text)

        def stop_recognition(evt):
            print("Completed: {}".format(evt))
            done.set()

        recognizer.recognized.connect(handle_final_result)
        recognizer.session_stopped.connect(stop_recognition)
        recognizer.canceled.connect(stop_recognition)

        print(f"Transcribing {audio_file}...")
        recognizer.start_continuous_recognition()
        done.wait()
        recognizer.stop_continuous_recognition()

        return " ".join(results)

    def convert_and_transcribe(self, m4a_file, make_output_file=True):
        """M4A to WAV and WAV to Text Transcription"""
        wav_file = m4a_file.replace(".m4a", ".wav")
        converted_file = self.convert_m4a_to_wav(m4a_file, wav_file)

        if converted_file:
            text = self.transcribe_audio(converted_file)
            if make_output_file:
                with open(f"{m4a_file.replace('.m4a', '.txt')}", "w") as f:
                    f.write(text)
            return text
        return None
