from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  return 'Filme vencedor do Oscar por ano. Use https://url/oscar/ano'

@app.route("/oscar/")
def semano():
  return "Erro na URL. Você deve passar um ano no parâmetro."

@app.route("/oscar/<ano>")
def melhorfilme(ano):
  if not ano.isdigit():
    return "Erro na URL. O parâmetro passado deve ser um número inteiro positivo."
  ano = int(ano)
  if ano < 1929:
    return "Erro. A primeira premiação do Oscar ocorreu em 1929."
  if ano > 2018:
    return "Erro. O ano informado é maior que o ano atual."
  return "Passou."

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)