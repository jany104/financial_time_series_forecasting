from data_fetch import fetch_data
from stft_spectrogram import generate_spectrogram
from cnn_model import train_cnn

# Step 1: Fetch Data
fetch_data()

# Step 2: Generate Spectrogram
spectrogram = generate_spectrogram()

# Step 3: Train CNN
model = train_cnn(spectrogram)

print("Pipeline Completed Successfully!")