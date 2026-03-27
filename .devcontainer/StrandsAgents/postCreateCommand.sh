# bin/bash
pip install --no-cache --user --break-system-packages strands-agents 'strands-agents[a2a]' strands-agents-tools
pip config set install.user 'false'
pip config set global.index-url https://pypi.org/simple

# Shorten terminal prompt
echo 'export PS1="\$ "' >> ~/.bashrc
