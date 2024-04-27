#!/bin/bash

# Check if the script is run as root
if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

# Check for .env file
if [ ! -f /home/ec2-user/JT-Discord-Bot/.env ]; then
    echo "Create /home/ec2-user/JT-Discord-Bot/.env before deploying"
    exit
fi

# Install Python and other dependencies
sudo yum update -y
sudo yum install -y git python3 python3-pip

# Install Docker
sudo amazon-linux-extras install docker

#Install Redis
sudo yum install -y redis6

#Install Docker Compose
sudo yum install -y docker-compose

# Start Docker and enable it to run at startup
sudo service docker start
sudo systemctl enable docker

# Add the current user to the Docker group
sudo usermod -a -G docker $(whoami)

# Optionally, install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.5.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Clone the repository if not already cloned or pull latest changes
if [ ! -d "/home/ec2-user/JT-Discord-Bot" ]; then
    git clone https://github.com/cs220s24/JT-Discord-Bot.git /home/ec2-user/JT-Discord-Bot
else
    cd /home/ec2-user/JT-Discord-Bot
    git pull
fi

# Create a Python virtual environment and install dependencies
python3 -m venv /home/ec2-user/JT-Discord-Bot/.venv
/home/ec2-user/JT-Discord-Bot/.venv/bin/pip install -r /home/ec2-user/JT-Discord-Bot/requirements.txt

# Set up the Discord bot service
sudo cp /home/ec2-user/JT-Discord-Bot/discordbot.service /etc/systemd/system/discordbot.service
sudo systemctl enable discordbot
sudo systemctl start discordbot

echo "Deployment complete. The Discord bot service is up and running!"

