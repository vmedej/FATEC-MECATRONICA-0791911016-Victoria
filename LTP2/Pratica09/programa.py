
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route("/ola")
def ola():
    return "Olá pessoas, meu nome é Victória"

@app.route("/pagina")
def primeira_pagina():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Page Title</title>
        </head>
        <body>
            <h1>This is a Heading</h1>
            <p>This is a paragraph.</p>
        </body>
    </html>
    """

@app.route("/pagina2")
def segunda_pagina():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Meu site mais bem  elaborado</title>
        </head>
        <body>
            <h1>Coisas aleatórias</h1>
            <p>Esse parágrafo está sendo escrito com um único intuito: Mostrar algo.</p>
            <iframe width="560" height="315" src="https://www.youtube.com/embed/b3nEaIPNx6Y" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </body>
    </html>
    """
