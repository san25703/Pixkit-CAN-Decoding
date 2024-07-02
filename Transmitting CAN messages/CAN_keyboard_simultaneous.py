import time
import can
import keyboard

# Function to send CAN message using python-can
def send_can_message(bus, arbitration_id, data):
    message = can.Message(arbitration_id=arbitration_id, data=data, is_extended_id=False)
    try:
        bus.send(message)
        print(f"Message sent: ID=0x{arbitration_id:X}, Data: {' '.join(f'{byte:02X}' for byte in data)}")
    except can.CanError as e:
        print(f"Message not sent: {e}")

# Function to handle key press events
def handle_key_press(bus):
    seventh_byte = 0x00  # Initialize 7th byte

    while True:
        if keyboard.is_pressed('w'):
            # Forward (Velocity Message)
            data_velocity = [0x11, 0x64, 0x00, 0x00, 0x00, 0x00, seventh_byte, 0x00]
            data_velocity[7] = data_velocity[0] ^ data_velocity[1] ^ data_velocity[2] ^ data_velocity[3] ^ data_velocity[4] ^ data_velocity[5] ^ data_velocity[6]
            send_can_message(bus, 0x130, data_velocity)
            print("Forward")

        if keyboard.is_pressed('s'):
            # Backward (Velocity Message)
            data_velocity = [0x31, 0x64, 0x00, 0x00, 0x00, 0x00, seventh_byte, 0x00]
            data_velocity[7] = data_velocity[0] ^ data_velocity[1] ^ data_velocity[2] ^ data_velocity[3] ^ data_velocity[4] ^ data_velocity[5] ^ data_velocity[6]
            send_can_message(bus, 0x130, data_velocity)
            print("Reverse")

        if keyboard.is_pressed('a'):
            # Left (Steering Message)
            data_left = [0x11, 0xFF, 0x00, 0x00, 0x0A, 0x00, seventh_byte, 0x00]
            data_left[7] = data_left[0] ^ data_left[1] ^ data_left[2] ^ data_left[3] ^ data_left[4] ^ data_left[5] ^ data_left[6]
            send_can_message(bus, 0x132, data_left)
            print("Left")

        if keyboard.is_pressed('d'):
            # Right (Steering Message)
            data_right = [0x11, 0xFF, 0xFF, 0x00, 0x0A, 0x00, seventh_byte, 0x00]
            data_right[7] = data_right[0] ^ data_right[1] ^ data_right[2] ^ data_right[3] ^ data_right[4] ^ data_right[5] ^ data_right[6]
            send_can_message(bus, 0x132, data_right)
            print("Right")

        if keyboard.is_pressed('space'):
            # Brake Message for Space Bar
            data_brake_space = [0x03, 0xC8, 0x00, 0x01, 0x00, 0x00, seventh_byte, 0x00]
            data_brake_space[7] = data_brake_space[0] ^ data_brake_space[1] ^ data_brake_space[2] ^ data_brake_space[3] ^ data_brake_space[4] ^ data_brake_space[5] ^ data_brake_space[6]
            send_can_message(bus, 0x131, data_brake_space)
            print("Brake (Space Bar)")

        if keyboard.is_pressed('r'):
            # Brake Message for R
            data_brake_r = [0x03, 0xC8, 0x00, 0x02, 0x00, 0x00, seventh_byte, 0x00]
            data_brake_r[7] = data_brake_r[0] ^ data_brake_r[1] ^ data_brake_r[2] ^ data_brake_r[3] ^ data_brake_r[4] ^ data_brake_r[5] ^ data_brake_r[6]
            send_can_message(bus, 0x131, data_brake_r)
            print("Brake (R) Released")

        # Increment 7th byte and reset to 0x00 if it reaches 0x10
        seventh_byte = (seventh_byte + 1) % 0x10

        # Sleep for a short duration to prevent high CPU usage
        time.sleep(0.02)

# Main function to initialize CAN bus and handle key presses
def main():
    try:
        bus = can.interface.Bus(channel='PCAN_USBBUS2', interface='pcan', bitrate=500000)
    except can.CanError as e:
        print(f"Failed to initialize CAN bus: {e}")
        return

    try:
        handle_key_press(bus)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        bus.shutdown()

if __name__ == "__main__":
    main()
