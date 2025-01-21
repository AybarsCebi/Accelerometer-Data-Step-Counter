import math
import pandas as pd
import matplotlib.pyplot as plt

file_path = input("CSV Dosyasını giriniz: ")

df = pd.read_csv(file_path, sep='[;,]')

print(df.head())
timestamps=df['Timestamp']
xs=df['AccelerationX']
ys=df['AccelerationY']
zs=df['AccelerationZ']

plt.figure(figsize=(10, 6))
plt.plot(timestamps, xs, label='AccelerationX', color='r')
plt.plot(timestamps, ys, label='AccelerationY', color='g')
plt.plot(timestamps, zs, label='AccelerationZ', color='b')


plt.title('Acceleration Data Over Time')
plt.xlabel('Timestamp')
plt.ylabel('Acceleration')
plt.xticks(rotation=45)
plt.legend()


plt.tight_layout()
plt.show()


