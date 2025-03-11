from setuptools import setup

setup(
    name="m4a2text",
    version="0.1.13",
    description="Convert M4A audio files to WAV and transcribe speech to text using Azure Speech API.",
    author="Ian Park",
    author_email="ianolpx@gmail.com",
    url="https://github.com/ianolpx/m4a2text",
    # packages=find_packages(),
    py_modules=["m4a2text"], 
    install_requires=[
        "ffmpeg-python",
        "azure-cognitiveservices-speech",
    ],
    entry_points={
        "console_scripts": [
            "m4a2text=m4a2text.speech_converter:convert_m4a_to_wav",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
