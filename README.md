# VLAN-Automation-Tool-using-Python-and-Netmiko

# VLAN Automation Tool using Python and Netmiko

This Python script automates VLAN creation on Cisco devices using the Netmiko library. It allows you to configure multiple VLANs across multiple devices with optional VLAN names.

## Features
- **Automated VLAN Creation:** Create multiple VLANs on multiple devices.
- **Input Validation:** Ensures proper IP address formatting and VLAN ID ranges.
- **Optional VLAN Naming:** VLANs can be created with or without names.
- **Error Handling:** Prevents duplicate VLAN IDs and handles connection errors gracefully.
- **Secure Input:** Uses `getpass` for secure credential entry.

---

## Requirements
- Python 3.x
- `netmiko` library

### Install Required Libraries
```bash
pip3 install netmiko
```

---

## How It Works
1. **Enter Credentials:** Provide the username, password, and enable secret.
2. **Enter Device IPs:** Input device IP addresses to target multiple devices.
3. **Enter VLAN IDs:** Provide VLAN IDs with built-in duplicate prevention.
4. **Enter VLAN Names:** Optionally assign names to VLANs (or skip).
5. **VLAN Configuration:** The script will connect to each device and apply the configurations.

---

## Usage
Run the script using the command:
```bash
python VLAN_automation.py
```

### Example Output:
```plaintext
Please enter the username: admin
Please enter the password:
Please enter the secret:
Please enter devices IPs one by one and type "done" when finished.
Enter IP: 192.168.1.1
Enter IP: done
Please enter VLAN IDs one by one and type "done" when finished.
Enter VLAN ID: 10
Enter VLAN ID: 20
Enter VLAN ID: done
Please enter VLAN names one by one. If no name, press enter and leave blank.
Enter VLAN name: Marketing
Enter VLAN name:
Enter VLAN name: done
Connecting to host 192.168.1.1......
VLANs have been configured successfully!
```

---

## Error Handling
- **Invalid IP Address:** Catches invalid IP addresses during input.
- **Duplicate VLAN IDs:** Prevents duplicate VLAN IDs from being entered.
- **Connection Errors:** Handles authentication and timeout errors using Netmiko exceptions.

---

## Known Issues
- Ensure devices have SSH access enabled.
- Only tested with Cisco IOS devices.

## Author
- **Mohamed Gowaied**
- LinkedIn: [Mohamed Gowaied](https://www.linkedin.com/in/mohamed-gowaied/)
- GitHub: [Mohamed Gowaied](https://github.com/gowaied)

