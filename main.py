import cgi
import fileinput
import html
import os

from flask import Flask, render_template, request, redirect, url_for, make_response

import requests
from pandas import DataFrame
from requests.structures import CaseInsensitiveDict
from werkzeug.utils import secure_filename

url = "http://127.0.0.1:5000/"

headers = CaseInsensitiveDict()
headers["Authorization"] = "Basic ZXVtZXNtbzoxMTExMTExMTExMQ=="
headers["Content-Type"] = "application/x-www-form-urlencoded"

data = "uname=windson&psw=123456"

nome_do_usuario = ''

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/autenticacao", methods=['POST'])
def autenticacao():
    #  resp = requests.get(url, headers=headers, data=data)

    #   print(resp.status_code)

    #   dados = resp.content

    if request.method == 'POST':
        name = request.form['uname']
        password = request.form['psw']
        print(name, password)

    resp = make_response(principal(name))
    resp.set_cookie('userId', name)

    #  dado = name

    #  nome_do_usuario = name

    return resp


# return render_template("principal.html", dados=dados)


@app.route("/principal/<user>")
def principal(user):
    usuario = request.cookies.get('userId')
    return render_template("principal.html", user=usuario)


import cgi, os
import cgitb;
import werkzeug

cgitb.enable()
import pandas as pd
import openpyxl
import numpy as np


@app.route("/carregarExcel", methods=['POST'])
def carregar_excel():
    if request.method == 'POST':
        f = request.files['filename']
        f.save(secure_filename(f.filename))
        print(f)
        print(f.filename)

        #  df = pd.read_excel(f)

        # colunas do excel

        #   html = df.to_html(classes='table table-stripped')

        #  data_frame = pd.DataFrame(df)

        #  cabecalhos = df.head(df.size)

        #  npp = data_frame.columns.values

        #  return render_template("principal.html", dados=nome_do_usuario, filltab=df, cabecalhos=npp)

        # print(df)
        #   print(cabecalhos)
        # print(html)
        usuario = request.cookies.get('userId')

        resp = make_response(tabelacarregada(f))
        resp.set_cookie('fileId', f.filename)

    return resp


# return tabelacarregada(f)

# return render_template("tabelacarregada.html", file=f)


@app.route("/tabelacarregada/<file>", methods=['GET'])
def tabelacarregada(file):
    #  html = df.to_html(classes='table table-stripped')
    # cabecalhos = df.head(df.size)

    #  arq = fileinput.filename(file)

    usuario = request.cookies.get('userId')

    df = pd.read_excel(file)
    cabecalhos = df.keys()
    # head(df.size)
    valores = np.array(df.values)

    html = df.to_html(classes='table table-stripped', escape=False)

    print(cabecalhos)

    print(valores[0][0])
    ar = np.empty(valores.shape, dtype=str)

    print(ar)

    print(cabecalhos.size)


    #print(html)

   # valores.item()

   #cabecalhos.item()

    return render_template("tabelacarregada.html", headers=cabecalhos, user=usuario, tabela=valores, html=html)


if __name__ == "__main__":
    app.run(debug=True)
