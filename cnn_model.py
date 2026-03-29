import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense
from sklearn.model_selection import train_test_split

def train_cnn(spectrogram):
    # Reshape for CNN
    X = spectrogram.reshape(1, spectrogram.shape[0], spectrogram.shape[1], 1)

    # Dummy target (next price simulation)
    y = np.array([1.0])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = Sequential([
        Conv2D(32, (3,3), activation='relu', input_shape=(X.shape[1], X.shape[2], 1)),
        Flatten(),
        Dense(50, activation='relu'),
        Dense(1)
    ])

    model.compile(optimizer='adam', loss='mse')

    model.fit(X_train, y_train, epochs=5)

    loss = model.evaluate(X_test, y_test)
    print("Test Loss:", loss)

    return model