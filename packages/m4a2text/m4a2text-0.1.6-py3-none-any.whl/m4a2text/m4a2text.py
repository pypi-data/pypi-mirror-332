import ffmpeg
import threading
import azure.cognitiveservices.speech as speechsdk

class M4A2Text:
    def __init__(self, subscription_key, region="eastus"):
        """Azure Speech 서비스 설정"""
        self.speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)

    def convert_m4a_to_wav(self, m4a_file, wav_file):
        """M4A 파일을 WAV 파일로 변환"""
        try:
            (
                ffmpeg
                .input(m4a_file)
                .output(wav_file, format="wav", acodec="pcm_s16le", ar="16000")
                .run(overwrite_output=True)
            )
            print(f"{m4a_file} → {wav_file} 변환 완료")
            return wav_file
        except Exception as e:
            print(f"오디오 변환 실패: {e}")
            return None

    def transcribe_audio(self, audio_file):
        """WAV 파일을 텍스트로 변환"""
        audio_config = speechsdk.audio.AudioConfig(filename=audio_file)
        recognizer = speechsdk.SpeechRecognizer(speech_config=self.speech_config, audio_config=audio_config)

        results = []
        done = threading.Event()

        def handle_final_result(evt):
            print(f"인식된 텍스트: {evt.result.text}")
            results.append(evt.result.text)

        def stop_recognition(evt):
            print("음성 인식 완료.")
            done.set()

        recognizer.recognized.connect(handle_final_result)
        recognizer.session_stopped.connect(stop_recognition)
        recognizer.canceled.connect(stop_recognition)

        print("음성 인식 시작...")
        recognizer.start_continuous_recognition()
        done.wait()
        recognizer.stop_continuous_recognition()

        return " ".join(results)

    def convert_and_transcribe(self, m4a_file):
        """M4A를 WAV로 변환 후 음성 인식 수행"""
        wav_file = m4a_file.replace(".m4a", ".wav")
        converted_file = self.convert_m4a_to_wav(m4a_file, wav_file)

        if converted_file:
            text = self.transcribe_audio(converted_file)
            return text
        return None
