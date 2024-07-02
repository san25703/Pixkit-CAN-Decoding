## CAN Key Press Control Script

This Python script allows you to send CAN messages to control a vehicle or simulation system based on key presses using the `python-can` library with PCAN-USB hardware. The script reads user inputs and transmits corresponding CAN messages to control vehicle functions such as movement, steering, and braking.

### Prerequisites

To use this script, you need to install the following Python libraries:

- **`python-can`**: For CAN bus communication.
- **`keyboard`**: For capturing key press events.

You can install these libraries using pip:

```bash
pip install python-can keyboard
```

### Description

The script initializes a CAN bus interface and listens for key presses to send predefined CAN messages. It uses the `pcan` interface for the PCAN-USB hardware and operates at a bitrate of 500 kbps.

**Key Functions:**

- **`send_can_message(bus, arbitration_id, data)`**: Sends a CAN message with a specified `arbitration_id` and `data` payload.
- **`handle_key_press(bus)`**: Continuously checks for key presses and sends corresponding CAN messages for different vehicle functions.
- **`main()`**: Sets up the CAN bus and starts handling key press events.

### CAN Messages

- **Forward (Velocity Message)**: ID: `0x130`, Data: `[0x11, 0x64, 0x00, 0x00, 0x00, 0x00, seventh_byte, 0x00]`
  ```python
  if keyboard.is_pressed('w'):
      data_velocity = [0x11, 0x64, 0x00, 0x00, 0x00, 0x00, seventh_byte, 0x00]
      send_can_message(bus, 0x130, data_velocity)
      print("Forward")
  ```

- **Backward (Velocity Message)**: ID: `0x130`, Data: `[0x31, 0x64, 0x00, 0x00, 0x00, 0x00, seventh_byte, 0x00]`
  ```python
  if keyboard.is_pressed('s'):
      data_velocity = [0x31, 0x64, 0x00, 0x00, 0x00, 0x00, seventh_byte, 0x00]
      send_can_message(bus, 0x130, data_velocity)
      print("Reverse")
  ```

- **Left (Steering Message)**: ID: `0x132`, Data: `[0x11, 0xFF, 0x00, 0x00, 0x0A, 0x00, seventh_byte, 0x00]`
  ```python
  if keyboard.is_pressed('a'):
      data_left = [0x11, 0xFF, 0x00, 0x00, 0x0A, 0x00, seventh_byte, 0x00]
      send_can_message(bus, 0x132, data_left)
      print("Left")
  ```

- **Right (Steering Message)**: ID: `0x132`, Data: `[0x11, 0xFF, 0xFF, 0x00, 0x0A, 0x00, seventh_byte, 0x00]`
  ```python
  if keyboard.is_pressed('d'):
      data_right = [0x11, 0xFF, 0xFF, 0x00, 0x0A, 0x00, seventh_byte, 0x00]
      send_can_message(bus, 0x132, data_right)
      print("Right")
  ```

- **Brake (Space Bar)**: ID: `0x131`, Data: `[0x03, 0xC8, 0x00, 0x01, 0x00, 0x00, seventh_byte, 0x00]`
  ```python
  if keyboard.is_pressed('space'):
      data_brake_space = [0x03, 0xC8, 0x00, 0x01, 0x00, 0x00, seventh_byte, 0x00]
      send_can_message(bus, 0x131, data_brake_space)
      print("Brake (Space Bar)")
  ```

- **Brake (R Key)**: ID: `0x131`, Data: `[0x03, 0xC8, 0x00, 0x02, 0x00, 0x00, seventh_byte, 0x00]`
  ```python
  if keyboard.is_pressed('r'):
      data_brake_r = [0x03, 0xC8, 0x00, 0x02, 0x00, 0x00, seventh_byte, 0x00]
      send_can_message(bus, 0x131, data_brake_r)
      print("Brake (R) Released")
  ```

**Note**: The `seventh_byte` is updated in each iteration and used to generate a simple message checksum. 

### Usage

1. **Configure the CAN Channel**: Update the `channel` argument in the `can.interface.Bus` instantiation to match your PCAN-USB hardware port.
2. **Run the Script**: Execute the script to start sending CAN messages based on key presses. Messages are sent every 20 ms.

### Example Configuration

For `PCAN-USB X6` with CAN3 port:

```python
bus = can.interface.Bus(channel='PCAN_USBBUS2', interface='pcan', bitrate=500000)
```

### Example Key Presses

| Key       | Action               | CAN Message ID | Data                                                           |
|-----------|----------------------|----------------|----------------------------------------------------------------|
| **W**     | Move Forward         | `0x130`         | `[0x11, 0x64, 0x00, 0x00, 0x00, 0x00, seventh_byte, 0x00]`   |
| **S**     | Move Backward        | `0x130`         | `[0x31, 0x64, 0x00, 0x00, 0x00, 0x00, seventh_byte, 0x00]`   |
| **A**     | Turn Left            | `0x132`         | `[0x11, 0xFF, 0x00, 0x00, 0x0A, 0x00, seventh_byte, 0x00]`   |
| **D**     | Turn Right           | `0x132`         | `[0x11, 0xFF, 0xFF, 0x00, 0x0A, 0x00, seventh_byte, 0x00]`   |
| **Space** | Apply Brake          | `0x131`         | `[0x03, 0xC8, 0x00, 0x01, 0x00, 0x00, seventh_byte, 0x00]`   |
| **R**     | Release Brake        | `0x131`         | `[0x03, 0xC8, 0x00, 0x02, 0x00, 0x00, seventh_byte, 0x00]`   |

### Resources

- [python-can Documentation](https://python-can.readthedocs.io/)
- [keyboard Documentation](https://keyboard.readthedocs.io/)
