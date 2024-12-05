import serial
import time
import tkinter as tk

# Set up the serial connection (adjust port if needed)
arduino = serial.Serial('/dev/cu.usbserial-2110', 9600)
time.sleep(2)  # Allow time for the connection to establish

def set_servo_angle(angle, servo_num):
    if 0 <= angle <= 180:
        command = f"{angle} {servo_num}\n"
        arduino.write(command.encode())
        time.sleep(0.05)  # Small delay to ensure the command is processed

# Function to be called when a slider is moved
# def update_servo_0(angle): # Always wants to return back to 0 degrees
#     set_servo_angle(int(angle), servo_num=0)

def update_servo_1(angle):
    set_servo_angle(int(angle), servo_num=1)

def update_servo_2(angle):
    set_servo_angle(int(angle), servo_num=2)

def update_servo_3(angle):
    set_servo_angle(int(angle), servo_num=3)

# Set up the main window
root = tk.Tk()
root.title("Servo Motor Controller")

# Create sliders for each servo
servo_1_slider = tk.Scale(root, from_=0, to=180, orient=tk.HORIZONTAL, label="Servo 1", command=update_servo_1)
servo_1_slider.set(90)  # Set initial position to 90°
servo_1_slider.pack()

servo_2_slider = tk.Scale(root, from_=0, to=180, orient=tk.HORIZONTAL, label="Servo 2", command=update_servo_2)
servo_2_slider.set(90)  # Set initial position to 90°
servo_2_slider.pack()

servo_3_slider = tk.Scale(root, from_=0, to=180, orient=tk.HORIZONTAL, label="Servo 3", command=update_servo_3)
servo_3_slider.set(90)  # Set initial position to 90°
servo_3_slider.pack()

# Run the GUI main loop
try:
    root.mainloop()
except KeyboardInterrupt:
    print("Interrupted by user")
finally:
    arduino.close()
