# GyroScope_UDP_Socket Project Overview

The GyroScope_UDP_Socket project facilitates real-time data acquisition from the MPU6050 sensor through the I2C interface, visualizes the data through a 3D cube simulation in Pygame, and communicates the data over UDP sockets. This project is designed to demonstrate the integration of hardware sensor data with software visualization and networking.

## Features

- **Real-time MPU6050 Sensor Data Acquisition:** Utilizes PyFTDI for I2C communication to read gyroscope and accelerometer data.
- **3D Cube Simulation:** A Pygame window displays a 3D cube that responds to the motion data from the MPU6050 sensor, providing a visual representation of the sensor's orientation.
- **UDP Socket Communication:** Sends and receives sensor data over the network using UDP sockets, allowing for real-time data streaming.
- **Dynamic Background Color Changes:** The background color of the Pygame window changes dynamically, enhancing the visual experience.

## Prerequisites

To run this project, you'll need:

- **Python 3.x:** Ensure you have Python 3 installed on your system.
- **Pygame:** A Python library for writing video games, used for visualizing the sensor data.
- **PyFTDI:** A Python library to communicate with FTDI devices via the USB interface, used for I2C communication with the MPU6050 sensor.
- **Numpy:** A fundamental package for scientific computing with Python, used for data manipulation.

## Configuration

Before running the project, make sure to configure the following:

### FTDI Configuration

- Modify the I2C configuration line to match your FTDI device's URL.
    ```python
    i2c.configure('ftdi://ftdi:232h:1:5/1')
    ```

### UDP Socket Configuration

- Adjust the server address and port to match your UDP server's settings. This is where the sensor data will be sent.
    ```python
    server_address = ('23.235.207.63', 9993)
    ```

## MPU6050 Registers

The project utilizes the following MPU6050 registers:

```python
PWR_MGMT_1 = 0x6B  # Power management
SMPLRT_DIV = 0x19  # Sample Rate Divider
CONFIG = 0x1A      # Configuration
GYRO_CONFIG = 0x1B # Gyroscope Configuration
INT_ENABLE = 0x38  # Interrupt Enable
ACCEL_XOUT_H = 0x3B # Accelerometer X-axis high byte
ACCEL_YOUT_H = 0x3D # Accelerometer Y-axis high byte
ACCEL_ZOUT_H = 0x3F # Accelerometer Z-axis high byte
GYRO_XOUT_H = 0x43  # Gyroscope X-axis high byte
GYRO_YOUT_H = 0x45  # Gyroscope Y-axis high byte
GYRO_ZOUT_H = 0x47  # Gyroscope Z-axis high byte
