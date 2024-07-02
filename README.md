## Steps to Read CAN Data from Pixkit Moving Research Vehicle using PCAN USB Hardware and SavvyCAN

Follow these steps to read CAN data from the Pixkit Moving Research Vehicle using PCAN USB hardware and SavvyCAN software:

### Step 1: Download SavvyCAN Software

Download the SavvyCAN software from the following link: [SavvyCAN V213](https://github.com/collin80/SavvyCAN/releases/tag/V213)

### Step 2: Download PCAN Drivers

Download the PCAN drivers for Windows from the following link: [PCAN Drivers](https://www.peak-system.com/Drivers.523.0.html?&L=1)

### Step 3: Install PCAN Drivers

After downloading the PCAN drivers, unzip the file and install the drivers.

### Step 4: Launch SavvyCAN

Unzip the downloaded SavvyCAN folder and double-click on the `savvycan.exe` file to launch the application.

### Step 5: Connect CAN Bus DB9 Cable

Find the CAN Bus DB9 cable from the Pixkit Moving Research Vehicle and connect it to any of the ports on the PCAN hardware.

### Step 6: Open Connection in SavvyCAN

1. In SavvyCAN, click on the "Open Connection" option in the title bar.
2. Connect it with the PCAN hardware.

### Step 7: View CAN Data

Once the setup is complete, you will see data flowing in the main window of SavvyCAN with different IDs, values, data lengths, and frequencies. To make it more convenient:

1. Select the "Overwrite" mode in the right pane of the home window.
2. This will update the messages every time new data is received.

These steps will allow you to read and monitor CAN data from the Pixkit Moving Research Vehicle using PCAN USB hardware and SavvyCAN.

Certainly! Here are the steps to decode the CAN messages, formatted for a GitHub README file:

---

## Steps to Decode CAN Messages

Follow these steps to decode CAN messages from the Pixkit Moving Research Vehicle:

### Step 1: Observe Changes in CAN Data

1. **Read in the Data**: Start reading the CAN data using SavvyCAN.
2. **Issue Commands**: Give commands to the vehicle to move, apply the brake, change the steering, etc.
3. **Observe Changes**: Monitor the IDs and the bytes that are changing when these commands are given.

### Step 2: Analyze Changing Bytes

1. **Identify Changing Bytes**: After identifying which bytes are changing for a particular ID:
    - Find the maximum and minimum values of the changing parameter.
    - Check whether the values are signed or unsigned.
   
2. **Use Sniffer Feature**: Utilize the Sniffer feature in SavvyCAN to help with this analysis.
3. **Record and Analyze Data**: You can record the data for further analysis:
    - Record the CAN data while issuing commands to the vehicle.
    - Export the recorded data to an Excel file.
    - Analyze the data in Excel to identify patterns and decode the messages.

### Example Analysis

- **Movement Commands**: For Pixkit, We decoded the 0x530 Id and found out what bytes are changing and which are constant.
- **Brake Commands**: We decoded that Id 0x531 is for Vehicle Brake.
- **Steering Changes**: We decoded that Id 0x532 is for Vehicle Steering.

Using these steps, you can systematically decode CAN messages by correlating specific vehicle actions with changes in the CAN data. 
