from machine import Pin, I2C
import utime

# MPU6050 I2C Address
MPU6050_ADDR = 0x68  

# Initialize I2C (SDA=GPIO4, SCL=GPIO5)
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)

# Function to Initialize MPU6050
def mpu6050_init():
    i2c.writeto_mem(MPU6050_ADDR, 0x6B, b'\x00')  # Wake up MPU6050

# Function to Read Accelerometer and Gyroscope Data
def read_mpu6050():
    data = i2c.readfrom_mem(MPU6050_ADDR, 0x3B, 14)
    
    AcX = (data[0] << 8 | data[1])
    AcY = (data[2] << 8 | data[3])
    AcZ = (data[4] << 8 | data[5])
    GyX = (data[8] << 8 | data[9])
    GyY = (data[10] << 8 | data[11])
    GyZ = (data[12] << 8 | data[13])
    
    AcX = AcX - 65536 if AcX > 32767 else AcX
    AcY = AcY - 65536 if AcY > 32767 else AcY
    AcZ = AcZ - 65536 if AcZ > 32767 else AcZ
    GyX = GyX - 65536 if GyX > 32767 else GyX
    GyY = GyY - 65536 if GyY > 32767 else GyY
    GyZ = GyZ - 65536 if GyZ > 32767 else GyZ
    
    return AcX, AcY, AcZ, GyX, GyY, GyZ

# Initialize MPU6050
mpu6050_init()

# Get user input for activity type
activity = input("Enter activity (standing/moving): ").strip().lower()

# Open CSV file to store data
filename = "MPU6050_data10.csv"
with open(filename, "w") as f:
    f.write("AcX,AcY,AcZ,GyX,GyY,GyZ,Activity\n")

# Collect 1000 samples
for i in range(1000):
    AcX, AcY, AcZ, GyX, GyY, GyZ = read_mpu6050()
    print(f"Sample {i+1}: {AcX}, {AcY}, {AcZ}, {GyX}, {GyY}, {GyZ}, {activity}")

    with open(filename, "a") as f:
        f.write(f"{AcX},{AcY},{AcZ},{GyX},{GyY},{GyZ},{activity}\n")
    
    utime.sleep(0.2)

print("✅ Data collection completed.")
