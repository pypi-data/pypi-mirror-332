# setup.py
from setuptools import setup, find_packages

setup(
    name="music-uri-alarm-clock",
    version="0.1.2",
    author="Md. Arman Hossain",
    author_email="armanhossain.tech@gmail.com",
    description="A beautiful Spotify alarm clock for macOS",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Md-Arman-Hossain-007/music-alarm-clock.git",  # Update with your repo
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "spotify-alarm = spotify_alarm.alarm_clock:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
    ],
    python_requires=">=3.6",
)