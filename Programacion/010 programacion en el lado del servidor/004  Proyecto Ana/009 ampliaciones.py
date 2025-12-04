from flask import Flask, render_template, request
import io
import contextlib
import traceback

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("frente mejorado con IA.html")

@app.route("/api", methods=['POST'])
def api():

    # Recibir SIEMPRE texto plano
    raw_text = request.data.decode("utf-8")

    # Separar código e inputs si existen
    if "#INPUTS" in raw_text:
        partes = raw_text.split("#INPUTS", 1)
        codigo = partes[0].replace("#CODE", "").strip()
        entradas = partes[1].strip()
    else:
        codigo = raw_text.strip()
        entradas = ""

    # Preparar líneas de entrada para input()
    input_lines = iter(entradas.splitlines())

    buffer = io.StringIO()

    def custom_input(prompt=""):
        print(prompt, end="", file=buffer)
        try:
            linea = next(input_lines)
            print(linea, file=buffer)
            return linea
        except StopIteration:
            print("\n[AVISO] No hay más líneas de entrada.", file=buffer)
            return ""

    global_env = {
        "__name__": "__main__",
        "input": custom_input,
    }

    try:
        with contextlib.redirect_stdout(buffer):
            with contextlib.redirect_stderr(buffer):
                exec(codigo, global_env)
    except Exception:
        return traceback.format_exc(), 400

    salida = buffer.getvalue()
    return salida if salida else "OK"

if __name__ == "__main__":
    app.run(debug=True)

