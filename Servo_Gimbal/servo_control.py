import serial
import time

# Set up the serial connection (adjust port if needed)
arduino = serial.Serial('/dev/cu.usbserial-2110', 9600)
time.sleep(2)  # Allow time for the connection to establish

Pause = 3

def set_servo_angle(angle, servo_num=0):
    if 0 <= angle <= 180:
        command = f"{angle} {servo_num}\n"
        arduino.write(command.encode())
        time.sleep(0.1)  # Adjust if servo is slow to respond

try:
    # Set each servo to 0 degrees initially
    set_servo_angle(0, servo_num=1)   # Servo 1
    time.sleep(Pause)
    set_servo_angle(0, servo_num=2)   # Servo 2
    time.sleep(Pause)
    set_servo_angle(0, servo_num=3)   # Servo 3
    time.sleep(2)

    # Move each servo to 90 degrees
    set_servo_angle(20, servo_num=1)  # Servo 1
    time.sleep(Pause)
    set_servo_angle(60, servo_num=2)  # Servo 2
    time.sleep(Pause)
    set_servo_angle(40, servo_num=3)  # Servo 3
    time.sleep(2)

    # Move each servo back to 0 degrees
    set_servo_angle(90, servo_num=1)   # Servo 1
    time.sleep(0.1)
    set_servo_angle(90, servo_num=2)   # Servo 2
    time.sleep(0.1)
    set_servo_angle(90, servo_num=3)   # Servo 3

except KeyboardInterrupt:
    print("Interrupted by user")
finally:
    arduino.close()
