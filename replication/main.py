import scipy
import numpy as np
import matplotlib.pyplot as plt

def load_sensor_data(filename):
    data = scipy.io.loadmat(filename)
    sensor_data = data['sensor_data_noisy']
    p_recorded = data['p_recorded']
    medium = data['medium']
    sensor = data['sensor']
    return data, sensor_data, p_recorded, medium, sensor


# pressure data variable is call p_recorded short for "pressure recorded"
data, sensor_data, p_recorded, medium, sensor = load_sensor_data('sensor_data_noisy')
plt.plot(p_recorded)

plt.show()

