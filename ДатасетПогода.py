import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

file_path = "/home/linux/Завантаження/temperature_data.csv"  # заміни на актуальний шлях

# Завантаження даних
df = pd.read_csv(file_path)

# Переведення стовпця 'Date' у datetime формат
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Візуалізація даних
plt.plot(df['Temperature'])
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.title('Temperature over time')
plt.show()

# Нормалізація температури
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(df['Temperature'].values.reshape(-1, 1))

# Створення датасету для LSTM
def create_dataset(data, time_step=60):
    X, y = [], []
    for i in range(len(data) - time_step - 1):
        X.append(data[i:(i + time_step), 0])
        y.append(data[i + time_step, 0])
    return np.array(X), np.array(y)

# Створення датасету
X, y = create_dataset(scaled_data)

# Розподіл на тренувальний та тестовий набори
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# Перетворення у 3D масив для LSTM (samples, time_steps, features)
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

# Створення моделі LSTM
model = Sequential()

# Перший LSTM шар
model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))

# Другий LSTM шар
model.add(LSTM(units=50, return_sequences=False))

# Dropout для уникнення перенавчання
model.add(Dropout(0.2))

# Вихідний шар
model.add(Dense(units=1))

# Компіляція моделі
model.compile(optimizer='adam', loss='mean_squared_error')

# Тренування моделі
model.fit(X_train, y_train, epochs=150, batch_size=32)

# Прогнозування на тестових даних
predictions = model.predict(X_test)

# Зворотне масштабування для отримання результату в оригінальних одиницях
predictions = scaler.inverse_transform(predictions)
y_test_rescaled = scaler.inverse_transform(y_test.reshape(-1, 1))

# Візуалізація прогнозів
plt.plot(y_test_rescaled, color='blue', label='Real Temperature')
plt.plot(predictions, color='red', label='Predicted Temperature')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.title('Real vs Predicted Temperature')
plt.legend()
plt.show()

# Прогнозування на 100 днів
input_data = scaled_data[-60:]  # Останні 60 днів
input_data = input_data.reshape(1, 60, 1)

predicted_temp = []
for i in range(100):  # Прогнозуємо 100 днів вперед
    temp = model.predict(input_data)
    predicted_temp.append(temp[0, 0])
    
    # Оновлюємо вход для наступного дня
    input_data = np.append(input_data[:, 1:, :], temp.reshape(1, 1, 1), axis=1)

# Зворотне масштабування прогнозу
predicted_temp = scaler.inverse_transform(np.array(predicted_temp).reshape(-1, 1))

# Візуалізація прогнозу на 100 днів
plt.plot(predicted_temp, color='red', label='Predicted Temperature for 100 days')
plt.xlabel('Days')
plt.ylabel('Temperature')
plt.title('Predicted Temperature for the next 100 days')
plt.legend()
plt.show()
