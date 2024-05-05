from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split

labels = to_categorical(labels)
X_train, X_val, y_train, y_val = train_test_split(images, labels, test_size=0.2, random_state=42)
history = model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))
