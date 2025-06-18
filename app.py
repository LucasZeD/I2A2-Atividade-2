'''
Cria interface web do usuário para o projeto i2a2 usando Streamlit.
Permite inserir credenciais de API da IA, carregar dados e interagir com o agente em fomato de chat
'''
import streamlit as st
from agente import AgenteController

# Configurações da página
st.set_page_config(
    page_title="i2a2 - Análise de CSV com Agentes de IA",
    page_icon=":robot:",
    layout="wide"
)

# Título da aplicação
st.title("i2a2 - Agente de IA para Análise de Arquivos CSV")
st.markdown("""
Para utilizar este aplicativo, você precisa de uma chave de API do GEMINI.


**Como usar:**
1.  **Configure o Agente** na barra lateral com sua chave de API e a URL do arquivo de dados.
2.  **Inicialize o Agente** clicando no botão "Inicializar Agente".
3.  **Converse com o Agente** na área de chat principal.
""")

# Gerenciamento do Estado da Sessão
# Inicializa o controlador e o estado do chat se não existirem
if 'agente_controller' not in st.session_state:
    st.session_state.agente_controller = AgenteController()
if 'agent_initialized' not in st.session_state:
    st.session_state.agent_initialized = False
if 'messages' not in st.session_state:
    st.session_state.messages = []
    
# Barra Lateral para Configuração do Agente
with st.sidebar:
    st.header("Configuração do Agente")
    
    # Use quando em ambiente de desenvolvimento
    # # Campo para inserir a chave da API
    # api_key = st.text_input(
    #     "Chave da API GEMINI",
    #     type="password",
    #     placeholder="Insira sua chave de API aqui"
    # )
    # Use quando em ambiente de produção
    # A chave de API será lida dos segredos do Streamlit
    api_key = st.secrets.get("GEMINI_API_KEY")

    # Como padrao o arquivo CSV é baixado do GitHub do projeto i2a2
    default_url = "https://github.com/grupo274/pre-projeto-i2a2/raw/refs/heads/thiago/projeto_i2a2_thiago/dataset/compactado/202401_NFs.zip"
    file_url = st.text_input(
        "URL do arquivo .zip",
        value=default_url,
        placeholder="Insira uma URL ublica publicada em outro site contendo uma base de dados com arquivo CSV aqui"
    )
    
    if st.button("Inicializar Agente", use_container_width=True):
        if not api_key:
            st.error("Por favor, insira sua chave de API.")
        elif not file_url:
            st.error("Por favor, insira a URL do arquivo CSV.")
        else:
            with st.spinner("Conectando ao agente e carregando dados... Por favor, aguarde."):
                controller = st.session_state.agente_controller
                status_message = controller.initialize_agente(api_key=api_key, file_url=file_url)
                
                if "✅" in status_message:
                    st.session_state.agent_initialized = True
                    st.success(status_message)
                    st.session_state.messages = [
                        {"role": "assistant", "content": "Olá! Estou pronto para responder suas perguntas sobre os dados carregados."}
                    ]
                else:
                    st.session_state.agent_initialized = False
                    st.error(status_message)
                
                
# Interface de Chat Principal
st.header("Converse com o Agente")

if not st.session_state.agent_initialized:
    st.warning("Por favor, inicialize o agente na barra lateral antes de fazer perguntas.")
else:
    # Exibe mensagens anteriores
    for message in st.session_state.messages:
        if message['role'] == 'user':
            st.chat_message("Usuário").write(message['content'])
        else:
            st.chat_message("Agente").write(message['content'])
    
    # Campo de entrada para perguntas
    user_input = st.chat_input("Faça uma pergunta sobre os dados...")
        
    if user_input:
        # Adiciona a pergunta do usuário às mensagens
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.write(user_input)
        
        with st.chat_message("assistant"):
            with st.spinner("Pensando..."):
                # Processa a pergunta através do controlador
                controller = st.session_state.agente_controller
                
                response = controller.ask_question(user_input)
                
                # St.markdown renderiza texto e blocos de código formatados
                st.markdown(response)
        
        # Adiciona a resposta do agente ao histórico
        st.session_state.messages.append({"role": "assistant", "content": response})

