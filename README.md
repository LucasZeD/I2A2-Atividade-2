# Interface implementada e ajustes realizados para adequação, commit provisorio em repo particular para fins de deploy e uso da equipe e montagem de relatorio


# Desafio 2 – Agentes de Inteligência Artificial (i2a2)

Este projeto foi desenvolvido como parte do **Desafio 2** do curso da plataforma [i2a2](https://i2a2.com.br), com foco na criação de agentes de inteligência artificial.



## Objetivo

Criar um sistema com **agentes de IA** capazes de descompactar arquivos  e responder, de forma inteligente, às perguntas dos usuários referente aos arquivos descompactados.

## Estrutura do Projeto

O projeto está dividido em quatro agentes principais:

### 1. Agente de Prompt

Responsável por:

- Receber a pergunta do usuário
- Selecionar uma amostra dos dados
- Gerar um prompt estruturado com o passo a passo necessário para encontrar a resposta

### 2. Agente descompactador

Responsável por:

- Receber o arquivo compactado
- Descompacta os arquivos
- Retorna o dataset dos arquivos agrupados.

### 3. Agente Programador

Responsável por:

- Gera o melhor codigo python para responder a pergunta do usuário
- Gera o código para agrupar os arquivos
- Retorna o código para ser executado
- Gera gráficos

### 4. Agente executor

Responsável por:

- Cria a classe agente
- Envia os comandos para os outros agentes
- Guarda os dados do dataset e chaves

## Interface

Streamlit

## Estrutura de Arquivos

├── dataset/
│ ├── 202401_NFs_Cabecalho.csv
│ └── 202401_NFs_Itens.csv
├── agentes/
│   ├── agente_descompactador.py
│   ├── agente_descompactador_url.py
│   ├── agente_executor.py
│   ├── agente_programador.py
│   └── agente_prompt.py
├── venv/
├── agente.py
├── requirements.txt
└── README.md


## Como Executar

1. Clone o repositório:
    ```bash
    git clone https://github.com/ThiagoDFMaia/projeto_i2a2.git
    cd projeto_i2a2
    ```

2. Configuração do ambiente virtual do programa
   1. Crie o ambiente
        ```bash
        python -m venv venv
        ```
   2. Ative o ambiente
       * Windows
            ```bash
            .\venv\Scripts\activate
            ```
      * Linux/Mac
            ```bash
            python -m venv venv
            ```
   
3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Executea a aplicação streamlit:
    ```bash
    streamlit run app.py
    ```

5. Acesse a interface:
    Abra o navegador no endereço fornecido pelo Streamlit durante a execução do código.

## Próximos Passos
* Criar uma interface web com Flask - OK

* Permitir upload de arquivos CSV pelo usuário

* Tornar os agentes independentes e reutilizáveis

* Armazenar logs das perguntas e respostas

* Permitir o uso de outros modelos de LLMS

## Contribuição
* Contribuições são bem-vindas!
* Sinta-se à vontade para abrir issues ou enviar pull requests.


## Streamlit Community Cloud
Publique repo no gitgub
Acesse o Streamlit Community Cloud: Vá para share.streamlit.io e faça login com sua conta do GitHub.
Clique em "New app": No seu painel, clique no botão para criar uma nova aplicação.
Configure o Repositório:
    Repository: Escolha o repositório do GitHub que você acabou de preparar.
    Branch: Selecione a branch principal (geralmente main ou master).
    Main file path: Verifique se está apontando para app.py.
Adicione sua Chave de API (Segredo):
    Clique em "Advanced settings...".
    Na seção "Secrets", cole sua chave de API do Gemini no seguinte formato:
    '''Ini, TOML
    GEMINI_API_KEY = "sua_chave_de_api_aqui"
    '''
    Clique em "Save". O nome GEMINI_API_KEY deve corresponder exatamente ao que você usou no código (st.secrets.get("GEMINI_API_KEY")).
Clique em "Deploy!":
    O Streamlit irá construir o ambiente a partir do seu requirements.txt e iniciar sua aplicação. O processo pode levar alguns minutos.
    Após a conclusão, você receberá um link público para sua aplicação, que poderá compartilhar com qualquer pessoa.
