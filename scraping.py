from bs4 import BeautifulSoup

def get_furia_valorant_roster():
    try:
        with open("web/valorant.html", "r", encoding="utf-8") as f:
            content = f.read()

        soup = BeautifulSoup(content, "html.parser")
        nomes_reais = soup.find_all("div", class_="team-roster-item-name-real")
        apelidos = soup.find_all("div", class_="team-roster-item-name-alias")

        if len(nomes_reais) != len(apelidos):
            return "Erro ao extrair dados."

        resposta = "<strong>Roster Atual de Valorant da FURIA Brasileiro:</strong><br>"
        for nome_real, apelido in zip(nomes_reais, apelidos):
            resposta += f"- {nome_real.text.strip()} (<strong>{apelido.text.strip()}</strong>)<br>"

        return resposta
    except Exception as e:
        return f"Erro ao ler o arquivo HTML: {str(e)}"
    
def get_furia_lol_roster():
    try:
        with open("web/lol.html", "r", encoding="utf-8") as f:
            content = f.read()

        soup = BeautifulSoup(content, "html.parser")
        tabela_desejada = soup.find("table", class_=[
        "wikitable",
        "sortable",
        "team-members",
        "hoverable-rows",
        "team-members-current",
        "jquery-tablesorter"
        ])
        
        if not tabela_desejada:
            return "Tabela não encontrada."

        nomes_reais = tabela_desejada.find_all("td", class_="team-members-irlname")
        apelidos = tabela_desejada.find_all("td", class_="team-members-player")

        if len(nomes_reais) != len(apelidos):
            return "Erro ao extrair dados."

        resposta = "<strong>Roster Atual de League Of Legends da FURIA Brasileiro:</strong><br>"
        for nome_real, apelido in zip(nomes_reais, apelidos):
            resposta += f"- {nome_real.text.strip()} (<strong>{apelido.text.strip()}</strong>)<br>"

        return resposta
    except Exception as e:
        return f"Erro ao ler o arquivo HTML: {str(e)}"

def get_furia_cs_roster():
    try:
        with open("web/cs2.html", "r", encoding="utf-8") as f:
            content = f.read()

        soup = BeautifulSoup(content, "html.parser")
        tabela_desejada = soup.find("table", class_=[
        "wikitable",
        "wikitable-striped",
        "roster-card"
        ])
        
        nomes_reais = soup.find_all("div", class_="LargeStuff")
        apelidos = soup.find_all("span", class_="inline-player")

        if len(nomes_reais) != len(apelidos):
            return "Erro ao extrair dados."

        resposta = "<strong>Roster Atual de Counter Strike 2 da FURIA Brasileiro:</strong><br>"
        for nome_real, apelido in zip(nomes_reais, apelidos):
            resposta += f"- {nome_real.text.strip()} (<strong>{apelido.text.strip()}</strong>)<br>"

        return resposta
    except Exception as e:
        return f"Erro ao ler o arquivo HTML: {str(e)}"