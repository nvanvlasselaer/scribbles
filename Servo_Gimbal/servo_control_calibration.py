import serial
import time

# Set up the serial connection (adjust port if needed)
arduino = serial.Serial('/dev/cu.usbserial-140', 9600)
time.sleep(2)  # Give some time for the connection to establish


def set_servo_pulse(pulse, servo_num=0):
    # Ensure pulse is within safe range to prevent damage
    if 100 <= pulse <= 600:
        command = f"{pulse} {servo_num}\n"
        arduino.write(command.encode())
        time.sleep(0.1)  # Adjust as needed

# Testing different pulse widths
try:
    set_servo_pulse(125)  # Start with a small pulse width
    time.sleep(2)
    set_servo_pulse(600)  # Increase to a higher pulse width
except KeyboardInterrupt:
    print("Calibration interrupted by user")
finally:
    arduino.close()
