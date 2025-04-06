from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Projeto Final rodando no OpenShift com Build automático!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
