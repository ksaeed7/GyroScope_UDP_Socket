import socket
from pyftdi.i2c import I2cController

class Gyroscope:
    def __init__(self):
        # MPU6050 I2C address
        self._devAddr = 0x68
        self._i2c = I2cController()
        self._i2c.configure('ftdi://ftdi:232h:1:5/1')
        self._slave = self.i2c.get_port(self._devAddr)
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._server_address = ('23.235.207.63', 9993) #University remote address
        self._init_sensor()
        self._data = {"xG": 0, "yG": 0, "zG": 0, "xA": 0, "yA": 0, "zA": 0}

    def _init_sensor(self):
        # MPU6050 Registers
        PWR_MGMT_1 = 0x6B
        SMPLRT_DIV = 0x19
        CONFIG = 0x1A
        GYRO_CONFIG = 0x1B
        INT_ENABLE = 0x38
        self._ACCEL_XOUT_H = 0x3B
        self._ACCEL_YOUT_H = 0x3D
        self._ACCEL_ZOUT_H = 0x3F
        self._GYRO_XOUT_H = 0x43
        self._GYRO_YOUT_H = 0x45
        self._GYRO_ZOUT_H = 0x47
        # Initialize MPU6050
        # Write to sample rate register
        self._slave.write_to(SMPLRT_DIV, b'\x07')
        # Write to power management register
        self._slave.write_to(PWR_MGMT_1, b'\x01')
        # Write to Configuration register
        self._slave.write_to(CONFIG, b'\x00')
        # Write to Gyro configuration register
        self._slave.write_to(GYRO_CONFIG, b'\x18')
        # Write to interrupt enable register
        self._slave.write_to(INT_ENABLE, b'\x01')

    def _read_data(self, addr):
        hi = self._slave.read_from(addr, 1).hex()
        lo = self._slave.read_from(addr + 1, 1).hex()
        value = int(hi + lo, 16)
        if value > 32768:
            value = value - 65536
        return value
    
        # while True:
        #for i in range(30):
        #Read Accelerometer raw value
        #  xAcc = getData(ACCEL_XOUT_H)
        # yAcc = getData(ACCEL_YOUT_H)
        # zAcc = getData(ACCEL_ZOUT_H)
        # print(xAcc, yAcc, zAcc)
        #Read Gyroscope raw value
        # xGyro = getData(GYRO_XOUT_H)
        #  yGyro = getData(GYRO_YOUT_H)
        # zGyro = getData(GYRO_ZOUT_H)
        # print(xGyro, yGyro, zGyro)
        #Full scale range +/- 250 degree/C as per sensitivity scale factor
        # xA = xAcc/16384.0
        # yA = yAcc/16384.0
        # zA = zAcc/16384.0
        # xG = xGyro/131.0
        # yG = yGyro/131.0
        # zG = zGyro/131.0
        # print("--------")
        # print("xG, yG, zG = %.2f, %.2f, %.2f \u00b0/s" %(xG, yG, zG))
        # print("xA, yA, zA = %.2f, %.2f, %.2f g" %(xA, yA, zA))
        # sleep(0.1)

    def get_sensor_data(self):
        # Addresses for accelerometer and gyroscope data
        
        # Read data
        xAcc = self._read_data(self._ACCEL_XOUT_H)
        yAcc = self._read_data(self._ACCEL_YOUT_H)
        zAcc = self._read_data(self._ACCEL_ZOUT_H)
        xGyro = self._read_data(self._GYRO_XOUT_H)
        yGyro = self._read_data(self._GYRO_YOUT_H)
        zGyro = self._read_data(self._GYRO_ZOUT_H)
        # Convert to g and degrees/sec
        xA = xAcc / 16384.0
        yA = yAcc / 16384.0
        zA = zAcc / 16384.0
        xG = xGyro / 131.0
        yG = yGyro / 131.0
        zG = zGyro / 131.0
        #self.data = {"xG": xG, "yG": yG, "zG": zG, "xA": xA, "yA": yA, "zA": zA}
        self._data["xG"] = str(xG)
        self._data["yG"] = str(yG)   
        self._data["zG"] = str(zG)  
        self._data["xA"] = str(xA)
        self._data["yA"] = str(yA)  
        self._data["zA"] = str(zA)  
        return self._data

    def send_data(self, data):
        self.get_sensor_data()
        allGData = "G".join([(self._data["xG"]), (self._data["yG"]), (self._data["zG"])])
        allAData = "A".join([(self._data["xA"]), (self._data["yA"]), (self._data["zA"])])
        encodedData = str.encode("\n".join([allGData, allAData]))
        self._sock.sendto(encodedData, self._server_address)
