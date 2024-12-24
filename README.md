# Audio-Fake-Sampling-Rate

A Python script to estimate the **real sampling rate** of an audio file based on the **Roll-off frequency** and visualize its frequency spectrum. This tool is particularly useful for detecting fake or upsampled audio files.

## Features
- Estimates the real sampling rate of audio files using the Roll-off frequency.
- Visualizes the audio's frequency spectrum and highlights the roll-off frequency.

**Empirically, we found that roll-off freq works best when set to 0.998**

## Usage

### Prerequisites
Ensure you have Python 3.7 or above installed and the following dependencies:
```bash
pip install librosa numpy matplotlib
```

Usage:

```bash
python tmp.py
```

Input the waveform path


Visualization:

![image](https://github.com/user-attachments/assets/3437c02d-f259-483a-949e-3b29bbe9645b)
