## CAN Message Transmission Script

This Python script demonstrates how to continuously send CAN messages using the `python-can` library with the PCAN-USB hardware. The script sets up a CAN bus instance and transmits a series of CAN messages at regular intervals.

### Prerequisites

To use this script, you need to install the `python-can` library. You can install it via pip:

```bash
pip install python-can
```

### Description

The script initializes a CAN bus interface and continuously sends a series of CAN messages. It uses the `pcan` interface for the PCAN-USB hardware and operates at a bitrate of 500 kbps. 

**Key Functions:**

- `send_can_message(bus, arbitration_id, data)`: Sends a CAN message with a specified `arbitration_id` and `data` payload.
- `continuous_can_send()`: Sets up the CAN bus and continuously sends a series of messages in a loop.

**CAN Messages:**

- **Brake Message**: Placeholder for sending a brake-related CAN message. ID: `0x131`
  ```python
  # Example: data_brake = [0x03, 0xC8, 0x00, 0x02, 0x00, 0x00, seventh_byte, 0x00]
  ```

- **Steering Message**: Placeholder for sending a steering-related CAN message. ID: `0x132`
  ```python
  # Example: data_other = [0x11, 0xFF, 0x00, 0x00, 0x0A, 0x00, seventh_byte, 0x00]
  ```

- **Velocity Message**: Placeholder for sending a velocity-related CAN message. ID: `0x130`
  ```python
  # Example: data_velocity = [0x11, 0x64, 0x00, 0x00, 0x00, 0x00, seventh_byte, 0x00]
  ```

The script includes commented-out sections for different types of CAN messages. Each message has an associated CAN ID and data format.

### Usage

1. **Configure the CAN Channel**: Update the `channel` argument in the `can.interface.Bus` instantiation to match your PCAN-USB hardware port.
2. **Run the Script**: Execute the script to start sending CAN messages. Messages are sent every 20 ms.

### Example Configuration

For `PCAN-USB X6` with CAN3 port:

```python
bus = can.interface.Bus(channel='PCAN_USBBUS2', interface='pcan', bitrate=500000)
```

### Notes

- The `seventh_byte` is updated in each iteration and used to generate a simple message checksum.
- Messages for brake, steering, and velocity are currently commented out and need to be customized based on your specific application.
