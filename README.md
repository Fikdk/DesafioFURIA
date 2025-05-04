# Chatbot FURIA - Desafio Técnico

Este projeto é uma solução para o **Desafio de Experiência Conversacional da FURIA**. A ideia é oferecer uma interface de chatbot que permita aos fãs da FURIA obter informações como:

- Roster dos jogadores brasileiros
- Quando serão os próximos jogos
- Site oficial da FURIA

---

## Tecnologias utilizadas

- [Python 3.10+](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
- HTML, CSS e JS para frontend básico

---

## Funcionalidades

- Interface de chatbot via web (Flask)
- Botões e mensagens rápidas
- Respostas em HTML com links clicáveis
- Web scraping do roster dos times

---

## Como rodar localmente

### 1. Clone o repositório:
git clone https://github.com/Fikdk/DesafioFURIA.git
cd DesafioFURIA
### 2. Crie um ambiente virtual (caso queira):
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
### 3. Instale as dependências:
flask
beautifulsoup4
### 4. Execute a aplicação:
flask run
