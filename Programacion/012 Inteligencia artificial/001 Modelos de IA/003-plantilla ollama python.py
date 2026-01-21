import json
import urllib.request

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5:3b-instruct"			#	Modelo de la IA

prompt = "Explica qué es PHP."		#Prompt que le pasamos al modelo de IA

data = {
    "model": MODEL,
    "prompt": prompt,
    "stream": False								#Utilizando false la informacion tardaria unos segundos en aparecer y nos daria el bloque entero de respuesta, en cambio utilizando true la informacion saldria palabra a palabra.
}

req = urllib.request.Request(
    OLLAMA_URL,
    data=json.dumps(data).encode("utf-8"),
    headers={"Content-Type": "application/json"}
)

with urllib.request.urlopen(req) as response:
    result = json.loads(response.read().decode("utf-8"))
    print(result["response"])

