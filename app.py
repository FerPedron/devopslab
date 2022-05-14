from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Bem Vindo ao APP FerPedron!"

if __name__ == '__main__':
    app.run()