import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import stft
import pandas as pd

def generate_spectrogram():
    data = pd.read_csv("stock_data.csv")

    signal = data.iloc[:, 1].values  # Use one stock

    f, t, Zxx = stft(signal, nperseg=64)

    plt.pcolormesh(t, f, np.abs(Zxx))
    plt.title("Spectrogram")
    plt.ylabel("Frequency")
    plt.xlabel("Time")
    plt.colorbar()
    plt.savefig("spectrogram.png")
    plt.show()

    return np.abs(Zxx)

if __name__ == "__main__":
    generate_spectrogram()