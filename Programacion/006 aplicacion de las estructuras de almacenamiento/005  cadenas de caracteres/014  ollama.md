# Descargamos la instalacion de ollama

sudo apt install curl (si no teneis curl)
curl -fsSL https://ollama.com/install.sh | sh

# Comprobar la versión instalada

ollama --version

Alternativa con snap:
sudo snap install ollama

# Quiero saber los modelos que tengo instalados

ollama list
