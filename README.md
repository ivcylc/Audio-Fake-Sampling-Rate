# Audio-Fake-Sampling-Rate

A Python script to estimate the **real sampling rate** of an audio file based on the **Roll-off frequency** and visualize its frequency spectrum. This tool is particularly useful for detecting fake or upsampled audio files.

## Features
- Estimates the real sampling rate of audio files using the 0.99 Roll-off frequency.
- Visualizes the audio's frequency spectrum and highlights the roll-off frequency.
- Handles long audio files by randomly sampling 10 short segments for analysis.
- Multi-threaded support for batch processing (future enhancement).

## Usage

### Prerequisites
Ensure you have Python 3.7 or above installed and the following dependencies:
```bash
pip install librosa numpy matplotlib

Usage:

python tmp.py

Input the waveform path

![image](https://github.com/user-attachments/assets/2cee9e05-0a30-412d-8687-0cb6ca9efe0f)
