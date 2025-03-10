import ffmpeg
import threading
import azure.cognitiveservices.speech as speechsdk


def convert_m4a_to_wav(m4a_file, wav_file):
    """M4A 파일을 WAV 파일로 변환"""
    try:
        (
            ffmpeg
            .input(m4a_file)
            .output(wav_file, format="wav", acodec="pcm_s16le", ar="16000")
            .run(overwrite_output=True)
        )
        print(f"{m4a_file} → {wav_file} 변환 완료")
    except Exception as e:
        print(f"오디오 변환 실패: {e}")


def speech_to_text_continuous(audio_file, subscription_key, region="eastus"):
    """Azure Speech Services를 이용하여 연속 음성 인식"""
    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)
    audio_config = speechsdk.audio.AudioConfig(filename=audio_file)

    recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

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
