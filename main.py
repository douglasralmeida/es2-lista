from flask import Flask
import os
import psycopg2 as psql

DB_URL = os.environ['DATABASE_URL']
SQL_FILME = 'SELECT nome FROM oscar.filmes WHERE ano = %d;'

app = Flask(__name__)
conn = psql.connect(DB_URL, sslmode='require')

def melhorfilme(ano):
  with conn:
    with conn.cursor() as cur:
      cur.execute(SQL_FILME, ano)
      cur.close
  cur = conn.cursor()
  cur.execute(SQL_FILME, ano)
  valor = cur.fetchone()
  cur.close()

  return valor[0]

@app.route('/')
def home():
  return 'Filme vencedor do Oscar por ano. Use https://url/oscar/ano'

@app.route("/filme/")
def semano():
  return "Erro na URL. Você deve passar um ano no parâmetro."

@app.route("/filme/<valor>")
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