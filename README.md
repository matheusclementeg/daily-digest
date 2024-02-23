#  Daily Digest - Notícias e Cotações Automatizadas 🗞️🤖

## Descrição do Projeto
O projeto Daily Digest é uma solução automatizada desenvolvida em Python, projetada para facilitar o acesso diário a informações cruciais sobre o mercado e notícias de interesse geral. Utilizando APIs poderosas como NewsAPI e ExchangeRate-API, este script busca as últimas notícias e cotações de moedas, compila essas informações em um formato de e-mail fácil de ler e envia automaticamente para uma lista de destinatários pré-configurada. Ideal para profissionais ocupados, investidores e qualquer pessoa interessada em manter-se atualizada sem o esforço de buscar essas informações manualmente todos os dias.

## Funcionalidades

**Busca Automatizada de Notícias:** Utiliza a NewsAPI para obter as últimas notícias sobre tópicos específicos como "bitcoin" e "adsense", limitando a busca às cinco principais notícias para garantir relevância e concisão.

**Atualização de Cotações de Moedas:** Através da ExchangeRate-API, busca a cotação mais recente do dólar em relação ao real, essencial para acompanhamento do mercado financeiro.

**Composição e Formatação de E-mail em HTML:** Organiza as notícias e cotações em um template de e-mail elegante e legível, incluindo títulos, imagens e descrições das notícias.

**Envio Automatizado de E-mails:** Com a API do Resend, envia o e-mail composto para uma lista de destinatários, facilitando a disseminação de informações.

## Como Funciona

O script é dividido em funções dedicadas para cada etapa do processo:

Obtenção de Dados: `obter_noticias()` e obter_cotacao_dolar() buscam informações atualizadas da internet.
Composição do E-mail: `compor_email()` organiza os dados obtidos em um formato de e-mail em HTML.
Envio do E-mail: `enviar_email(conteudo)` utiliza a API do Resend para enviar o e-mail aos destinatários configurados.
Instalação e Uso
Para utilizar o Daily Digest, você precisará de Python 3.x instalado em seu sistema e acesso à internet. Clone o repositório, instale as dependências listadas em requirements.txt e configure suas chaves de API nos locais indicados no script. Execute o script manualmente ou configure um agendador de tarefas para automação diária.

## Contribuições

Contribuições são bem-vindas! Se você tem melhorias, correções ou novas funcionalidades a sugerir, sinta-se à vontade para abrir um pull request ou uma issue. Juntos, podemos tornar o Daily Digest ainda mais poderoso e útil para nossa comunidade.

## Licença

Este projeto é distribuído sob a licença MIT, permitindo que seja livremente usado, modificado e distribuído.

