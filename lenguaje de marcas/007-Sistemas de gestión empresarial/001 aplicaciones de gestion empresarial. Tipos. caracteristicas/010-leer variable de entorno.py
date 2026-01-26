# En el shell (terminal):
# echo 'export NOMBRE="Pau"' >> ~/.bashrc
# source ~/.bashrc
import os

print(os.environ.get("NOMBRE"))
