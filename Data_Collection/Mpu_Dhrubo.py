//THONNY
from machine import Pin, I2C
import time
import math
import uos

MPU6050_ADDR = 0x68
ACCEL_XOUT_H = 0x3B
GYRO_XOUT_H = 0x43
PWR_MGMT_1 = 0x6B

i2c = I2C(scl=Pin(5), sda=Pin(4))  # D1 -> SCL, D2 -> SDA
i2c.writeto_mem(MPU6050_ADDR, PWR_MGMT_1, b'\x00')  # Wake up MPU6050

filename = "motion_dataset.csv"

def create_csv():
    try:
        with open(filename, "w") as file:
            file.write("AccY,AccZ,GyroX,GyroY,GyroZ,Label\n")
    except OSError:
        print("Error creating file.")

create_csv()  # Create CSV file initially

def read_raw_data(addr):
    data = i2c.readfrom_mem(MPU6050_ADDR, addr, 2)
    value = (data[0] << 8) | data[1]  # Combine high and low byte
    if value > 32768:
        value -= 65536  # Convert to signed 16-bit
    return value

def get_sensor_data():
    ay = read_raw_data(ACCEL_XOUT_H + 2) / 16384.0  # AccY
    az = read_raw_data(ACCEL_XOUT_H + 4) / 16384.0  # AccZ
    gx = read_raw_data(GYRO_XOUT_H) / 131.0  # GyroX
    gy = read_raw_data(GYRO_XOUT_H + 2) / 131.0  # GyroY
    gz = read_raw_data(GYRO_XOUT_H + 4) / 131.0  # GyroZ
    return ay, az, gx, gy, gz

# Data Collection with Movement Detection
count = 0
previous_accel = math.sqrt(get_sensor_data()[0]**2 + get_sensor_data()[1]**2)  # Initial magnitude
movement_threshold = 0.1  # Threshold for detecting movement

while count < 150:  # Collect 150 samples
    ay, az, gx, gy, gz = get_sensor_data()
    accel_magnitude = math.sqrt(ay**2 + az**2)  # Ignore X-axis
    movement_change = abs(accel_magnitude - previous_accel)
   
    # Determine if standing or moving
    label = "MOVING" if movement_change > movement_threshold else "STANDING"
    
    previous_accel = accel_magnitude
  
    data_entry = f"{ay:.3f},{az:.3f},{gx:.3f},{gy:.3f},{gz:.3f},{label}\n"
    with open(filename, "a") as file:
        file.write(data_entry)
    
    print(f"Saved: {data_entry.strip()}")
    count += 1
    time.sleep(0.5)  # Delay for better sampling

print("CSV file saved.")
