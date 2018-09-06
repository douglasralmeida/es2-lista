from flask import Flask
import pandas as pd

app = Flask(__name__)
data = pd.read_csv("data.csv").values

def melhorfilme(ano):
  return data[ano-1929][1]

@app.route('/')
def home():
  return 'Filme vencedor do Oscar por ano. Use https://url/oscar/ano'

@app.route("/oscar/")
def semano():
  return "Erro na URL. Você deve passar um ano no parâmetro."

@app.route("/oscar/<valor>")
def oscar(valor):
  if not valor.isdigit():
    return "Erro na URL. O parâmetro passado deve ser um número inteiro positivo."
  valor = int(valor)
  if valor < 1929:
    return "Erro. A primeira premiação do Oscar ocorreu em 1929."
  if valor > 2018:
    return "Erro. O ano informado é maior que o ano atual."
  return melhorfilme(valor)

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)