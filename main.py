import requests
from datetime import datetime
import json

# Substitua pelos seus tokens de API
API_KEY_NEWS = "SUA_CHAVE_API_NEWSAPI"
API_KEY_RESEND = "SUA_CHAVE_API_RESEND"

# Funções para obter dados
def obter_noticias(kw='noticias'):
    try:
        url = f"https://newsapi.org/v2/everything?q={kw}&apiKey={API_KEY_NEWS}"
        resposta = requests.get(url)
        if resposta.status_code == 200:
            noticias = resposta.json()['articles'][:5]  # Limitar a 5 notícias
            noticias_formatadas = []
            for noticia in noticias:
                titulo = noticia['title']
                link = noticia['url']
                descricao = noticia.get('description', 'Descrição não disponível.')
                imagem_url = noticia.get('urlToImage', 'URL da imagem não disponível.')
                noticia_html = f"""
                <li>
                    <img src="{imagem_url}" alt="Imagem da notícia" style="width:100px;height:auto;">
                    <a href="{link}">{titulo}</a>
                    <p>{descricao}</p>
                </li>
                """
                noticias_formatadas.append(noticia_html)
            return "\n".join(noticias_formatadas)
        else:
            return f"<li>Não foi possível obter as notícias de {kw}.</li>"
    except Exception as e:
        return f"<li>Erro ao obter notícias de {kw}: {e}</li>"


def obter_cotacao_dolar():
    try:
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        resposta = requests.get(url)
        if resposta.status_code == 200:
            cotacao = resposta.json()['rates']['BRL']
            return cotacao
        else:
            return "Não foi possível obter a cotação do dólar."
    except Exception as e:
        return f"Erro ao obter a cotação do dólar: {e}"

# Compondo o e-mail
def compor_email():
    noticias_marketing = obter_noticias(kw='marketing')
    noticias_bitcoin = obter_noticias(kw='bitcoin')
    cotacao_dolar = obter_cotacao_dolar()
    data_hoje = datetime.now().strftime("%d/%m/%Y")
    
    conteudo_email = f"""
    <html>
        <body>
            <h2>Resumo do dia {data_hoje}:</h2>
            <p>Cotação do Dólar: R$ {cotacao_dolar:.2f}</p>
            <h3>Notícias de Marketing:</h3>
            <ul>{ noticias_marketing}</ul>
            <h3>Notícias sobre Bitcoin:</h3>
            <ul>{noticias_bitcoin}</ul>
        </body>
    </html>
    """
    return conteudo_email

# Enviando o e-mail
def enviar_email(conteudo):
    url = "https://api.resend.com/emails"
    dados_email = {
        "to": ["destinatario@example.com"],  # Assegure-se de que é uma lista
        "subject": "Resumo Diário",
        "html": conteudo,  # Usando o campo 'html' para conteúdo em HTML
        "from": "onboarding@resend.dev"
    }
    headers = {
        'Authorization': f'Bearer {API_KEY_RESEND}',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=json.dumps(dados_email))
    
    if response.status_code == 200:
        return "E-mail enviado com sucesso!"
    else:
        return f"Erro ao enviar e-mail: {response.status_code} {response.text}"
    
# Executar o script
if __name__ == "__main__":
    conteudo_email = compor_email()
    resultado_envio = enviar_email(conteudo_email)
    print(resultado_envio)
