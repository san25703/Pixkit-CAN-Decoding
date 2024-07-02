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
