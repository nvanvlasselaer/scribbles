import serial
import time
import tkinter as tk
from threading import Thread

# Set up the serial connection (adjust port if needed)
arduino = serial.Serial('/dev/cu.usbserial-140', 9600)
time.sleep(2)  # Allow time for the connection to establish

# Function to set servo angle
def set_servo_angle(angle, servo_num):
    if 0 <= angle <= 180:
        command = f"{angle} {servo_num}\n"
        arduino.write(command.encode())
        time.sleep(0.05)  # Small delay to ensure the command is processed

# Update functions for each servo
def update_servo_1(angle):
    set_servo_angle(int(angle), servo_num=1)

def update_servo_2(angle):
    set_servo_angle(int(angle), servo_num=2)

def update_servo_3(angle):
    set_servo_angle(int(angle), servo_num=3)

# Loop control function
def run_loop():
    while running:
        for servo_num in range(3):
            min_angle = int(min_angle_entries[servo_num].get())
            max_angle = int(max_angle_entries[servo_num].get())
            
            # Move from min to max angle
            for angle in range(min_angle, max_angle + 1, 1):
                set_servo_angle(angle, servo_num + 1)
                time.sleep(0.01)  # Small delay for smooth movement
            
            # Move back from max to min angle
            for angle in range(max_angle, min_angle - 1, -1):
                set_servo_angle(angle, servo_num + 1)
                time.sleep(0.01)  # Small delay for smooth movement

# Start and stop loop functions
def start_loop():
    global running
    running = True
    loop_thread = Thread(target=run_loop)
    loop_thread.start()

def stop_loop():
    global running
    running = False

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

# Create entry fields for min and max angles
min_angle_entries = []
max_angle_entries = []

for i in range(3):
    min_label = tk.Label(root, text=f"Servo {i+1} Min Angle:")
    min_label.pack()
    min_entry = tk.Entry(root)
    min_entry.insert(tk.END, "0")  # Default min angle
    min_entry.pack()
    min_angle_entries.append(min_entry)
    
    max_label = tk.Label(root, text=f"Servo {i+1} Max Angle:")
    max_label.pack()
    max_entry = tk.Entry(root)
    max_entry.insert(tk.END, "180")  # Default max angle
    max_entry.pack()
    max_angle_entries.append(max_entry)

# Start and Stop buttons for loop
start_button = tk.Button(root, text="Start Loop", command=start_loop)
start_button.pack()

stop_button = tk.Button(root, text="Stop Loop", command=stop_loop)
stop_button.pack()

# Initialize the running variable for loop control
running = False

# Run the GUI main loop
try:
    root.mainloop()
except KeyboardInterrupt:
    print("Interrupted by user")
finally:
    arduino.close()
