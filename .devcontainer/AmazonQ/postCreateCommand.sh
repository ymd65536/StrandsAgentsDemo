# bin/bash
sudo apt update -y
sudo apt upgrade -y
sudo apt install -y python3 python3-pip
pip install --user --break-system-packages strands-agents
pip config set install.user 'false'
pip config set global.index-url https://pypi.org/simple
