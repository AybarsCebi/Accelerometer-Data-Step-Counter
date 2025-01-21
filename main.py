import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_path = input("CSV Dosyasını giriniz: ")
data = pd.read_csv(file_path, sep='[;,]', engine='python')

time = data['Timestamp'] - data['Timestamp'].min()


def find_step(acceleration_data, window_size, threshold_factor):
    peaks = []
    half_window = window_size // 2
    

    for i in range(len(acceleration_data)):
        
        if i < half_window:
            window = acceleration_data[:i + half_window]
        elif i > len(acceleration_data) - half_window:
            window = acceleration_data[i - half_window:]
        else:
            window = acceleration_data[i - half_window:i + half_window]
        
        midpoint = acceleration_data[i]
        
        if midpoint == max(window) and midpoint - (sum(window)/len(window))>0.1: #stabilite durumunda adım saymasını engellemek için 
         
            print(midpoint-(sum(window)/len(window)))
            print(sum(window)/len(window))
            print("***********************************")
            peaks.append(i)
        
    return peaks

acceleration = np.sqrt(data['AccelerationZ'].values**2+data['AccelerationX'].values**2+data['AccelerationY'].values**2)
peaks = find_step(acceleration, window_size=18, threshold_factor=0.6)

print(f"Estimated step count: {len(peaks)}")

plt.figure(figsize=(12, 6))
plt.plot(time, acceleration, label='Acceleration', color='b')
plt.scatter(time[peaks], acceleration[peaks], color='r', label='Peaks (Steps)')
plt.text(0.01,0.96, f'Estimated step count: {len(peaks)}', fontsize=14, ha='left', va='top', transform=plt.gca().transAxes)
plt.title('Step Detection from Acceleration Data')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s²)')

plt.legend()
plt.grid(True)
plt.show()