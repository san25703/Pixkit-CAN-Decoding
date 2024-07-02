import time
import can

# Function to send CAN message using python-can
def send_can_message(bus, arbitration_id, data):
    message = can.Message(arbitration_id=arbitration_id, data=data, is_extended_id=False)
    try:
        bus.send(message)
        print(f"Message sent: ID=0x{arbitration_id:X}, Data: {' '.join(f'{byte:02X}' for byte in data)}")
    except can.CanError as e:
        print(f"Message not sent: {e}")

# Function to continuously send CAN messages
def continuous_can_send():
    # Try to create a CAN bus instance
    try:
        bus = can.interface.Bus(channel='PCAN_USBBUS2', interface='pcan', bitrate=500000) #Change the channel according to the CAN Bus connected to which port. In PCAN-USB X6, there are 6 ports, so I am using CAN3 port which signify PCAN_USBBUS2 in Pyhton code.
    except can.CanError as e:
        print(f"Failed to initialize CAN bus: {e}")
        return

    seventh_byte = 0x00  # Initialize 7th byte

    try:
        while True:
            # Brake Message
            #data_brake = [0x03, 0xC8, 0x00, 0x02, 0x00, 0x00, seventh_byte, 0x00]
            #data_brake[7] = data_brake[0] ^ data_brake[1] ^ data_brake[2] ^ data_brake[3] ^ data_brake[4] ^ data_brake[5] ^ data_brake[6]
            #send_can_message(bus, 0x131, data_brake)

            # Steering Message
            #data_other = [0x11, 0xFF, 0x00, 0x00, 0x0A, 0x00, seventh_byte, 0x00]
            #data_other[7] = data_other[0] ^ data_other[1] ^ data_other[2] ^ data_other[3] ^ data_other[4] ^ data_other[5] ^ data_other[6]
            #send_can_message(bus, 0x132, data_other)

            # Velocity Message
            #data_velocity = [0x11, 0x64, 0x00, 0x00, 0x00, 0x00, seventh_byte, 0x00]
            #data_velocity[7] = data_velocity[0] ^ data_velocity[1] ^ data_velocity[2] ^ data_velocity[3] ^ data_velocity[4] ^ data_velocity[5] ^ data_velocity[6]
            #send_can_message(bus, 0x130, data_velocity)

            # Increment 7th byte and reset to 0x00 if it reaches 0x10
            seventh_byte = (seventh_byte + 1) % 0x10

            # Sleep for 20 ms
            time.sleep(0.02)

    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        bus.shutdown()

if __name__ == "__main__":
    continuous_can_send()
