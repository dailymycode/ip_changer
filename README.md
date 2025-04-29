# Automatically IP Changer using Tor

A Python script to automatically change your IP address using the Tor network. This script can change your IP at regular intervals, with the option for infinite mode, and will display the new IP in the terminal.

**Follow us on Instagram:** [@dailymycode](https://www.instagram.com/@dailymycode)


## Features

- Change IP automatically using Tor.
- Option to set a time interval between IP changes.
- Option to change IP a specific number of times or infinitely.
- Color-coded output for new IP address (Green).

## Requirements
Before using the script, make sure you have the following dependencies installed:

- Python 3
- Tor running on your machine
```bash
#### 1.Configure Your Browser
To properly use the Tor network with the script, you need to configure your browser to route traffic through the Tor network.

For example, set your browser to use the following proxy settings:

Proxy Type: SOCKS5

Host: 127.0.0.1

Port: 9050 

#### 2. Install Tor

First, make sure Tor is installed and running on your machine. You can install it using the following steps:

- **For Linux:**
 
  sudo apt update
  sudo apt install tor
  sudo systemctl enable tor
  sudo systemctl start tor

#### 3. Clone the Repository and Run

git clone https://github.com/dailymycode/ip_changer.git

cd ip_changer

python3 ip_changer.py