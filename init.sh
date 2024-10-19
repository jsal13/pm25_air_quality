## ============
## MANUAL STEPS
## ============
# 1. Get the Raspberry Pi Imager (https://www.raspberrypi.com/software/) and run it with your SD Card in your computer.  Configure as needed.
# 2. Plug in the Pi and wait like 5 - 10 minutes for it to boot up.
# 3. `sudo raspi-config` and turn on SSH.  (How to do this headless?)
# 3. `sudo nmap -sn 192.168.1.0/24` and find the IP for the Raspberry Pi.  Or guess which one it is.
# 4. SSH in and do the rest of this.

# APT installs for Python.
sudo apt-get update \
    && sudo apt-get -y upgrade \
    && sudo apt-get install python3-pip python3-venv python3-setuptools vim

# Create venv, install blinka.
cd ~
python3 -m venv venv --system-site-packages

# Create the "venv" alias to activate venv.
echo 'alias venv="source venv/bin/activate"' >> .bashrc
. ~/.bashrc

# Download Blinka and install.
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py

source venv/bin/activate \
    && pip3 install --upgrade adafruit-python-shell adafruit-circuitpython-pm25 \
    && sudo -E env PATH=$PATH python3 raspi-blinka.py

# Requires a reboot now!