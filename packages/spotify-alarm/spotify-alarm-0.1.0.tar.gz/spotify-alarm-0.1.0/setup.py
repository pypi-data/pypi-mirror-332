# setup.py
from setuptools import setup, find_packages

setup(
    name="spotify-alarm",
    version="0.1.0",
    author="Md. Arman Hossain",
    author_email="armanhossain.tech@gmail.com",
    description="A beautiful Spotify alarm clock for macOS",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/spotify-alarm",  # Update with your repo
    packages=find_packages(),
    install_requires=[
        "tkinter",  # Usually bundled with Python, but listed for clarity
    ],
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