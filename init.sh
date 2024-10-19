: ***

    ============
    MANUAL STEPS
    ============
    1. Get the Raspberry Pi Imager <https://www.raspberrypi.com/software/> and run it with your SD Card in your computer.  Configure as needed.

    2. Plug in the Pi and wait like 5 - 10 minutes for it to boot up.

    3. `sudo raspi-config` and turn on SSH.  (How to do this headless?)

    3. `sudo nmap -sn 192.168.1.0/24` and find the IP for the Raspberry Pi.  Or guess which one it is.

    4. Copy or create new ssh creds for the Rasp Pi.  From host: 
    
        ```shell
        scp -r ~/.ssh james@192.168.1.12:/home/james/
        ```

    5. Copy or create AWS creds if pushing to S3.  From host: 
        
        ```shell
        scp -r ~/.aws james@192.168.1.12:/home/james/
        ```

    6. SSH in and run the rest of this.

***

# APT installs for Python.
sudo apt-get update \
    && sudo apt-get -y upgrade \
    && sudo apt-get install python3-pip python3-venv python3-setuptools vim git

# Clone the repository for the reporting code.
git clone ssh://git@github.com/jsal13/pm25_air_quality

# Create venv, install blinka.
cd ~
python3 -m venv venv --system-site-packages

# Create the "venv" alias to activate venv.
echo 'alias venv="source venv/bin/activate"' >> .bashrc
. ~/.bashrc

# Download Blinka and install.
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py

source venv/bin/activate \
    && pip3 install --upgrade attrs boto3 adafruit-python-shell adafruit-circuitpython-pm25 \
    && sudo -E env PATH=$PATH python3 raspi-blinka.py

# Requires a reboot now!