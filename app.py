
from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
from scraping import get_furia_valorant_roster, get_furia_cs_roster, get_furia_lol_roster
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/responder', methods=['POST'])
def responder():
    pergunta = request.json.get('pergunta')

    if pergunta == "Qual o roster do time de Valorant da FURIA?":
        resposta = get_furia_valorant_roster()
    elif pergunta == "Qual o roster do time de CS2 da FURIA?":
        resposta = get_furia_cs_roster()
    elif pergunta == "Qual o roster do time de League of Legends da FURIA?":
        resposta = get_furia_lol_roster()
    elif pergunta == "Quando a FURIA joga?":
        resposta = (
            'Você pode acompanhar toda a agenda da FURIA pelo '
            '<a href="https://www.hltv.org/team/8297/furia#tab-matchesBox" target="_blank">HLTV, </a>'
            '(CS2) '
            'o calendário da FURIA de Valorant pelo '
            '<a href="https://www.vlr.gg/matches" target="_blank">VLR.GG, </a>'
            'e a agenda da FURIA de League of Legends pelo '
            '<a href="https://bo3.gg/pt/lol/matches/current?team_slug=furia-esports-lol&team_id=17448&period&date=2025-05-11" target="_blank">BO3.gg</a>'
        )
    elif pergunta == "Qual o site oficial da FURIA?":
        resposta = (
            'Site oficial da FURIA: '
            '<a href="https://www.furia.gg" target="_blank">furia.gg</a>'
        )
    else:
        resposta = "Ainda não tenho informações sobre isso!"

    return jsonify({"resposta": resposta})
