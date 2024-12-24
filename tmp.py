import librosa
import numpy as np
import matplotlib.pyplot as plt

def calculate_rolloff_with_threshold(y, sr, roll_percent=0.99, energy_threshold=0.01):

    fft = np.fft.fft(y)
    magnitude = np.abs(fft)
    freq = np.fft.fftfreq(len(magnitude), 1 / sr)

    positive_freqs = freq[:len(freq) // 2]
    positive_magnitude = magnitude[:len(magnitude) // 2]

    total_energy = np.sum(positive_magnitude)
    cumulative_energy = np.cumsum(positive_magnitude)
    normalized_energy = cumulative_energy / total_energy

    rolloff_index = np.searchsorted(normalized_energy, roll_percent)
    rolloff_freq = positive_freqs[rolloff_index]

    return rolloff_freq


def analyze_audio(file_path, output_image_path):

    y, sr = librosa.load(file_path, sr=None)
    print(f"Loaded audio: Sample rate = {sr}, Duration = {len(y) / sr:.2f}s")

    rolloff_freq = calculate_rolloff_with_threshold(y, sr, roll_percent=0.998)
    print(f"0.99 Roll-off Frequency (with threshold): {rolloff_freq:.2f} Hz")

    S, freqs, times, _ = plt.specgram(y, NFFT=2048, Fs=sr, noverlap=1024, cmap="viridis")
    plt.axhline(y=rolloff_freq, color='r', linestyle='--', label=f"0.99 Roll-off: {rolloff_freq:.2f} Hz")
    plt.title("Spectrogram with 0.99 Roll-off (Improved)")
    plt.xlabel("Time (s)")
    plt.ylabel("Frequency (Hz)")
    plt.legend()

    plt.savefig(output_image_path)
    print(f"Spectrogram saved as {output_image_path}")
    plt.close()

    return rolloff_freq

while 1:
    file_path = input("input:") 
    output_image_path = "xtmp.png" 
    nearest_rate = analyze_audio(file_path, output_image_path)

    print(f"The closest estimated sample rate is: {nearest_rate * 2} Hz")
