from flask import Flask
import json 

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
    cadena = '''
        <doctype html>
<html lang ="es">     
    <head>
        <title>PAUblog</title>
        <meta charset="utf-8">
        <style>
         body{background:steelblue;color:steelblue;font-family:sans-serif;}
         header,main,footer{background:white;padding:20px;margin:auto;width:600px;}
         header,footer{text-aling:center;}
         main{color:black;}
        
         </style>
    </head>
   <body>
         <header><h1>PAUblog</h1></header>
          <main>
          '''
          ############################### ESTO ES OTRO BLOQUE
    cadena+='''
            <article>
            <h3>Titulo del articulo</h3>
            <time>2025-10-16</time>
            <p>Pau Contreras Romero</p>
            <p>Este es el contenido de un articulo ficticio</p>
          </article>
          '''
          ############################### ESTO ES OTRO BLOQUE
    cadena +='''
        </main>
        <footer>(c)2025 Pau Contreras Romero</footer>
      </body>
    </html>
    '''
    ############################## NO OS OLVIDEIS DE RETURN
    return cadena 
if __name__ == "__main__":
  aplicacion.run(debug=True)

