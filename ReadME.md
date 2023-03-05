# Response AI - Utilizando API da OpenAI
A aplicação é um estudo sobre inteligência artificial, integrando a API da OpenAI para responder a perguntas em linguagem natural. A aplicação foi criada em Python e pode ser executada a partir do terminal.

Para utilizar a aplicação, basta ter uma API Key válida da OpenAI e inseri-la no código. Em seguida, basta executar o código e a aplicação será iniciada. O usuário poderá inserir perguntas em linguagem natural e a aplicação irá utilizar o modelo "text-davinci-003" da OpenAI para gerar uma resposta.

A biblioteca "halo" é utilizada para exibir uma animação de espera enquanto a resposta é gerada pela API. Além disso, são definidos alguns parâmetros na função "get_answer", como a temperatura, o número máximo de tokens e as penalidades de frequência e presença.

O código é acompanhado por comentários explicativos e é fácil de entender e modificar. O objetivo do projeto é fornecer uma demonstração simples e prática de como a API da OpenAI pode ser utilizada para criar aplicações de inteligência artificial em Python.

## Pré-requisitos
Para utilizar a aplicação, é necessário ter uma API Key válida da OpenAI. Caso não tenha, é possível criar uma conta na plataforma OpenAI e obter a sua chave de API.

link: https://platform.openai.com/signup

Insira sua API Key da OpenAI no arquivo responseAI.py

openai.api_key = "API-KEY"

## Como utilizar
Para iniciar a aplicação, execute o seguinte comando:

python openai_api.py

## Bibliotecas utilizadas
OpenAI
Halo

Para instalar as bibliotecas necessarias:

pip install openai
pip install halo

# Response AI - Using OpenAI API
This application is a study of artificial intelligence, integrating the OpenAI API to answer natural language questions. The application was created in Python and can be executed from the terminal.

To use the application, you need a valid API Key from OpenAI, which should be inserted into the code. Then, simply execute the code and the application will start. The user can enter natural language questions and the application will use the "text-davinci-003" model from OpenAI to generate an answer.

The "halo" library is used to display a waiting animation while the answer is generated by the API. In addition, some parameters are defined in the "get_answer" function, such as temperature, maximum number of tokens, and frequency and presence penalties.

The code is accompanied by explanatory comments and is easy to understand and modify. The project's goal is to provide a simple and practical demonstration of how the OpenAI API can be used to create artificial intelligence applications in Python.

## Prerequisites
To use the application, you need a valid API Key from OpenAI. If you don't have one, you can create an account on the OpenAI platform and obtain your API Key.

Link: https://platform.openai.com/signup

Insert your OpenAI API Key in the responseAI.py file:

openai.api_key = "API-KEY"

## How to use
To start the application, execute the following command:

python responseAI.py

## Libraries used
OpenAI
Halo

To install the required libraries, run the following commands:

pip install openai
pip install halo